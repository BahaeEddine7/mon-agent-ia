from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

historique = []

print("Agent IA démarré ! Tape 'quitter' pour arrêter.\n")

while True:
    question = input("Toi : ")
    
    if question.lower() == "quitter":
        print("Au revoir !")
        break
    
    historique.append({"role": "user", "content": question})
    
    reponse = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Tu es un assistant comptable intelligent."}
        ] + historique
    )
    
    message = reponse.choices[0].message.content
    historique.append({"role": "assistant", "content": message})
    
    print(f"\nAgent : {message}\n")