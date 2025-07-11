
import os
import tempfile
import subprocess
import json

# --- CONFIG ---
def analyse_transcript(transcript):
    prompt = f"""
    Transcript:
    \"{transcript}\"

    Please analyse the transcript and return:
    - A 1-sentence summary
    - Customer's intent
    - Urgency level (Low / Medium / High)
    - Recommended actions
    - Any contact information
    - Suggested tags
    """

    # Placeholder for actual OpenAI call, print simulated analysis
    print("\nGPT Analysis (simulated):\n")
    return """
    - Summary: Simulated summary of the customer message.
    - Intent: Simulated intent.
    - Urgency: Medium
    - Actions: Follow up via phone.
    - Contact: Simulated phone number.
    - Tags: simulated, test
    """

def transcribe_audio_with_ffmpeg_and_whisper_cpp(file_path):
    print("Transcribing using Whisper.cpp fallback...")
    wav_file = file_path.replace(".mp3", ".wav").replace(".m4a", ".wav")
    subprocess.run(["ffmpeg", "-i", file_path, wav_file, "-y"])

    result_file = "result.json"
    subprocess.run(["main", "-m", "models/ggml-base.en.bin", "-f", wav_file, "-otxt", "-oj", "--output", "result"])

    with open(result_file, "r") as f:
        result_json = json.load(f)
    return result_json.get("text", "")

def process_audio_file(file_path):
    print("Transcribing audio...")
    transcript = transcribe_audio_with_ffmpeg_and_whisper_cpp(file_path)
    print("\nTranscript:\n", transcript)

    print("\nAnalysing transcript...")
    analysis = analyse_transcript(transcript)
    print("\nAnalysis:\n", analysis)

    with open("transcript.txt", "w") as f:
        f.write(transcript)

    with open("analysis.txt", "w") as f:
        f.write(analysis)

    print("\nTranscript and analysis saved as 'transcript.txt' and 'analysis.txt'")

if __name__ == "__main__":
    input_path = input("Enter path to audio file (mp3, wav, m4a): ").strip()

    if os.path.exists(input_path):
        process_audio_file(input_path)
    else:
        print("File not found. Please check the path and try again.")
