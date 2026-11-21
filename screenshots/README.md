# Screenshots – how to capture them

This folder is empty on purpose. Screenshots must come from **your own running app**, not mock-ups.

## Steps (Windows)
1. Run the app: `streamlit run app.py` (the browser opens at http://localhost:8501).
2. Zoom the browser to 90–100% and maximise the window.
3. Press **Win + Shift + S**, select the area, then paste into **Paint** and save as PNG in this folder. (Or press **PrtScn** and paste into Paint.)
4. Use these file names so the main README shows them automatically:

| File name | What to capture |
|-----------|-----------------|
| `01_home.png` | The app on first load: title, sidebar guide, empty text area |
| `02_email_pasted.png` | A sample email loaded in the text area |
| `03_replies.png` | The three reply cards (Formal, Friendly, Short) after generating |
| `04_copied.png` | A copy button showing "✅ Copied!" |
| `05_validation_error.png` | The warning after clicking Generate with an empty box |
| `06_tests_passed.png` | Terminal output of `python -m pytest -v` |
| `07_mobile_view.png` *(optional)* | Narrow window, with cards stacked |

## Before saving, check that…
- ❌ Your API key is **not visible** anywhere (don't screenshot the `.env` file).
- ✅ The footer "LLM Mini Project | PS6 | Roll No. 6" is visible in at least one image.
- ✅ The text is readable (no tiny full-screen captures of a 4K monitor).
