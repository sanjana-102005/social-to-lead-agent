# 🤖 Social-to-Lead Agent (AutoStream)

## 📌 Overview
This project implements an AI-powered conversational agent that converts user interactions into qualified leads. The agent simulates a real-world SaaS sales assistant for AutoStream, an automated video editing platform.

---

## 🚀 Features

- Intent Detection (Greeting, Product Query, High Intent)
- RAG-based Knowledge Retrieval (from local JSON)
- Conversational Memory (multi-turn interaction)
- Lead Capture Workflow (Name, Email, Platform)
- Tool Execution (Mock Lead Capture API)

---

## 🧠 Architecture

User Input → Intent Detection →  
→ If Query → RAG Retrieval  
→ If High Intent → Lead Capture Flow  
→ Tool Execution  

State is managed using a custom AgentState class that tracks conversation flow and user details.

---

## 🛠️ Tech Stack

- Python
- Rule-based Intent Detection
- JSON-based RAG
- CLI-based conversational interface

---

## ▶️ How to Run

```bash
python app.py

