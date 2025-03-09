try:
    from google import genai

    client = genai.Client(api_key="AIzaSyBq-hPsmp9GxmF08z0Fnkh6l53SM3sQq08")

    user_query = "Explain how AI works for short"  # Example input

    # Modify the AI prompt to enforce the healthcare restriction
    system_prompt = (
        "You are a strict healthcare assistant. You ONLY provide information related to healthcare, "
        "medicine, medical conditions, treatments, wellness, and similar topics. "
        "If the user asks anything outside of healthcare, refuse to answer."
    )

    full_prompt = f"{system_prompt}\n\nUser Query: {user_query}"

    response = client.models.generate_content(
        model="gemini-2.0-flash", contents=full_prompt
    )

    print("Response received:")
    print(response.text)

except Exception as e:
    print(f"An error occurred: {e}")

