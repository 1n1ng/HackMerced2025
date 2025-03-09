from flask import Flask, request, render_template
import requests
from geopy.distance import geodesic

app = Flask(__name__)

# 🔹 Convert Address to Lat/Lng using OpenStreetMap (Nominatim API)
def get_lat_lng(street, city, state, country):
    full_address = f"{street}, {city}, {state}, {country}"
    url = f"https://nominatim.openstreetmap.org/search?q={full_address}&format=json"

    headers = {
        "User-Agent": "MyHealthcareApp/1.0 (your@email.com)"  # Use a valid email or app name
    }

    response = requests.get(url, headers=headers)
    
    print("🔹 Requested Address:", full_address)
    print("🔹 API Response Code:", response.status_code)
    print("🔹 API Response Text:", response.text)

    if response.status_code == 403:
        print("❌ Error: Blocked by Nominatim. Try again later.")
        return None, None

    try:
        data = response.json()
        if not data:
            print("❌ No results found for this address.")
            return None, None
    except requests.exceptions.JSONDecodeError:
        print("❌ Error: Response is not in JSON format!")
        return None, None

    print("✅ Parsed Lat:", data[0]["lat"], "Lng:", data[0]["lon"])
    return float(data[0]["lat"]), float(data[0]["lon"])

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

# 🔹 Get 211 Resources using API (Alternative Resources)
def get_211_resources(lat, lng):
    url = f"https://api.211.org/resources?latitude={lat}&longitude={lng}&radius=5000"
    response = requests.get(url)
    
    resources = []
    if response.status_code == 200:
        data = response.json()
        for resource in data.get('data', []):
            resource_details = {
                "name": resource.get("name", "Unknown Resource"),
                "lat": lat,  # Using the same lat/lng for the resource, may need more precise data if available
                "lng": lng,
                "address": resource.get("address", "Unknown Address")
            }
            resources.append(resource_details)
    else:
        print(f"❌ Error fetching 211 resources: {response.status_code}")
    
    return resources

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
        street = request.form["street"]
        city = request.form["city"]
        state = request.form["state"]
        country = request.form["country"]

        lat, lng = get_lat_lng(street, city, state, country)
        if lat is None or lng is None:
            return render_template("index.html", error="Invalid address. Please try again.")

        # Fetch healthcare locations and 211 resources
        healthcare_places = get_nearby_healthcare(lat, lng)
        resources_211 = get_211_resources(lat, lng)
        
        # Combine both sources of resources
        all_places = healthcare_places + resources_211
        
        # Sort all places by distance
        sorted_places = sort_by_distance(lat, lng, all_places)[:5]  # Top 5 results

        return render_template("index.html", places=sorted_places, address=f"{street}, {city}, {state}, {country}")

    return render_template("index.html", places=None)

if __name__ == "__main__":
    app.run(debug=True)


