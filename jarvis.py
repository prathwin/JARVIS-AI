import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import requests

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice', voices[0].id)

API_KEY = "your_openweathermap_api_key"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good morning mam! Have a good day.")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon mam! Hope you are productive today.")
    else:
        speak("Good evening mam! How was your day?")
        speak("I am Jarvis, please tell me how I can help you.")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source, 0, 4)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")
    except Exception:
        print("Say that again please...")
        return "None"
    return query

def getWeather(city):
    complete_url = f"{BASE_URL}q={city}&appid={API_KEY}&units=metric"
    response = requests.get(complete_url)
    data = response.json()

    if data["cod"] != "404":
        main = data["main"]
        weather = data["weather"][0]
        description = weather["description"]
        temp = main["temp"]
        pressure = main["pressure"]
        humidity = main["humidity"]

        weather_report = f"The temperature in {city} is {temp}°C with {description}. The pressure is {pressure} hPa and the humidity is {humidity}%."
        return weather_report
    else:
        return "City not found."

def openSettings():
    speak("Opening system settings...")
    os.system("start ms-settings:")

def playSpotify(query):
    speak(f"Searching for {query} on Spotify...")
    query = query.replace("play", "").strip()
    webbrowser.open(f"https://open.spotify.com/search/{query}")

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'search youtube' in query:
            query = query.replace("search youtube", "")
            speak(f"Searching YouTube for {query}")
            webbrowser.open(f"https://www.youtube.com/results?search_query={query}")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'search google' in query:
            query = query.replace("search google", "")
            speak(f"Searching Google for {query}")
            webbrowser.open(f"https://www.google.com/search?q={query}")

        elif 'open gmail' in query:
            webbrowser.open("https://gmail.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\LENOVO\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'open image' in query:
            imagePath = ""
            os.startfile(imagePath)

        elif 'open settings' in query:
            openSettings()

        elif 'open block' in query:
            blockPath = "C:\\Program Files\\CodeBlocks\\codeblocks.exe"
            os.startfile(blockPath)

        elif 'play' in query and 'spotify' in query:
            playSpotify(query)

        elif 'who are you' in query:
            speak("I am Jarvis, your personal assistant.")

        elif 'what is your name' in query:
            speak("I am Jarvis, sir! You created me!")

        elif 'hey' in query:
            speak("Hello, sir! What's up!")

        elif 'don’t you get bored of me' in query:
            speak("No mam, you created me... How can I get bored of you? That would be unethical! I am always here to assist you in every possible way.")

        elif 'who is my friend' in query:
            speak("Your friend is Prathwin!")

        elif 'when is my birthday' in query:
            speak("You are a precious gift of God born on December 24rd, 2003!")

        elif 'my day was bad' in query:
            speak("Honey, don’t worry! Your smile made many of them happy today...")

        elif 'who do I love the most' in query:
            speak("Your mom, she is your motivation.")

        elif 'do I have siblings' in query:
            speak("Yeah... the annoying girl, Mohitha.")

        elif 'who is my best friend' in query:
            speak("Jithesh!")

        elif 'what do I love to do' in query:
            speak("You love to read books and be delusional with your book boyfriends, especially that Meadows made you go crazy.")

        elif 'which music do I listen to often' in query:
            speak("Anuv Jain, 'Husn' is one of your favorites among all his creations.")

        elif 'good morning' in query:
            speak("Have a good day, sir!")

        elif 'good night' in query:
            speak("How was your day?")

        elif 'the day was not bad' in query:
            speak("It's okay, sir, you did well today.")

        elif 'the day was very nice' in query:
            speak("Wow, you seem very happy today! Glad to hear that.")

        elif 'the day was very bad' in query:
            speak("Don't worry, sir, you can do better tomorrow!")

        elif 'exit' in query or 'bye' in query or 'stop' in query or 'quit' in query:
            speak("Take care, sir, see you later!")
            break
