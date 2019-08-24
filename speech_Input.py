import random
import time

import speech_recognition as sr
import classify
import fake

def recognize_speech_from_mic(recognizer, microphone):

    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    response = {
        "success": True,
        "error": None,
        "transcription": None
    }

    try:
        response["transcription"] = recognizer.recognize_google(audio)
    except sr.RequestError:
        response["success"] = False
        response["error"] = "API unavailable"
    except sr.UnknownValueError:
        response["error"] = "Unable to recognize speech"

    return response


if __name__ == "__main__":
    NUM_GUESSES = 3
    PROMPT_LIMIT = 5
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()
    print("speak now!")
    time.sleep(3)

    for i in range(NUM_GUESSES):
        for j in range(PROMPT_LIMIT):
            guess = recognize_speech_from_mic(recognizer, microphone)
            if guess["transcription"]:
                break
            if not guess["success"]:
                break
            print("I didn't catch that. What did you say?\n")

        
        if guess["error"]:
            print("ERROR: {}".format(guess["error"]))
            break

        
        print("You said: {}".format(guess["transcription"]))

        
        guessed = guess["transcription"].lower() 
        user_has_more_attempts = i < NUM_GUESSES - 1

        
        if guessed='classify':
            classify.main()
            break
        elif guessed='check':
             fake.main()
             break
        else:
            print("Incorrect. Try again.\n")
            break
