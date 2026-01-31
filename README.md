# A2A Meeting Coordinator

**A2A Meeting Coordinator** is an experimental multi-agent coordination framework built using the **A2A SDK**. It enables autonomous agents to schedule meetings by negotiating directly with one another through structured A2A messages.

This repository demonstrates three agents — each implemented with a different AI framework — coordinating to schedule a meeting based on availability.

---

## 🚀 Project Overview

In this setup:

- **Miles** is the **host agent** responsible for organizing the meeting.
- **John** and **Ava** are **participant agents** who respond with availability.
- All agents communicate using **A2A Meeting Coordinator**, exchanging structured A2A messages.

The goal is to reach agreement on a common meeting time using automated negotiation.

---

## 🤖 Agents & Tech Stack

| Agent Name | Role | Framework | Port |
|------------|------|-----------|------|
| **Miles** | Host / Coordinator | **Google ADK** | 8000 (ADK Web UI) |
| **John** | Participant | **Crew AI** | 10004 |
| **Ava** | Participant | **LangChain** | 10003 |

### 🧠 Technology Summary

- **A2A SDK** – Cross-agent messaging framework defining structured protocols.
- **Google ADK** – Agent Development Kit used to implement Miles (the host).
- **Crew AI** – Used to implement John, a participant agent.
- **LangChain** – Used to implement Ava, another participant agent.

---

## 📦 Installation

### Prerequisites

- Python 3.10 or higher
- Google API Key (for Gemini models)

### Setup

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd a2a-meeting-coordinator
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
   
   Or if using `uv`:
   ```bash
   uv pip install -r requirements.txt
   ```

3. **Set up environment variables:**
   
   Create a `.env` file in the project root:
   ```bash
   GOOGLE_API_KEY=your_google_api_key_here
   ```

---

## 🏃 Running the Agents

The agents need to be run in separate terminal windows/sessions. Start the participant agents first, then the host agent.

### Terminal 1: Start Ava Agent (LangChain)
```bash
cd ava_agent
python main.py
```
Ava agent will start on `http://localhost:10003`

### Terminal 2: Start John Agent (Crew AI)
```bash
cd john_agent
python main.py
```
John agent will start on `http://localhost:10004`

### Terminal 3: Start Miles Agent (Google ADK)
```bash
cd miles_agent
python agent.py
```
Miles agent will connect to the participant agents and coordinate the meeting.

---

## 📡 Communication Protocol

Agents communicate through A2A messages that follow predetermined intents:

- `availability_request`: Sent by the host to ask for availability.
- `availability_response`: Participants reply with available time slots.
- `meeting_proposal`: Host proposes a time based on responses.
- `meeting_confirmation`: Participants confirm acceptance.

All messages conform to the structured A2A message format, ensuring compatibility across frameworks.

---

## 📅 Scheduling Workflow

1. **Miles (Host)** requests availability from **John** and **Ava**
   - Sends `availability_request` to each agent.
2. **Participants** send back availability
   - `availability_response` with a list of free time slots.
3. **Miles collects responses**
   - Identifies a common time slot that works for both John and Ava.
4. **Miles proposes a meeting**
   - Sends `meeting_proposal` with the selected time.
5. **Participants confirm**
   - Each agent sends `meeting_confirmation`.
6. Once all confirmations are received, the meeting is finalized.

---

## 📁 Project Structure

```
a2a-meeting-coordinator/
├── ava_agent/          # LangChain-based participant agent
│   ├── agent.py        # Agent implementation
│   ├── agent_executor.py
│   ├── main.py         # Server entry point
│   └── tools.py        # Availability checking tools
├── john_agent/         # Crew AI-based participant agent
│   ├── agent.py        # Agent implementation
│   ├── agent_executor.py
│   ├── main.py         # Server entry point
│   └── tools.py        # Availability checking tools
├── miles_agent/        # Google ADK-based host agent
│   ├── agent.py        # Agent implementation
│   └── tools.py        # Meeting scheduling tools
├── main.py             # Root entry point
├── requirements.txt    # Python dependencies
├── pyproject.toml      # Project configuration
└── README.md          # This file
```

---

## 🔧 Configuration

- **Port Configuration**: Default ports are defined in each agent's `main.py`:
  - Ava: `10003`
  - John: `10004`
  - Miles: Connects to the participant agents via their URLs

- **Agent URLs**: Miles agent connects to participants at:
  - `http://localhost:10004` (John)
  - `http://localhost:10003` (Ava)

---

## 📝 Notes

- Each agent maintains its own availability calendar (dummy data for demonstration).
- The agents use in-memory task stores and push notification clients.
- All agents require a valid `GOOGLE_API_KEY` environment variable for Gemini model access.

---

## 🤝 Contributing

This is an experimental project demonstrating multi-agent coordination. Contributions and improvements are welcome!