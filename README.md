 # Social-to-Lead Agent (AutoStream)

## Project Overview
This project implements a conversational AI agent designed to convert user interactions into qualified business leads. The system simulates a real-world SaaS assistant for AutoStream, an automated video editing platform.

Unlike basic chatbots, this agent performs structured reasoning by identifying user intent, retrieving accurate information from a knowledge base, tracking conversation state, and executing actions such as lead capture.

---

## Problem Statement
Businesses often struggle to convert casual user conversations into actionable leads. Traditional chatbots respond to queries but fail to identify high-intent users and do not trigger meaningful backend actions.

This project addresses that gap by building an agent that:
- Understands user intent
- Provides accurate product information
- Detects high-intent users
- Captures lead details automatically

---

## System Architecture
User Input  
→ Intent Detection  
→ Decision Layer  
→ Product Query → Knowledge Retrieval (RAG)  
→ High Intent → Lead Capture Flow  
→ Tool Execution  

State is maintained using a custom AgentState class to support multi-turn conversations and ensure continuity.

---

## Key Components

### Intent Detection
Classifies user input into greeting, product query, or high intent using rule-based logic with fuzzy matching support.

### Knowledge Retrieval (RAG)
Fetches accurate responses from a structured JSON knowledge base instead of generating answers blindly.

### State Management
Tracks user details and conversation flow to enable multi-step interactions and avoid duplicate lead capture.

### Lead Capture Workflow
Collects name, email, and platform only after detecting high intent, then triggers tool execution.

### Tool Execution
Simulates backend processing using a mock function:mock_lead_capture(name, email, platform)

---

## Why This Approach
- Rule-based intent detection ensures fast and interpretable behavior
- JSON-based RAG provides controlled and accurate responses
- State management enables realistic conversational flow
- Tool execution simulates real business workflows

---

## Edge Cases Handled
- Handles user typos using fuzzy matching
- Prevents duplicate lead submissions
- Maintains conversation continuity across multiple turns
- Differentiates between informational queries and action intent

---

## Tech Stack
- Python
- Rule-based NLP
- JSON-based Knowledge Base
- CLI-based Interface

---

## How to Run

Clone the repository:git clone https://github.com/sanjana-102005/social-to-lead-agent.git

Navigate to the project folder:cd social-to-lead-agent

Run the application:python app.py

---

## Example Interaction

User: What is your pricing?  
Agent: Displays pricing details  

User: I want Pro plan  
Agent: Starts lead capture  

Agent: Lead captured successfully  

---

## WhatsApp Integration (Concept)
This system can be extended using APIs such as Twilio or Meta WhatsApp Cloud API.

Flow:
User → Webhook → Backend (Flask/FastAPI) → Agent → Response → User

---

## Future Improvements
- LLM-based intent classification
- Vector database for advanced RAG
- Web interface (Streamlit or React)
- Deployment as an API service

---

## Author
Sanjana Kulkarni
