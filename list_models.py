import google.generativeai as genai
import os

genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

def list_models():
    print("Available Gemini Models:")
    for model in genai.list_models():
        print(f"  Name: {model.name}")
        print(f"  Description: {model.description}")
        print(f"  Supported generation methods: {model.supported_generation_methods}\n")

if __name__ == "__main__":
    list_models()
