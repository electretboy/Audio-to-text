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
root.geometry('300x200')
root.title("Audio to text transcriber")
root.configure(bg='dark blue')
browse_button = tk.Button(root, text="Browse", command=browse_file, bg='light yellow')
browse_button.pack(padx=30, pady=30)

root.mainloop()
