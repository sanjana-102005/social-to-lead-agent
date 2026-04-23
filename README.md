 Social-to-Lead Agent (AutoStream)

 Project Overview

This project demonstrates an AI-powered conversational agent designed to convert user interactions into qualified business leads. It simulates a real-world SaaS assistant for **AutoStream**, an automated video editing platform.



 Key Features

*  Intent Detection (Greeting, Product Query, High Intent)
*  RAG-based Knowledge Retrieval (from local JSON)
*  Multi-turn Conversation Memory
*  Lead Capture Workflow (Name, Email, Platform)
*  Tool Execution (Mock Lead Capture API)

 System Architecture

User Input
↓
Intent Detection
↓
→ Product Query → RAG Retrieval
→ High Intent → Lead Capture Flow
↓
Tool Execution

State is maintained using a custom `AgentState` class for smooth conversation handling.



 Tech Stack

* Python
* Rule-based NLP
* JSON-based Knowledge Base
* CLI-based Interface



 How to Run

bash
python app.py




 Example Interaction

User: What is your pricing?
Bot: [Displays pricing using RAG]

User: I want Pro plan
Bot: [Collects user details]

Bot: Lead captured successfully


WhatsApp Integration (Concept)

This system can be extended to WhatsApp using:

* Twilio API / Meta WhatsApp Cloud API
* Webhook → Backend (Flask/FastAPI)
* Agent processes message → Sends response


 Future Improvements

* LLM-based intent classification
* Vector database (FAISS / Pinecone) for advanced RAG
* Web UI (Streamlit / React)
* Deployment as API service



 Author

Sanjana Kulkarni
