import whisper

model = whisper.load_model("tiny")
result = model.transcribe("120.mp3")
with open('transcription.txt', 'w') as f:
   for i in result:
      f.write(result["text"])
