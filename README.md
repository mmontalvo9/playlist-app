🎵 Playlist App with YouTube Search
This web app allows users to create and manage a custom music playlist — including YouTube video embedding, search functionality via the YouTube Data API, and CSV download support.

🚀 Features
Add songs with title, artist, duration, and optional YouTube video

Embed and play songs directly from the playlist

Search YouTube for music videos using keywords

Shuffle and display all added songs

Download your playlist as a .csv file

Modern UI using HTML/CSS and real-time JavaScript

🧠 Background
The core functionality of this app was adapted from a CSII data structures project using a Python-based Playlist class with doubly linked list implementation. The original code handled song storage and manipulation through command-line input, which was extended here into a full-stack web application.

🛠 Technologies Used
Layer	Tools / Languages
Frontend	HTML, CSS, JavaScript (vanilla)
Backend	Python (Flask web framework)
APIs	YouTube Data API v3
Storage	CSV file handling via Python csv module
Platform	Replit, Render, GitHub
Deployment	Hosted on Render.com

⚙️ Setup Instructions
Local Development
Clone this repository

Create a virtual environment and activate it

Install requirements:

bash
Copy
Edit
pip install -r requirements.txt
Run the app:

bash
Copy
Edit
python app.py
Visit http://localhost:81 in your browser

Deployment
This project is deployed using Render. You can also run it on Replit or another cloud platform with Python support.

🔐 API Key Usage
This project uses the YouTube Data API v3 for video search. You must:

Get an API key from Google Cloud Console

Add it securely to app.js or store it as an environment variable in your deployment platform

Note: For security reasons, the API key is not stored in this public repository.

👤 Author
Developed by Marc Sebastian Montalvo, adapting a CSII class project into a production-grade web application with extended capabilities and UI improvements.
