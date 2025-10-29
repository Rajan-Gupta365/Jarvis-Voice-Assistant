import google.generativeai as genai

# ✅ Correct API key
genai.configure(api_key="AIzaSyAV7nXYMei8jijfIPPfh8E17cDkFLXpnB0")

try:
    # ✅ Using the correct model from your list
    model = genai.GenerativeModel("models/gemini-2.5-flash")

    response = model.generate_content("Who is Donald Trump?")
    print("AI Response:", response.text)

except Exception as e:
    print("Error:", e)
