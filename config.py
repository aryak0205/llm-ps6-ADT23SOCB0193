"""
config.py - Central configuration for the Email Reply Assistant (PS6).

All settings live here so they are easy to find and change.
The API key is NEVER written in code. It is read from the .env file
(or from an environment variable) at runtime.
"""

import os

from dotenv import load_dotenv

# Load variables from a local .env file (if it exists) into the environment.
load_dotenv()

# ---------------------------------------------------------------------------
# App information
# ---------------------------------------------------------------------------
APP_TITLE = "📧 Email Reply Assistant"
APP_SUBTITLE = "Generate professional email replies instantly using AI."
FOOTER_TEXT = "LLM Mini Project | PS6 | Roll No. 6"

# ---------------------------------------------------------------------------
# Model settings
# ---------------------------------------------------------------------------
# The problem statement suggests Gemini 2.5 Flash. In November 2026 Google
# lists gemini-2.5-flash as deprecated (shutdown 1 Dec 2026) and limits it to
# users who already used it, so new API keys may get a "model not found"
# error. We therefore use a current Flash model by default and try the
# others in order if one is unavailable for your key.
#
# You can force a specific model by adding GEMINI_MODEL=... to your .env file.
DEFAULT_MODELS = [
    "gemini-3.8-flash",       # current Flash model (first choice)
    "gemini-3.5-flash-lite",  # lighter, cheaper Flash-Lite model
    "gemini-2.5-flash",       # model named in the brief (may be unavailable)
]

_custom_model = os.getenv("GEMINI_MODEL", "").strip()
MODEL_CANDIDATES = [_custom_model] + DEFAULT_MODELS if _custom_model else DEFAULT_MODELS
# Remove duplicates while keeping order.
MODEL_CANDIDATES = list(dict.fromkeys(MODEL_CANDIDATES))

# A little creativity makes replies sound natural; too much invents things.
TEMPERATURE = 0.6

# ---------------------------------------------------------------------------
# Input limits (used for validation)
# ---------------------------------------------------------------------------
MIN_EMAIL_CHARS = 15      # shorter than this is probably not a real email
MAX_EMAIL_CHARS = 6000    # keeps requests fast and within free-tier limits

# ---------------------------------------------------------------------------
# File locations
# ---------------------------------------------------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SAMPLE_EMAILS_PATH = os.path.join(BASE_DIR, "sample_inputs", "sample_emails.txt")


def get_api_key() -> str:
    """Return the Gemini API key from the environment, or '' if missing."""
    key = os.getenv("GEMINI_API_KEY", "").strip()
    # Treat the placeholder from .env.example as "not set".
    if key in ("", "your_api_key_here"):
        return ""
    return key
