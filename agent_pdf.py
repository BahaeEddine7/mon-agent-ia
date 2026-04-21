import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import PyPDF2
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.title("Agent IA - Analyse de documents")
st.write("Upload un PDF et pose des questions dessus !")

pdf_file = st.file_uploader("Choisis un PDF", type="pdf")

if pdf_file:
    reader = PyPDF2.PdfReader(pdf_file)
    texte = ""
    for page in reader.pages:
        texte += page.extract_text()
    
    st.success(f"PDF chargé ! ({len(reader.pages)} pages)")
    
    question = st.text_input("Ta question :")
    
    if question:
        reponse = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": f"Tu es un assistant comptable. Voici le contenu du document : {texte}"},
                {"role": "user", "content": question}
            ]
        )
        
        st.write("**Réponse :**")
        st.write(reponse.choices[0].message.content)