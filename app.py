from flask import Flask, request, render_template, jsonify
import requests
from geopy.distance import geodesic

app = Flask(__name__)

# 🔹 Convert Address to Lat/Lng using OpenStreetMap (Nominatim API)
def get_lat_lng(address):
    url = f"https://nominatim.openstreetmap.org/search?q={address}&format=json"
    response = requests.get(url)

    print("Response Status Code:", response.status_code)  # Debugging
    print("Response Text:", response.text)  # Debugging

    try:
        data = response.json()  # Convert response to JSON
    except requests.exceptions.JSONDecodeError:
        print("Error: Response is not in JSON format!")
        return None, None

    if data and len(data) > 0:
        return float(data[0]["lat"]), float(data[0]["lon"])

    return None, None

# 🔹 Get Nearby Healthcare Locations using OpenStreetMap (Overpass API)
def get_nearby_healthcare(lat, lng, radius=5000):
    overpass_url = "https://overpass-api.de/api/interpreter"
    overpass_query = f"""
    [out:json];
    node
      (around:{radius},{lat},{lng})
      ["amenity"~"hospital|clinic|pharmacy"];
    out;
    """
    response = requests.get(overpass_url, params={"data": overpass_query}).json()

    places = []
    for node in response.get("elements", []):
        place = {
            "name": node.get("tags", {}).get("name", "Unknown"),
            "lat": node["lat"],
            "lng": node["lon"],
            "address": node.get("tags", {}).get("addr:street", "Unknown Address"),
        }
        places.append(place)

    return places

# 🔹 Sort locations by distance
def sort_by_distance(user_lat, user_lng, places):
    user_location = (user_lat, user_lng)
    return sorted(
        places, 
        key=lambda place: geodesic(user_location, (place["lat"], place["lng"])).miles
    )

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        address = request.form["address"]

        lat, lng = get_lat_lng(address)  # Convert address to lat/lng
        if lat is None or lng is None:
            return "Invalid address. Please try again."

        # Fetch & sort healthcare locations
        places = get_nearby_healthcare(lat, lng)
        sorted_places = sort_by_distance(lat, lng, places)[:5]  # Top 5 results

        return render_template("index.html", places=sorted_places, address=address)

    return render_template("index.html", places=None)

if __name__ == "__main__":
    app.run(debug=True)

