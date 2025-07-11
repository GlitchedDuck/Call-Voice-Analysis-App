# Call-Voice-Analysis-App

This tool lets small businesses transcribe and analyse voicemails or call recordings using open-source tools like `ffmpeg` and `whisper.cpp`. It simulates GPT-style analysis to extract insights like urgency, customer intent, and contact info.

---

## 💻 How to Run the Tool

### 1. Install Python 3.8+

### 2. Install dependencies:

- `ffmpeg`
- `whisper.cpp` compiled as `main`
- Place `ggml-base.en.bin` in a `models/` folder

### 3. Run in terminal:

```
python voice_analysis_app.py
```

### 4. Output:

- `transcript.txt` – the full transcription of the audio file
- `analysis.txt` – a summary of the customer's intent, urgency, and next steps

---

## ❗ Licensing

This project is **proprietary software**.  
You are not permitted to use, copy, distribute, or modify any part of this code without explicit written permission from the author.

See the [LICENSE](./LICENSE) file for full terms.
