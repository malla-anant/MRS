🎬 Movie Recommender System

A content-based movie recommender system built using Python, Streamlit, and TMDb API. Given a movie, the system suggests five similar movies based on movie metadata and similarity scores.

🔍 Features
Select any movie from the dropdown menu

Get 5 personalized movie recommendations

Displays posters using The Movie Database (TMDb) API

Clean and interactive Streamlit interface

Fallback mechanism to ensure poster availability

🛠️ Tech Stack
Frontend: Streamlit

Backend: Python

ML Model: Cosine similarity on precomputed feature vectors

Data: TMDb for posters, pickled data for movie similarity

Libraries: pandas, pickle, requests, streamlit

🚀 Getting Started
1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/yourusername/Movie-Recommender-System.git
cd Movie-Recommender-System
2. Install Dependencies
Make sure you have Python installed, then run:

bash
Copy
Edit
pip install -r requirements.txt
Required packages:

txt
Copy
Edit
streamlit
pandas
requests
3. Add Required Files
Ensure the following files are in your project directory:

movie_dict.pkl

similarity.pkl

These files are used for mapping movie titles and calculating similarity.

4. Run the App
bash
Copy
Edit
streamlit run app.py
The app will open in your browser at http://localhost:8501.

📦 Project Structure
bash
Copy
Edit
.
├── app.py                  # Main Streamlit app
├── movie_dict.pkl          # Movie metadata
├── similarity.pkl          # Precomputed similarity matrix
├── Screenshot.png          # Screenshot for README
├── requirements.txt        # Python dependencies
└── README.md               # This file
🔑 API Key Note
This project uses the TMDb API for fetching movie posters. An API key is hardcoded for demonstration. For production or deployment:

Replace the key with your own from TMDb

Store it in environment variables for security

🧠 How it Works
When a movie is selected, its feature vector is compared to others using cosine similarity

The top 5 similar movies (excluding the selected one) are displayed with posters

Posters are fetched using the TMDb API (with fallback search if movie ID fails)

📸 Demo

🙋‍♂️ Author
Your Name
📧 your.email@example.com
🔗 GitHub

⭐️ Show Your Support
If you like this project, give it a ⭐ on GitHub!
