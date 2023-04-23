
ElevenLabsTTSClient
Description

ElevenLabsTTSClient is a Python script that uses the ElevenLabs TTS API to convert text files to audio files in MP3 format. It provides a graphical user interface (GUI) using the Tkinter library, allowing users to select the input text files directory, output directory, and voice for text-to-speech conversion. The script supports multiple voices provided by the ElevenLabs TTS API and provides a progress bar to track the conversion progress.
Prerequisites

Before running the script, you need to set your ElevenLabs TTS API key by replacing "ADDYOURAPIKEYHERE" with your actual API key. You can obtain an API key by signing up for an account at the ElevenLabs TTS API website.
Dependencies

The script uses the following dependencies:

    tkinter: The standard Python GUI library for creating graphical user interfaces.
    filedialog: A module in tkinter that provides a file dialog for selecting directories.
    ttk: A module in tkinter that provides themed widgets.
    elevenlabs: A Python library for accessing the ElevenLabs TTS API.
    os: A Python module for working with operating system functionality.

How to Use

    Set your ElevenLabs TTS API key by replacing "ADDYOURAPIKEYHERE" with your actual API key.
    Run the script using a Python interpreter or IDE.
    The GUI window will open with input fields for the text files directory, output directory, and voice selection.
    Click the "Convert" button to start the text-to-speech conversion process.
    The progress bar will update to show the progress of the conversion.
    Once the conversion is complete, the result will be displayed in the log text box and the result label.

Notes

    The script validates the input directories to ensure they are valid before proceeding with the text-to-speech conversion.
    The script reads all text files with the ".txt" extension in the selected text files directory and generates an MP3 audio file for each text file.
    The generated MP3 files are saved in the selected output directory with the same name as the original text files.
    The script updates the progress bar and logs the conversion process in the log text box.
    Any errors that occur during the conversion process will be displayed in the result label.

Disclaimer

This script is provided as-is and may be subject to limitations and restrictions of the ElevenLabs TTS API. Make sure to review and comply with the terms of use and licensing agreements of the ElevenLabs TTS API before using this script in a production environment.
