import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
print(f"Found {len(voices)} voice(s)")
for v in voices:
    print(v.id)
engine.setProperty('rate', 150)
engine.say("Testing one two three")
engine.runAndWait()
