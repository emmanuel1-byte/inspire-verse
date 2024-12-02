import google.generativeai as gemini
import os
import dotenv

dotenv.load_dotenv()

gemini.configure(api_key=os.getenv("GOOGLE_GEMINI_API_KEY"))

model = gemini.GenerativeModel("gemini-1.5-flash")
