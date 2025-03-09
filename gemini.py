try:
    from google import genai
    
    client = genai.Client(api_key="AIzaSyBq-hPsmp9GxmF08z0Fnkh6l53SM3sQq08")
    response = client.models.generate_content(
        model="gemini-2.0-flash", contents="Explain how AI works for short"
    )
    print("Response received:")
    print(response.text)
except Exception as e:
    print(f"An error occurred: {e}")