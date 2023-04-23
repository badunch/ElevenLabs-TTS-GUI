from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from elevenlabs import set_api_key, voices, generate
import os

# Set your API key
set_api_key("ADDYOURAPIKEYHERE")

# Get the list of available voices
all_voices = voices()

# Extract the names of the voices
voice_names = [voice.name for voice in all_voices]

# Define function to handle button click event
def convert_text_to_audio():
    try:
        # Get selected voice
        voice_name = voice_var.get()
        voice = next((voice for voice in all_voices if voice.name == voice_name), None)

        # Get selected directories
        text_files_directory = text_files_directory_var.get()
        output_directory = output_directory_var.get()

        # Validate directories
        if not os.path.isdir(text_files_directory) or not os.path.isdir(output_directory):
            raise ValueError("Invalid directory")

        # Get list of text files
        text_files = [file_name for file_name in os.listdir(text_files_directory) if file_name.endswith(".txt")]

        # Configure progress bar
        progress_bar['value'] = 0
        progress_bar['maximum'] = len(text_files)
        progress_bar.update()

        # Loop through the text files
        for i, file_name in enumerate(text_files, 1):
            text_file_path = os.path.join(text_files_directory, file_name)

            # Extract the file name from the text file path
            file_name = os.path.splitext(os.path.basename(text_file_path))[0]

            # Read the text from the file
            with open(text_file_path, 'r') as file:
                text = file.read()

            # Generate audio from the text using the given voice
            audio = generate(text=text, voice=voice)

            # Save the audio as an MP3 file with the same name as the text file
            output_path = os.path.join(output_directory, f"{file_name}.mp3")
            with open(output_path, 'wb') as file:
                file.write(audio)

            # Update progress bar and log
            progress_bar['value'] = i
            progress_bar.update()
            log_text.insert(END, f"Converted '{file_name}.txt' to '{file_name}.mp3'\n")
            log_text.see(END)

        result_label.config(text="Conversion completed successfully!")
    except Exception as e:
        result_label.config(text=str(e))

# Create Tkinter window
root = Tk()
root.title("ElevenLabsTTSClient")

text_files_directory_label = Label(root, text="Text Files Directory:")
text_files_directory_label.grid(row=0, column=0, padx=10, pady=10, sticky=W)

text_files_directory_var = StringVar()
text_files_directory_entry = Entry(root, textvariable=text_files_directory_var, width=50)
text_files_directory_entry.grid(row=0, column=1, padx=10, pady=10, sticky=W)

output_directory_label = Label(root, text="Output Directory:")
output_directory_label.grid(row=1, column=0, padx=10, pady=10, sticky=W)

output_directory_var = StringVar()
output_directory_entry = Entry(root, textvariable=output_directory_var, width=50)
output_directory_entry.grid(row=1, column=1, padx=10, pady=10, sticky=W)

voice_label = Label(root, text="Select Voice:")
voice_label.grid(row=2, column=0,padx=10, pady=10, sticky=W)

voice_var = StringVar()
voice_dropdown = ttk.Combobox(root, textvariable=voice_var, values=voice_names)
voice_dropdown.grid(row=2, column=1, padx=10, pady=10, sticky=W)
voice_dropdown.current(0)

convert_button = Button(root, text="Convert", command=convert_text_to_audio)
convert_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

progress_bar = ttk.Progressbar(root, mode='determinate')
progress_bar.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky=W+E)

log_text = Text(root, height=10, width=60)
log_text.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

result_label = Label(root, text="")
result_label.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
