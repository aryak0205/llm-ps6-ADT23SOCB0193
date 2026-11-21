# 📧 Email Reply Assistant (PS6)

> Generate professional email replies instantly using AI.

**LLM Mini Project · Problem Statement PS6 · Roll No. 6**

Paste any email you received and the app writes **three reply drafts** at once:

| Tone | Style |
|------|-------|
| 🧑‍💼 **Formal** | Professional, polite and respectful |
| 😊 **Friendly** | Warm, natural and conversational |
| ⚡ **Short** | Brief, clear and direct |

The app sends **one carefully designed prompt** to Google Gemini and asks for **structured JSON**, so it can show the three replies reliably.

---

## ✨ Features

- Large text area for pasting an email, plus 5 built-in sample emails
- **Generate Replies** button with a loading spinner
- Exactly three labelled reply cards (Formal, Friendly, Short)
- Separate **📋 Copy reply** button for each reply
- **🧹 Clear** button to reset the app
- Input validation (empty, too short, too long, non-text)
- Friendly error messages for an invalid key, quota limits, network problems and bad AI output
- Validates the AI's JSON before showing anything
- Prompt rules against invented facts or promises: it uses placeholders like `[Your Name]` instead
- API key kept in a `.env` file. It never appears in the code or the UI
- Responsive layout (cards stack on mobile)
- Sidebar guide for first-time users
- Automatic fallback to another Gemini Flash model if one is unavailable

## 🛠️ Technology Stack

| Component | Used for |
|-----------|----------|
| Python 3.10+ | Programming language |
| Streamlit | Web user interface |
| Google Gemini API (Flash model) | Large Language Model |
| Google GenAI Python SDK (`google-genai`) | Calling Gemini from Python |
| python-dotenv | Loading the API key from `.env` |
| JSON (structured output) | Reliable 3-reply response format |
| pytest | Automated tests (development only) |
| Git & GitHub | Source code hosting |

### About the model choice
The brief suggests **Gemini 2.5 Flash**. As of November 2026, Google's deprecations page lists `gemini-2.5-flash` as deprecated, with shutdown on 1 December 2026, and restricts it to users who used it before. New API keys may therefore get a "model not found" error.

The app uses this order:

1. `gemini-3.8-flash` (current Flash model, default)
2. `gemini-3.5-flash-lite`
3. `gemini-2.5-flash`

If one model is unavailable, the app tries the next one automatically. To force a model, add `GEMINI_MODEL=model-name` to `.env`. The card footer shows which model produced the replies.

## 📁 Project Structure

```
Email_Reply_Assistant/
├── app.py                  # Streamlit user interface (main file)
├── reply_engine.py         # Prompt, Gemini call, JSON validation (no UI code)
├── config.py               # Settings: models, limits, API key loading
├── requirements.txt        # Python packages
├── .env.example            # Template for your API key
├── .gitignore              # Keeps .env, venv and caches out of Git
├── .streamlit/config.toml  # App colour theme
├── README.md
├── SUBMISSION_CHECKLIST.md
├── github_link.txt         # Paste your repository URL here
├── assets/                 # Optional UI assets
├── screenshots/            # Put your real screenshots here
│   └── README.md
├── tests/
│   └── test_app.py         # Automated tests (fake Gemini, no key needed)
├── documentation/
│   ├── Procedure_Report.md
│   ├── Report.pdf / Report.docx
│   ├── Test_Cases.md
│   ├── Final_Prompt.md
│   └── Viva_Questions.md
└── sample_inputs/
    └── sample_emails.txt   # 5 realistic test emails
```

## ⚙️ Installation (Windows)

1. Install **Python 3.10 or newer** from https://www.python.org/downloads/. During setup, tick **"Add Python to PATH"**.
2. Unzip the project and open the folder in **Command Prompt** (or the VS Code terminal):
   ```bat
   cd path\to\Email_Reply_Assistant
   ```
3. Create and activate a virtual environment (recommended):
   ```bat
   python -m venv venv
   venv\Scripts\activate
   ```
   On PowerShell use `venv\Scripts\Activate.ps1`. If you get an execution-policy error, run `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` once.
4. Install the packages:
   ```bat
   pip install -r requirements.txt
   ```

macOS/Linux: use `python3 -m venv venv` and `source venv/bin/activate`.

## 🔑 API Key Setup

1. Go to **Google AI Studio**: https://aistudio.google.com/apikey and sign in.
2. Click **Create API key** and copy it.
3. In the project folder, copy the template:
   ```bat
   copy .env.example .env
   ```
4. Open `.env` in Notepad and replace the placeholder:
   ```
   GEMINI_API_KEY=paste_your_key_here
   ```
   No quotes and no spaces. Save the file.
5. **Never** share `.env` or upload it to GitHub. `.gitignore` already excludes it.

## ▶️ Run the App

```bat
streamlit run app.py
```

The browser opens at http://localhost:8501. If it doesn't open, copy that address into your browser. Press `Ctrl + C` in the terminal to stop the app.

After editing `.env`, stop and restart the app.

## 🧪 Run the Tests

The tests use a **fake** Gemini client, so they need no API key and no internet.

```bat
pip install pytest
python -m pytest -v
```

Manual test cases are in [`documentation/Test_Cases.md`](documentation/Test_Cases.md).

## 🧠 How It Works

1. You paste an email and click **Generate Replies**.
2. `validate_email_input()` checks the text (not empty, not too short or long).
3. `build_prompt()` puts the email inside `<email>` tags in one prompt that describes all three tones and the rules.
4. One `generate_content()` call is sent to Gemini with `response_mime_type="application/json"` and a JSON schema.
5. `parse_replies()` checks that the answer is valid JSON with non-empty `formal`, `friendly` and `short` strings.
6. Streamlit shows three cards, each with its own copy button.

The full prompt and how it was improved are in [`documentation/Final_Prompt.md`](documentation/Final_Prompt.md).

## 🖼️ Screenshots

Take your own screenshots by following [`screenshots/README.md`](screenshots/README.md), then add them here:

| Home screen | Generated replies |
|-------------|-------------------|
| ![Home](screenshots/01_home.png) | ![Replies](screenshots/03_replies.png) |

## ⚠️ Limitations

- Needs internet and a valid Gemini API key. The free tier has rate limits.
- AI replies can contain mistakes, so always read them before sending.
- The tool does not read your inbox or send emails. You copy and paste the reply.

## 🚀 Future Improvements

- Choose the reply length or extra tones (apologetic, persuasive)
- Regenerate a single reply
- Gmail/Outlook integration
- Reply history and downloads

## 👤 Author

| | |
|---|---|
| **Name** | `[Your Name]` |
| **Roll Number** | 6 |
| **Class** | `[Your Class / Section]` |
| **Problem Statement** | PS6 – Email Reply Assistant |
| **GitHub** | `[Paste repository URL]` |

*Built as an LLM mini project. No machine learning model was trained; the app uses the Gemini API.*
