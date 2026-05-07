import pandas as pd
from google import genai
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("Error: API Key Not Found")
else:
    try:
        client = genai.Client(api_key=api_key)

        print("Mengecek model yang tersedia...")
        available_models = [m.name for m in client.models.list() if 'generateContent' in m.supported_actions]
        
        selected_model = "gemini-1.5-flash"
        if "models/gemini-1.5-flash" not in available_models:
        
            if available_models:
                selected_model = available_models[0].replace("models/", "")
        print(f"Menggunakan model: {selected_model}\n")

        path_data = 'dataset_tweet_sentiment_pilkada_DKI_2017.csv'
        df = pd.read_csv(path_data)

        sample_rows = df.sample(2)

        print("=== ANALISIS SENTIMEN PILKADA DKI DENGAN GEMINI AI ===\n")

        for _, row in sample_rows.iterrows():
            tweet = row['Text Tweet']
            label_dataset = row['Sentiment']

            response = client.models.generate_content(
                model=selected_model,
                contents=f"Analisis Tweet Berikut: {tweet}"
            )
            print(f"Tweet: {tweet}")
            print(f"Sentimen Asli: {label_dataset}")
            print(f"Analisis AI:\n{response.text}")
            print("-"*50)

    except Exception as e:
        print(f"Error: {e}")

