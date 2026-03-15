# The Empathy Engine ️

The Empathy Engine is a Text-to-Speech (TTS) service that dynamically modulates vocal characteristics based on the detected emotion of the input text. It aims to bridge the "uncanny valley" by adding emotional resonance to synthetic voices.

## Features
- **Dynamic Emotion Detection**: Analyzes input text for sentiment (polarity) and subjectivity using TextBlob.
- **Vocal Parameter Modulation**: Programmatically adjusts **Speech Rate** and **Volume** based on the detected emotion.
- **Granular Emotions**: Categorizes text into *Excited*, *Happy*, *Angry/Outraged*, *Frustrated*, *Inquisitive*, or *Neutral*.
- **Intensity Scaling**: The degree of vocal modulation scales with the intensity of the detected sentiment.
- **Web Interface**: A FastAPI-powered web UI for real-time testing and audio playback.

## Emotion-to-Voice Mapping Logic

Our engine uses a multi-dimensional mapping strategy:

| Emotion | Rate (WPM) | Volume | Context |
| :--- | :--- | :--- | :--- |
| **Excited** | Fast (180+) | High (0.9+) | High polarity + High subjectivity |
| **Happy** | Moderately Fast | Moderate | High polarity + Low subjectivity |
| **Angry** | Slow/Deliberate | Max (1.0) | Low polarity + High subjectivity |
| **Frustrated** | Slower | Moderate High | Low polarity + Low subjectivity |
| **Inquisitive** | Slightly Slow | Moderate Low | Presence of a question mark |
| **Neutral** | Standard (175) | Calm (0.7) | Near-zero polarity |

**Intensity Scaling**: For emotions like *Excited* or *Frustrated*, the `abs(polarity)` acts as a multiplier, further increasing or decreasing the rate and volume to match the strength of the sentiment.

## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone <repo-url>
   cd empathy-engine
   ```

2. **Install Dependencies**:
   Ensure you have Python 3.8+ installed.
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**:
   ```bash
   python main.py
   ```
   The application will start at `http://127.0.0.1:8000`.

4. **Access the Web UI**:
   Open your browser and navigate to `http://127.0.0.1:8000` to interact with the Empathy Engine.

## Technical Stack
- **Backend**: FastAPI (Python)
- **Sentiment Analysis**: TextBlob
- **TTS Engine**: pyttsx3 (Offline, SAPI5/NSSpeechSynthesizer)
- **Frontend**: Jinja2 Templates + CSS
