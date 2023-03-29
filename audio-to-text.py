import whisper

file = "130.mp3"
model = whisper.load_model("tiny")
result = model.transcribe(file)
with open('transcription '+file+'.txt', 'w') as f:
    f.write(result["text"])