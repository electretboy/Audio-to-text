import tkinter as tk
from tkinter import filedialog
import whisper

def browse_file():
    file_path = filedialog.askopenfilename()
    print("Selected file:", file_path)
    model = whisper.load_model("tiny")
    result = model.transcribe(str(file_path))
    with open('transcription.txt', 'w') as f:
        f.write(result.text)

root = tk.Tk()

browse_button = tk.Button(root, text="Browse", command=browse_file)
browse_button.pack()

root.mainloop()
