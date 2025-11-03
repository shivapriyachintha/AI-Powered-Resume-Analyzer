import google.generativeai as genai

genai.configure(api_key="AIzaSyCWKbbJHtNtEEhhC5SKPWmp7ACGODYbhE")

try:
    models = genai.list_models()
    print("Valid API Key! Models available:")
    for model in models:
        print(model.name)
except Exception as e:
    print("API key validation error:", str(e))
