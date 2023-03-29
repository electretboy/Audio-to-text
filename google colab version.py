import ipywidgets as widgets
from google.colab import files
import whisper

upload_button = widgets.FileUpload()

def on_upload_button_value_change(change):
    uploaded_files = change["new"]
    if uploaded_files:
        uploaded_file = next(iter(uploaded_files))
        print(f"Selected file: {uploaded_file}")
        # Do something with the selected file, e.g. save it to disk
        with open(uploaded_file, "wb") as f:
            f.write(uploaded_files[uploaded_file]["content"])
        model = whisper.load_model("tiny")  
        result = model.transcribe(str(uploaded_file))
        with open('transcription.txt', 'w') as f:
            f.write(result["text"])
upload_button.observe(on_upload_button_value_change, names="value")
display(upload_button)
