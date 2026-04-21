from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini")

historique = []

print("Agent LangChain démarré ! Tape 'quitter' pour arrêter.\n")

while True:
    question = input("Toi : ")
    
    if question.lower() == "quitter":
        print("Au revoir !")
        break
    
    historique.append(HumanMessage(content=question))
    
    reponse = llm.invoke(historique)
    
    historique.append(AIMessage(content=reponse.content))
    
    print(f"\nAgent : {reponse.content}\n")