import google.generativeai as genai


genai.configure(api_k="use your own api key")

try:
     
    model = genai.GenerativeModel("models/gemini-2.5-flash")

    response = model.generate_content("Who is Donald Trump?")
    print("AI Response:", response.text)

except Exception as e:
    print("Error:", e)
