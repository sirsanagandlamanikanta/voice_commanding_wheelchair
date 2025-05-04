# 🗣️ Voice Command Recognition with Python

This Python script listens to your voice through the microphone, converts it to text using Google's Speech Recognition API, and responds with voice using a text-to-speech engine. It's a simple demo of voice-command-based interaction.

---

## 🎯 Features

- Continuous listening via microphone
- Converts voice to text using Google Speech Recognition
- Responds using voice via `pyttsx3`
- Recognizes simple commands like:
  - `hello` or `hallo`
  - `turn left`, `turn right`
  - `move`, `stop`
  - `exit` (to quit the program)

---

## 🛠️ Requirements

Install the required libraries using pip:

```bash
pip install SpeechRecognition pyttsx3 pyaudio
