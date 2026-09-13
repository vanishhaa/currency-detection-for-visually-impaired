import pyttsx3
# Initialize the text-to-speech engine (uses the default driver )
engine = pyttsx3.init()
# Get the list of available voices installed on the system
voices = engine.getProperty('voices')
print(f"Found {len(voices)} voice(s)")
for v in voices:
    print(v.id)
engine.setProperty('rate', 150)
# Queue up text to be spoken
engine.say("Testing one two three")
# Actually speak the queued text; this call blocks until speech finishes
engine.runAndWait()