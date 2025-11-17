# 🧠 MindfulAI: 24/7 Mental Health Crisis Support & Wellness Companion

**Built with Official Google ADK**

**Track:** Agents for Good (Healthcare)

**Subtitle:** Intelligent multi-agent system providing accessible, 24/7 mental health support with crisis detection, empathetic intervention, and resource coordination using the official Google Agent Development Kit.

---

## 📋 Project Description

### Problem Statement

Mental health crises don't follow business hours. According to the CDC, suicide is a leading cause of death in the United States, with someone dying by suicide every 11 minutes. Meanwhile:

- **Immediate crisis support is hard to access**: Traditional crisis hotlines can have long wait times
- **Between-session support gaps**: Therapy typically happens once a week
- **Resource navigation is complex**: Finding appropriate mental health resources is overwhelming
- **Stigma and accessibility barriers**: Many people hesitate to reach out for help

**This matters because lives are at stake**, and accessible, immediate mental health support can prevent crises and save lives.

### Why Agents?

**Agents are the RIGHT solution because:**

1. **24/7 Immediate Response** - No wait times, crucial for crisis situations
2. **Specialized Expertise via Multi-Agent Architecture** - Each agent has specific training (triage, crisis, support, resources) like a care team
3. **Intelligent Tool Use** - Active crisis detection, mood tracking, resource finding beyond static responses
4. **Contextual Memory** - ADK's built-in session management provides personalized support
5. **Dynamic Orchestration** - Intelligent routing based on urgency and need using ADK's agent coordination
6. **Scalability** - Support for unlimited users simultaneously

This is a **true multi-agent system built with Google ADK**, not a chatbot—specialized LLM agents collaborate using tools and memory.

### What I Created

A production-quality multi-agent system using **official Google ADK** featuring:

**ADK-Powered Architecture:**
- **Multi-Agent System** using `LlmAgent` with `sub_agents`
- **4 Specialized Agents** (Triage, Crisis, Support, Resource)
- **4 Custom Tools** wrapped as ADK `FunctionTool`
- **ADK Session Management** via `InMemorySessionService`
- **Gemini 2.0 Flash Integration** for all agents
- **Console Runner** using ADK's `run_in_console`

**Agent Workflow:**
```
User Message
    ↓
Coordinator Agent (ADK)
    ↓
Triage Agent → Uses detect_crisis tool
    ↓
[If Crisis] → Crisis Agent → get_crisis_resources tool
[If No Crisis] → Support Agent → log_mood + get_coping_strategies tools
    ↓
[If Needed] → Resource Agent → get_crisis_resources tool
```

### Demo

**Installation:**
```bash
pip install -r requirements.txt
```

**Run the ADK-powered system:**
```bash
python adk_main.py
```

This launches an interactive console powered by Google ADK where you can:
- Have natural conversations with the multi-agent system
- See agents automatically coordinating based on your needs
- Get crisis support, coping strategies, mood tracking, and resource help

**Example Interaction:**
```
User: "I'm feeling really anxious and can't calm down"
→ Triage Agent assesses (uses detect_crisis tool)
→ Support Agent provides help (uses log_mood + get_coping_strategies tools)
→ Response includes: mood tracking, anxiety coping strategies, and support
```

### The Build

**Technologies:**
- **Google ADK (`google-adk>=1.18.0`)** - Official Agent Development Kit
- **Gemini 2.0 Flash** - Powers all agents
- **ADK LlmAgent** - For multi-agent orchestration
- **ADK FunctionTool** - For custom tools
- **ADK InMemorySessionService** - For session management
- **Rich** - For beautiful terminal UI

**Development Approach:**
- Problem-first design from mental health research
- Safety-first architecture (crisis detection primary)
- **Official ADK patterns** for agent orchestration
- **ADK tools** for functionality augmentation
- **ADK session management** for state handling

**ADK Key Concepts Implemented:**

1. ✅ **Multi-Agent System (ADK `LlmAgent` + `sub_agents`)**
   - Coordinator agent with 4 specialized sub-agents
   - Sequential workflow orchestrated by ADK
   - Each agent has dedicated tools and instructions

2. ✅ **Custom Tools (ADK `FunctionTool`)**
   - `detect_crisis` - Crisis indicator detection with severity scoring
   - `log_mood` - Longitudinal mood tracking with trend analysis
   - `get_crisis_resources` - Mental health resource database
   - `get_coping_strategies` - Evidence-based strategy recommendations

3. ✅ **Sessions & Memory (ADK `InMemorySessionService`)**
   - Built-in session lifecycle management
   - Conversation state preservation
   - Context maintained across turns

4. ✅ **Built-in Tools (ADK `google_search` - extendable)**
   - System designed to integrate ADK's `google_search` tool
   - Architecture supports ADK's OpenAPI tools
   - Can add `VertexAiSearchTool` for enhanced resource finding

5. ✅ **Gemini Integration**
   - All 4 agents powered by Gemini 2.0 Flash
   - Specialized system instructions per agent
   - ADK handles model configuration and invocation

### Code Quality

- **Uses Official ADK APIs** - Proper ADK patterns throughout
- **Comprehensive docstrings** - Every function documented
- **Type hints** - Throughout the codebase
- **Modular design** - Separation of concerns across 3 core modules
- **Configuration management** - Environment variables via `.env`

---

## 🚀 Setup Instructions

### Prerequisites

- Python 3.10 or higher
- Google API key (provided in `.env`)

### Installation

1. **Navigate to project directory:**
```bash
cd ~/google-adk-project
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

The `.env` file already contains your API key.

### Running the Application

**Interactive ADK Console:**
```bash
python adk_main.py
```

This launches ADK's built-in console runner with the MindfulAI coordinator agent.

### Project Structure (ADK Version)

```
google-adk-project/
├── adk_main.py            # Main entry point (ADK console runner)
├── adk_agents.py          # Multi-agent system using LlmAgent
├── adk_tools.py           # Custom tools as FunctionTool
├── adk_config.py          # Configuration
├── .env                   # API key (provided)
├── requirements.txt       # Dependencies (google-adk)
├── README_ADK.md         # This file
└── (legacy files)        # Original custom implementation
```

---

## 🎯 Competition Requirements Met

### Track Selection
✅ **Agents for Good (Healthcare)** - Mental health crisis support

### Key Concepts Implemented Using Official Google ADK

1. ✅ **Multi-Agent System**
   - **ADK `LlmAgent` with `sub_agents`** parameter
   - 4 specialized agents (Triage, Crisis, Support, Resource)
   - Sequential workflow orchestrated by ADK
   - Coordinator agent pattern

2. ✅ **Custom Tools**
   - **ADK `FunctionTool`** wrapping Python functions
   - 4 tools: crisis detection, mood tracking, resources, coping strategies
   - ADK automatically extracts function signatures
   - Tools assigned per-agent based on specialization

3. ✅ **Sessions & Memory**
   - **ADK `InMemorySessionService`** (built-in)
   - Session lifecycle managed by ADK
   - State preservation across conversation

4. ✅ **Built-in Tools (Extensible)**
   - Architecture supports ADK's `google_search` tool
   - Can integrate `VertexAiSearchTool`
   - OpenAPI tool support via ADK

5. ✅ **Gemini Integration**
   - All agents use Gemini 2.0 Flash via ADK
   - Specialized system instructions
   - ADK handles model invocation

---

## 💡 If I Had More Time

### ADK-Specific Enhancements

1. **ADK OpenAPI Tools**
   - Integrate therapy directory APIs
   - Mental health resource search APIs

2. **ADK MCP Tools**
   - Implement MCP server for memory management
   - Enable cross-application context sharing

3. **ADK Google Search Integration**
   - Real-time search for local therapists
   - Find nearby crisis centers

4. **ADK Long-Running Operations**
   - Implement pause/resume with ADK's resumability
   - Use ADK's LongRunningFunctionTool

5. **ADK Vertex AI Agent Engine Deployment**
   - Deploy to Vertex AI using ADK
   - Scale with Agent Engine

6. **ADK Agent Evaluation**
   - Use ADK's evaluation framework
   - Create eval sets for mental health scenarios

---

## ⚠️ Important Disclaimers

1. **Not a Replacement for Professional Help**: MindfulAI is a support tool.
2. **Emergency Situations**: Call 988 (US) or local emergency services.
3. **Demo Implementation**: Production deployment requires clinical validation.

---

## 📞 Crisis Resources (Always Available)

- **988 Suicide & Crisis Lifeline**: 988 or 1-800-273-8255 (24/7)
- **Crisis Text Line**: Text HOME to 741741
- **SAMHSA National Helpline**: 1-800-662-4357

---

**Built with Official Google ADK + Gemini 2.0 Flash**

**Remember: You are not alone. Help is available. Support is possible. Hope is real.** 💙

