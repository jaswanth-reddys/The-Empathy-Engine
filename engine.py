import pyttsx3
from textblob import TextBlob
import os
import uuid

class EmpathyEngine:
    def __init__(self):
        self.output_dir = "static/audio"
        os.makedirs(self.output_dir, exist_ok=True)

    def analyze_emotion(self, text):
        blob = TextBlob(text)
        pol = blob.sentiment.polarity
        subj = blob.sentiment.subjectivity
        
        if pol > 0.2:
            if subj > 0.5:
                return "Excited", pol
            return "Happy", pol
        elif pol < -0.2:
            if subj > 0.5:
                return "Angry/Outraged", pol
            return "Frustrated", pol
        elif "?" in text:
            return "Inquisitive", pol
        else:
            return "Neutral", pol

    def generate_audio(self, text):
        emotion, intensity = self.analyze_emotion(text)
        abs_int = abs(intensity)
        
        engine = pyttsx3.init()
        
        # Base settings
        rate = 175
        volume = 0.8
        
        # Advanced Modulation Mapping
        if emotion == "Excited":
            rate = 180 + (60 * abs_int)  # Very fast
            volume = 0.9 + (0.1 * abs_int) # Very loud
        elif emotion == "Happy":
            rate = 175 + (40 * abs_int)  # Slightly fast
            volume = 0.8 + (0.1 * abs_int) # Moderate volume
        elif emotion == "Angry/Outraged":
            rate = 150 - (20 * abs_int)  # Slow and deliberate
            volume = 1.0                # Max volume
        elif emotion == "Frustrated":
            rate = 160 - (20 * abs_int)  # Slower
            volume = 0.85 + (0.05 * abs_int) # Slightly firm
        elif emotion == "Inquisitive":
            rate = 170                  # Slightly slower for clarity
            volume = 0.75
        else:
            rate = 175
            volume = 0.7                # Calm neutral
            
        engine.setProperty('rate', int(rate))
        engine.setProperty('volume', volume)
        
        filename = f"{uuid.uuid4()}.mp3"
        filepath = os.path.join(self.output_dir, filename)
        
        # Note: pyttsx3 save_to_file is asynchronous in some environments, 
        # but usually synchronous on Windows.
        engine.save_to_file(text, filepath)
        engine.runAndWait()
        
        # Return relative path for web serving
        return f"/static/audio/{filename}", emotion, intensity

if __name__ == "__main__":
    engine = EmpathyEngine()
    test_texts = [
        "I am so incredibly happy today, everything is wonderful!",
        "I am very frustrated and angry with this service.",
        "The weather is okay today."
    ]
    for t in test_texts:
        path, emotion, intensity = engine.generate_audio(t)
        print(f"Text: {t}\nEmotion: {emotion} ({intensity:.2f})\nAudio: {path}\n")
