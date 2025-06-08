# 🎵 Playlist App with YouTube Search  
**Live site:** 👉 [https://playlist-app-8ggt.onrender.com](https://playlist-app-8ggt.onrender.com)

This web app allows users to create and manage a custom music playlist — including YouTube video embedding, search functionality via the YouTube Data API, and CSV download support.

---

## 🚀 Features

- 🎶 Add songs with title, artist, duration, and optional YouTube video  
- 🎥 Embed and play songs directly from the playlist  
- 🔍 Search YouTube for music videos using keywords  
- 🔀 Shuffle and display all added songs  
- 💾 Download your playlist as a `.csv` file  
- 🖥️ Modern UI using HTML/CSS and real-time JavaScript  

---

## 🧠 Background

The core functionality of this app was adapted from a **CSII data structures project**, originally written in Python with a doubly linked list–based `Playlist` class. This code served as the backend logic and was extended into a full-stack web application with live search, video support, and browser interactivity.

---

## 🛠 Technologies Used

| Layer        | Tools / Languages                           |
|--------------|----------------------------------------------|
| **Frontend** | HTML, CSS, JavaScript (vanilla)              |
| **Backend**  | Python (Flask web framework)                 |
| **API**      | YouTube Data API v3                          |
| **Storage**  | CSV file handling via Python's `csv` module  |
| **Platforms**| Replit, GitHub, Render                       |
| **Deployment**| Hosted on [Render](https://render.com/)     |

---

## ⚙️ Setup Instructions

### 🔧 Local Development

1. Clone this repository  
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
3. Run this app:
   python main.py

4. Visit http://localhost:5000 or your assigned port.

**### 🌐 Deployment Notes**
- The app is deployed on Render.
- No database is used — the playlist is stored in memory and can be downloaded as a CSV.
- API keys are stored securely in Render as environment variables and accessed dynamically via a backend route.

**### 🔐 API Key**
To use the YouTube search feature:
- You must create a free YouTube Data API key
- Add it to your deployment platform as YOUTUBE_API_KEY
- The frontend fetches it securely from a backend endpoint
- Note: The API key is not exposed in this repository.

### 👤 Author

Developed by **Marc Sebastian Montalvo**  
Adapted from CSII coursework and enhanced into a full-stack project.
