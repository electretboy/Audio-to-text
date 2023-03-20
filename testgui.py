'''
import whisper
import tkinter as tk
from tkinter import filedialog

def browse_file():
    file_path = filedialog.askopenfilename()
    print(str(file_path))
    model = whisper.load_model("tiny")
    result = model.transcribe(file_path)
    with open('transcription.txt', 'w') as f:
        f.write(result["text"])

root = tk.Tk()
root.withdraw()
root.deiconify()

browse_button = tk.Button(text="Browse", command=browse_file)
browse_button.pack()

root.mainloop()
'''
import os
import whisper
import tkinter as tk
from tkinter import filedialog

def browse_file():
    file_path = filedialog.askopenfilename()
    print(file_path)
    # Check that file exists and has a valid audio extension
    if os.path.isfile(file_path) and file_path.lower().endswith(('.mp3', '.wav', '.ogg')):
        model = whisper.load_model("tiny")
        result = model.transcribe(file_path)
        with open('transcription.txt', 'w') as f:
            f.write(result["text"])
    else:
        print("Invalid file or file format.")

root = tk.Tk()
root.withdraw()
root.deiconify()

browse_button = tk.Button(text="Browse", command=browse_file)
browse_button.pack()

root.mainloop()
