# Agent IA - Analyse de documents

Agent conversationnel capable d'analyser des documents PDF et de répondre à des questions dessus.

## Technologies utilisées
- Python
- OpenAI API (GPT-4o-mini)
- LangChain
- Streamlit
- PyPDF2

## Fonctionnalités
- Chat conversationnel avec mémoire
- Upload d'un PDF et questions sur son contenu
- Interface web avec Streamlit

## Lancer le projet
```bash
pip install -r requirements.txt
python -m streamlit run agent_pdf.py
```

## Configuration
Créer un fichier `.env` avec :
```
OPENAI_API_KEY=ta_clé_ici
```