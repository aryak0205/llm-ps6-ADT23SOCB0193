# Submission Checklist – PS6 Email Reply Assistant (Roll No. 6)

⏰ **Deadline: 22 November 2026, before 11:30 AM.** Aim to finish by 10:30 AM to leave buffer time.

## 1. Personal details (≈10 min)
- [ ] Replace `[Your Name]`, `[Your Class / Section]` in `README.md` (Author section)
- [ ] Fill the same placeholders in `documentation/Report.docx` (yellow highlighted fields), then export a new `Report.pdf` (see step 6)
- [ ] Fill the header of `documentation/Test_Cases.md`

## 2. Run the app (≈15 min)
- [ ] `pip install -r requirements.txt` worked
- [ ] Created `.env` from `.env.example` with **your** key
- [ ] `streamlit run app.py` opens at http://localhost:8501
- [ ] Generated replies for all 5 samples
- [ ] Copy button and Clear button work

## 3. Test (≈20 min)
- [ ] `pip install pytest` then `python -m pytest -v` and note the result
- [ ] Filled **Actual result** + **Pass/Fail** in `documentation/Test_Cases.md` Part A (only for tests you actually ran)
- [ ] Copied one real AI reply into the report's "Sample output" box

## 4. Screenshots (≈10 min)
- [ ] Saved images in `screenshots/` using the names in `screenshots/README.md`
- [ ] No API key is visible in any screenshot

## 5. GitHub (≈15 min)
- [ ] Created the repository (steps below) and uploaded the files
- [ ] **`.env` is NOT in the repository** (check the file list on github.com)
- [ ] Pasted the URL into `github_link.txt`, `README.md` and the report

### How to upload (no Git commands needed)
1. Sign in at https://github.com → **+** (top right) → **New repository**.
2. Name: `Email_Reply_Assistant`, set it to **Public**, and do **not** tick "Add a README". Click **Create repository**.
3. Click **"uploading an existing file"**.
4. Open the project folder in File Explorer, select everything **except** `.env` and `venv`, and drag it into the page. (Hidden files: in File Explorer → View → Show → Hidden items, so `.gitignore`, `.env.example` and `.streamlit` are visible.)
5. Commit message: `Initial commit - PS6 Email Reply Assistant` → **Commit changes**.
6. Copy the URL from the address bar (e.g. `https://github.com/yourname/Email_Reply_Assistant`).

### Or with Git (if installed)
```bat
git init
git add .
git status            :: make sure .env is NOT listed
git commit -m "Initial commit - PS6 Email Reply Assistant"
git branch -M main
git remote add origin https://github.com/<your-username>/Email_Reply_Assistant.git
git push -u origin main
```

## 6. Final report
- [ ] Open `Report.docx` in Word → fill fields → **File → Save As → PDF** → name it `Report.pdf`
- [ ] Check that the PDF is still **exactly 2 pages** (if it grows, shorten the sample output text)

## 7. Re-create the ZIP
- [ ] Delete `venv`, `__pycache__`, `.pytest_cache` and **`.env`** from the folder copy
- [ ] Right-click the `Email_Reply_Assistant` folder → **Send to → Compressed (zipped) folder** → rename to `Email_Reply_Assistant_PS6.zip`

## 8. Google Drive submission
1. Go to https://drive.google.com → **New → Folder** → name it `PS6_RollNo6_Email_Reply_Assistant`.
2. Upload `Email_Reply_Assistant_PS6.zip`, `Report.pdf`, `Report.docx` (and `github_link.txt` if asked).
3. Right-click the folder → **Share** → under General access choose **"Anyone with the link – Viewer"** (or whatever your teacher asked for) → **Copy link**.
4. Submit the link through your college's form/classroom **before 11:30 AM**. Open the link in an incognito window to check it works.

## Final safety check
- [ ] No real API key in any file (`python -m pytest` includes a key-scan test)
- [ ] ZIP contains: app.py, reply_engine.py, config.py, requirements.txt, .env.example, .gitignore, README.md, tests/, documentation/, sample_inputs/, screenshots/, SUBMISSION_CHECKLIST.md, github_link.txt
