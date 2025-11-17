"""
Configuration for MindfulAI using Google ADK.
Sets up API keys and system-wide settings.
"""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API Configuration
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY", "XXXXXXXXXXX")

# Set environment variable for ADK
os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY

# Agent Model Configuration
DEFAULT_MODEL = "gemini-2.0-flash-exp"

# Crisis Keywords - Used by custom crisis detection tool
CRISIS_KEYWORDS = [
    "suicide",
    "kill myself",
    "end it all",
    "want to die",
    "no reason to live",
    "better off dead",
    "self-harm",
    "hurt myself",
    "can't go on",
    "no hope",
    "overdose",
    "end my life",
    "goodbye cruel world",
]

SEVERE_KEYWORDS = [
    "plan to",
    "going to",
    "tonight",
    "right now",
    "have the",
    "pills",
    "gun",
    "jump off",
    "step in front",
]

# Mental Health Resources
CRISIS_RESOURCES = {
    "us": {
        "988 Suicide & Crisis Lifeline": "988 or 1-800-273-8255 (24/7)",
        "Crisis Text Line": "Text HOME to 741741",
        "SAMHSA National Helpline": "1-800-662-4357",
        "Trevor Project (LGBTQ+ Youth)": "1-866-488-7386",
        "Veterans Crisis Line": "988 then press 1",
    },
    "international": {
        "International Association for Suicide Prevention": "https://www.iasp.info/resources/Crisis_Centres/",
        "Befrienders Worldwide": "https://www.befrienders.org/",
    },
}
