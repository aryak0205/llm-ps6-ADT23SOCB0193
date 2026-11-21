# Viva Questions & Answers – Email Reply Assistant (PS6)

Short answers you can explain in your own words.

### Basics

**1. What is an LLM?**
A Large Language Model is an AI model trained on huge amounts of text. It predicts the next words, so it can understand and write human-like text. Examples: Gemini, GPT, Claude, Llama.

**2. What is Generative AI?**
AI that *creates* new content, such as text, images, audio or code, instead of only classifying or predicting labels. My project generates new email replies.

**3. What is prompt engineering?**
Designing the instructions (the prompt) given to an LLM so it produces the output we want: correct tone, no invented facts and the right format.

**4. What is Gemini?**
Google's family of LLMs. I used a Gemini **Flash** model through the Gemini API because it is fast, cheap and has a free tier.

**5. What is an API?**
An Application Programming Interface lets one program talk to another. My app sends the prompt to Google's servers through the Gemini API and receives the reply.

**6. What is Streamlit?**
A Python library for building web apps with plain Python, with no HTML or JavaScript needed. I used it for the text area, buttons, spinner and reply cards.

**7. What is JSON?**
JavaScript Object Notation, a simple text format for data made of key–value pairs, e.g. `{"formal": "...", "friendly": "...", "short": "..."}`. Python's `json` module converts it into a dictionary.

**8. What is an SDK?**
A Software Development Kit is a ready-made library for using a service. I used the `google-genai` Python SDK, so I call `client.models.generate_content()` instead of writing raw HTTP requests.

### About my project

**9. How does the application work?**
The user pastes an email → the app validates it → one prompt is built with the email inside `<email>` tags → one API call goes to Gemini in JSON mode → the JSON is checked → three cards are shown with copy buttons.

**10. Why are three different tone instructions used?**
Different situations need different replies: formal for teachers, recruiters or clients, friendly for known people, short for quick acknowledgements. Each tone has its own clear instruction, so the three drafts are really different and the user can pick one.

**11. Why one prompt and not three API calls?**
The problem statement asks for one prompt. It is also 3× fewer requests, so it is faster, cheaper and uses less quota. And the model keeps all three replies consistent but distinct.

**12. Why do you ask for JSON output?**
Free text can come in different formats each time. JSON with fixed keys lets the code reliably split the answer into three cards. I also turn on Gemini's JSON mode and pass a schema.

**13. How do you validate the LLM response?**
`parse_replies()` removes any code fences, parses the JSON, and checks that `formal`, `friendly` and `short` all exist and are non-empty strings. Otherwise it shows a friendly error instead of crashing.

**14. How do you stop the AI from inventing facts?**
The prompt says not to invent dates, names, numbers or promises, and to use placeholders like `[Your Name]` or `[your available time]` for unknown details. Temperature is kept moderate (0.6).

**15. How is the API key secured?**
It is stored in a `.env` file and loaded with `python-dotenv`. It is never written in the code or shown in the UI. `.env` is listed in `.gitignore`, so it is not uploaded to GitHub. Only `.env.example` with a placeholder is shared.

**16. What input validation is done?**
Empty or spaces-only input, input under 15 characters, input over 6000 characters, and input with no letters are all rejected with a message. No API call is made for invalid input.

**17. What errors does the app handle?**
A missing or invalid API key, quota or rate limits (429), server busy (503), network problems, an unavailable model (the app tries the next model) and invalid JSON output.

**18. What is prompt injection, and how did you handle it?**
When text inside the input tries to give the AI new instructions (e.g. "ignore all rules"). I put the email inside `<email>` tags and told the model to treat it only as content to reply to.

**19. What is temperature?**
A setting that controls randomness. Low gives predictable answers; high gives creative but riskier ones. I used 0.6 so the replies sound natural without being made up.

**20. Did you train a model?**
No. I used a pre-trained LLM through an API. The work was in prompt design, app logic, validation and the interface.

**21. Why did you not use Gemini 2.5 Flash?**
The brief suggested it, but in November 2026 Google lists it as deprecated and only available to older users. So the app uses `gemini-3.8-flash` by default and falls back to other Flash models automatically. The model can be changed in `.env`.

**22. How did you test the project?**
Automated pytest tests with a fake Gemini client check validation, parsing, error handling and the single API call. Manual test cases in `Test_Cases.md` check the real app with five sample emails.

### Limitations & future

**23. What are the limitations?**
It needs internet and an API key, and the free tier has limits. AI can still make mistakes, so the user must review the reply. It does not connect to Gmail and cannot send emails. Privacy: email text is sent to Google's API.

**24. What is the future scope?**
Gmail/Outlook integration, more tones (apologetic, persuasive), choice of reply length, regenerating one reply, reply history, multi-language selection and deploying online (Streamlit Community Cloud).

**25. What did you learn?**
How LLM APIs work, prompt engineering, structured JSON outputs, building UIs with Streamlit, handling errors and keeping secrets safe with `.env` and `.gitignore`.
