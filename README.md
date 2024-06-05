# YouTube Transcript Scraper Bot

## Overview

The YouTube Transcript Scraper Bot is a powerful automation tool built with Selenium that allows users to effortlessly extract transcripts from YouTube videos. By simply providing a link to the desired YouTube video, this bot retrieves the transcript and saves it as a PDF file in the user's Downloads folder. The PDF file is aptly named after the video's title for easy identification.

## Features

- **Easy to Use**: Just input the link to any YouTube video, and the bot takes care of the rest.
- **Automated Transcript Extraction**: Leverages Selenium to navigate YouTube and extract the full transcript.
- **PDF Generation**: Transcripts are saved as PDF files, ensuring they are easy to read and share.
- **Title-based Naming**: Each PDF file is named after the corresponding YouTube video title, making it simple to organize and find your transcripts.
- **Saves in Downloads Folder**: Automatically saves the PDF file in your system's Downloads folder for convenience.

## How It Works

1. **Input Video Link**: Provide the link to the YouTube video from which you want to extract the transcript.
2. **Automated Navigation**: The bot uses Selenium to open the video, navigate to the transcript section, and extract the text.
3. **PDF Generation**: The extracted transcript is converted into a PDF file.
4. **Save PDF**: The PDF is saved in the Downloads folder with a filename matching the video's title.

## Installation

1. **Clone the Repository**:
    ```sh
    git clone https://github.com/yourusername/youtube-transcript-scraper.git
    cd youtube-transcript-scraper
    ```

2. **Install Dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

3. **Configure Selenium WebDriver**:
   - Download the WebDriver for your preferred browser (e.g., ChromeDriver for Google Chrome).
   - Ensure the WebDriver is in your system's PATH or specify the path in the script.

## Usage

1. **Run the Script**:
    ```sh
    python transcript_scraper.py
    ```

2. **Provide YouTube Link**: Enter the YouTube video link when prompted.

3. **Check Downloads Folder**: Find the generated PDF transcript in your Downloads folder.

## Example

```sh
Enter the YouTube video link: https://www.youtube.com/watch?v=dQw4w9WgXcQ
Transcript saved as 'Never Gonna Give You Up - Rick Astley.pdf' in your Downloads folder.
