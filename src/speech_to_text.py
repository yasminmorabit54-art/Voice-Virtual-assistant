from RealtimeSTT import AudioToTextRecorder

recorder = AudioToTextRecorder(
    model="tiny.en",
    language="en",
    spinner=False
)

def listen():
    print("You:", end="", flush=True)
    text = recorder.text()
    print(text)
    return text
