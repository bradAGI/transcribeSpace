from google import generativeai as genai
from pathlib import Path

# Configure API key
genai.configure(api_key="YOUR_API_KEY")

print("Uploading file...")
# Upload the file
uploaded_file = genai.upload_file(path="output.mp3")
print(f"File uploaded: {uploaded_file.display_name} (ID: {uploaded_file.name})")

# Transcribe using Gemini
prompt = 'Generate a transcript of the speech.'
print("Transcribing...")

model = genai.GenerativeModel(model_name="models/gemini-1.5-flash-latest")
response = model.generate_content([prompt, uploaded_file])

# Save output properly
output_path = Path("gemini_output.txt")

with output_path.open("w", encoding="utf-8") as f:
    f.write("".join(part.text for part in response.parts if hasattr(part, "text")))

print(f"Saved to {output_path.absolute()}")

