import pyttsx3


def speak(text):
    # Initialize the TTS engine
    engine = pyttsx3.init()

    # Set properties (optional)
    engine.setProperty('rate', 150)  # Speed of speech
    engine.setProperty('volume', 0.9)  # Volume (0.0 to 1.0)

    # Speak the text
    engine.say(text)

    # Wait for speech to finish
    engine.runAndWait()


if __name__ == "__main__":
    while True:
      x = input("Enter text for the robospeaker: ")
      if x =="q":
       break
      speak(x)
