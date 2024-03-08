import time
import pyttsx3


# def readOut(text, choice = 0, language = 'english'):
def readOut(text, choice = 0):
    if choice not in [0, 1]:
        choice = 0
    # if language not in ['en','hi']:
    #     language = 'english'

    # Initialize the Pyttsx3 engine
    engine = pyttsx3.init()

    # Set properties
    # engine.setProperty('voice', language) 
    engine.setProperty('rate', 130)    # Speed of speech
    engine.setProperty('volume', 1)  # Volume (0.0 to 1.0)

    ## Get a list of available voices
    voices = engine.getProperty('voices')

    # # Print available voices
    # for voice in voices:
    #     print("ID:", voice.id, "Name:", voice.name, "Lang:", voice.languages)

    # Set the voice (change index to select a different voice)
    engine.setProperty('voice', voices[choice].id)

    # text = "नमस्ते, यह एक उदाहरण है."
    # Speak the text
    engine.say(text)

    # Wait for speech to finish
    engine.runAndWait()


if __name__ == '__main__':
    user_wish = True
    while user_wish:

        try:
            #which language you prefer, en - english, hi - hindi
            # language = input("press En for English, hi for hindi: ")
            #voice to say
            voice = int(input("Press 0 for Male, 1 for Female: "))
            if voice not in [0, 1]:
                print("pressing any other number default to 0")
                
            # text to read
            text = input("Enter the text to read: ")

            # readOut(text, voice, language)
            readOut(text, voice)
            
            # waiting time
            time.sleep(5)        
            user_choice = input("Enter any words to continue...")
            if len(user_choice) == 0:
                user_wish = False
        except Exception as e:
            print("Try again differently.", e)
        
    print("thank you for trying.")



""" prerequirements: pip install pyttsx3 """