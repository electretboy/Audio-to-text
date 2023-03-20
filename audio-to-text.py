import whisper
import tkinter as tk
from tkinter import filedialog

def browse_file():
    file_path = filedialog.askopenfilename()
    print(file_path)

root = tk.Tk()
root.withdraw()

browse_button = tk.Button(text="Browse", command=browse_file)
browse_button.pack()

root.mainloop()

model = whisper.load_model("tiny")
result = model.transcribe("120.mp3")
with open('transcription.txt', 'w') as f:
    f.write(result["text"])
