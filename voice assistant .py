import pyttsx3
import speech_recognition as sr
import openai

# Set your OpenAI API key
openai.api_key = 'Aya you can put your here openai Api'        
def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
        query = r.recognize_google(audio, language="en-in")
        return query

def get_openai_response(query):
    # Use the OpenAI API to get a response
    response = openai.Completion.create(
        engine="text-davinci-002",  # You can change the engine based on your preference
        prompt=query,
        max_tokens=50
    )
    return response.choices[0].text.strip()

if __name__ == "__main__":
    say("hi I am the personal voice assistant of nagy")
    
    while True:
        print("listening----")
        text = takecommand()
        
        # Get response from OpenAI
        openai_response = get_openai_response(text)
        
        # Say the response
        say(openai_response)



 
 



        
