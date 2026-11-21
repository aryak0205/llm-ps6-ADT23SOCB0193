"""
app.py - Streamlit user interface for the Email Reply Assistant (PS6).

Run with:
    streamlit run app.py

Flow:
    paste email -> click Generate Replies -> ONE prompt to Gemini
    -> JSON with 3 replies -> validated -> shown in 3 cards with copy buttons
"""

import html
import json

import streamlit as st
import streamlit.components.v1 as components

import config
from reply_engine import (
    REPLY_KEYS,
    REPLY_LABELS,
    ReplyAssistantError,
    generate_replies,
    load_sample_emails,
    validate_email_input,
)

# ---------------------------------------------------------------------------
# Page setup
# ---------------------------------------------------------------------------
st.set_page_config(page_title="Email Reply Assistant | PS6", page_icon="📧", layout="wide")

CARD_STYLE = {
    "formal": {"icon": "🧑‍💼", "color": "#2563eb", "hint": "Professional, polite and respectful"},
    "friendly": {"icon": "😊", "color": "#16a34a", "hint": "Warm, natural and conversational"},
    "short": {"icon": "⚡", "color": "#ea580c", "hint": "Brief, clear and direct"},
}

st.markdown(
    """
    <style>
    .block-container {padding-top: 2rem; max-width: 1200px;}
    .hero {
        background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 55%, #db2777 100%);
        border-radius: 18px; padding: 28px 32px; color: #ffffff; margin-bottom: 1.2rem;
        box-shadow: 0 10px 30px rgba(79, 70, 229, 0.25);
    }
    .hero h1 {color: #ffffff; margin: 0; font-size: 2.2rem;}
    .hero p {color: #eef2ff; margin: 6px 0 0 0; font-size: 1.1rem;}
    .reply-card {
        background: #ffffff; border: 1px solid #e5e7eb; border-radius: 14px;
        padding: 16px 18px; min-height: 220px; box-shadow: 0 4px 14px rgba(0,0,0,0.06);
    }
    .reply-card h3 {margin: 0 0 2px 0; font-size: 1.15rem; color: #111827;}
    .reply-hint {font-size: 0.85rem; color: #6b7280; margin-bottom: 10px;}
    .reply-text {white-space: pre-wrap; color: #1f2937; line-height: 1.55; font-size: 0.97rem;}
    .footer {text-align: center; color: #6b7280; font-size: 0.9rem; padding: 18px 0 6px 0;
             border-top: 1px solid #e5e7eb; margin-top: 2rem;}
    @media (max-width: 640px) { .hero h1 {font-size: 1.6rem;} .hero {padding: 20px;} }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------------------------------------
# Session state (remembers values between button clicks)
# ---------------------------------------------------------------------------
for name, default in (("email_input", ""), ("replies", None), ("model_used", None)):
    if name not in st.session_state:
        st.session_state[name] = default

SAMPLES = load_sample_emails()


def clear_all():
    """Clear button callback: empty the text area and remove old replies."""
    st.session_state.email_input = ""
    st.session_state.replies = None
    st.session_state.model_used = None


def load_selected_sample():
    """Copy the chosen sample email into the text area."""
    choice = st.session_state.get("sample_choice")
    if choice in SAMPLES:
        st.session_state.email_input = SAMPLES[choice]
        st.session_state.replies = None


def copy_button(text):
    """
    Show a small "Copy reply" button that copies `text` to the clipboard.
    Uses the modern Clipboard API with an older fallback for some browsers.
    """
    js_text = json.dumps(text).replace("</", "<\\/")  # safe inside <script>
    components.html(
        f"""
        <button id="copy" style="background:#4f46e5;color:#fff;border:none;border-radius:8px;
            padding:8px 16px;font-size:14px;cursor:pointer;font-family:sans-serif;">📋 Copy reply</button>
        <script>
        const text = {js_text};
        const btn = document.getElementById("copy");
        function done(ok) {{
            btn.innerText = ok ? "✅ Copied!" : "⚠️ Select the text and press Ctrl+C";
            setTimeout(() => btn.innerText = "📋 Copy reply", 2000);
        }}
        function fallback() {{
            const area = document.createElement("textarea");
            area.value = text; document.body.appendChild(area); area.select();
            let ok = false; try {{ ok = document.execCommand("copy"); }} catch (e) {{}}
            document.body.removeChild(area); done(ok);
        }}
        btn.addEventListener("click", () => {{
            if (navigator.clipboard && window.isSecureContext) {{
                navigator.clipboard.writeText(text).then(() => done(true)).catch(fallback);
            }} else {{ fallback(); }}
        }});
        </script>
        """,
        height=46,
    )


# ---------------------------------------------------------------------------
# Sidebar: help for first-time users
# ---------------------------------------------------------------------------
with st.sidebar:
    st.header("ℹ️ How to use")
    st.markdown(
        """
        1. **Paste** the email you received (or load a sample).
        2. Click **✨ Generate Replies**.
        3. Read the **Formal**, **Friendly** and **Short** drafts.
        4. Click **📋 Copy reply** on the one you like.
        5. Replace placeholders like **[Your Name]** before sending.
        """
    )
    st.divider()
    st.subheader("🔑 API key status")
    if config.get_api_key():
        st.success("Gemini API key found in .env")
    else:
        st.error("No API key found.\n\nCopy `.env.example` to `.env`, add your key, then restart.")
    st.caption("Your key stays on your computer. It is never shown in the app.")
    st.divider()
    st.caption("Tip: AI drafts can contain mistakes. Always read a reply before sending it.")

# ---------------------------------------------------------------------------
# Header
# ---------------------------------------------------------------------------
st.markdown(
    f"""<div class="hero"><h1>{html.escape(config.APP_TITLE)}</h1>
    <p>{html.escape(config.APP_SUBTITLE)}</p></div>""",
    unsafe_allow_html=True,
)

# ---------------------------------------------------------------------------
# Input section
# ---------------------------------------------------------------------------
if SAMPLES:
    sample_col, load_col = st.columns([4, 1], vertical_alignment="bottom")
    with sample_col:
        st.selectbox("Try a sample email (optional)", list(SAMPLES.keys()), key="sample_choice")
    with load_col:
        st.button("📥 Load sample", on_click=load_selected_sample)

st.text_area(
    "✉️ Paste the email you received",
    key="email_input",
    height=240,
    placeholder="Example:\nDear Student,\nThis is a reminder that your assignment is due on Friday...",
)
st.caption(f"{len(st.session_state.email_input.strip())} / {config.MAX_EMAIL_CHARS} characters")

gen_col, clear_col, _ = st.columns([2, 1, 3])
with gen_col:
    generate_clicked = st.button("✨ Generate Replies", type="primary")
with clear_col:
    st.button("🧹 Clear", on_click=clear_all)

# ---------------------------------------------------------------------------
# Generate replies (one API call)
# ---------------------------------------------------------------------------
if generate_clicked:
    is_valid, message = validate_email_input(st.session_state.email_input)
    if not is_valid:
        st.warning(message)
    else:
        with st.spinner("Writing your three replies... this usually takes a few seconds."):
            try:
                replies, model_used = generate_replies(st.session_state.email_input)
                st.session_state.replies = replies
                st.session_state.model_used = model_used
            except ReplyAssistantError as error:
                st.session_state.replies = None
                st.error(f"❌ {error}")
            except Exception:  # never show a raw stack trace to the user
                 st.session_state.replies = None
                 st.error(
                    f"❌ Unexpected error: {type(error).__name__}: {error}"
                 )
# ---------------------------------------------------------------------------
# Output section: three cards
# ---------------------------------------------------------------------------
if st.session_state.replies:
    st.subheader("📝 Your reply drafts")
    columns = st.columns(3, gap="medium")
    for column, key in zip(columns, REPLY_KEYS):
        style = CARD_STYLE[key]
        reply_text = st.session_state.replies[key]
        with column:
            st.markdown(
                f"""<div class="reply-card" style="border-top: 5px solid {style['color']};">
                <h3>{style['icon']} {REPLY_LABELS[key]}</h3>
                <div class="reply-hint">{style['hint']}</div>
                <div class="reply-text">{html.escape(reply_text)}</div></div>""",
                unsafe_allow_html=True,
            )
            copy_button(reply_text)
    st.caption(f"Generated with model: {st.session_state.model_used}. Review and edit before sending.")
else:
    st.info("👆 Paste an email above and click **Generate Replies** to see three drafts here.")

st.markdown(f'<div class="footer">{html.escape(config.FOOTER_TEXT)}</div>', unsafe_allow_html=True)
