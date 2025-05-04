import speech_recognition as sr
import pyttsx3

# Initialize the recognizer
r = sr.Recognizer()

# Initialize the text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    """Convert text to speech"""
    engine.say(text)
    engine.runAndWait()

print("You can say 'exit' to stop the program.")

try:
    while True:  # Keep the program running in a loop
        with sr.Microphone() as source:
            print("Listening...")
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)

        try:
            text = r.recognize_google(audio).lower()
            print(f"You said: {text}")

            # Respond and check for exit command
            if "exit" in text:
                response = "Goodbye! Exiting the program."
                print(response)
                speak(response)
                break  # Exit the loop
            elif "hallo" in text or "hello" in text:
                response = "Hallo, how can I help you?"
                print(response)
                speak(response)
            elif "turn left" in text:
                response = "turn left"
                print(response)
                speak(response)
            elif "turn right" in text:
                response = "turn right"
                print(response)
                speak(response)
            elif "stop" in text:
                response = "ok stop"
                print(response)
                speak(response)
            elif "move" in text:
                response = "ok moveing"
                print(response)
                speak(response)
            else:
                response = "I didn't understand that. Please try again!"
                print(response)
                speak(response)

        except sr.UnknownValueError:
            response = "Could not understand audio. Please speak clearly."
            print(response)
            speak(response)
        except sr.RequestError as e:
            response = f"Could not request results from Google Speech Recognition service; {e}"
            print(response)
            speak(response)

except KeyboardInterrupt:
    print("Program interrupted by user.")
except Exception as e:
    response = f"An unexpected error occurred: {e}"
    print(response)
    speak(response)
