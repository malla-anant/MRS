import streamlit as st
import pickle
import pandas as pd
import requests


API_KEY = "8265bd1679663a7ea12ac168da84d2e8"
TMDB_MOVIE_URL = "https://api.themoviedb.org/3/movie/{}?api_key={}&language=en-US"
TMDB_SEARCH_URL = "https://api.themoviedb.org/3/search/movie?api_key={}&query={}"


def fetch_poster(movie_id, title=None):
    try:
        # Try fetching with movie ID
        url = TMDB_MOVIE_URL.format(movie_id, API_KEY)
        response = requests.get(url, timeout=5)

        if response.status_code == 200:
            data = response.json()
            if data.get("poster_path"):
                return "https://image.tmdb.org/t/p/w500/" + data["poster_path"]

        # Fallback: Search by title
        if title:
            search_url = TMDB_SEARCH_URL.format(API_KEY, title)
            search_response = requests.get(search_url, timeout=5)

            if search_response.status_code == 200:
                results = search_response.json().get("results")
                if results:
                    poster_path = results[0].get("poster_path")
                    if poster_path:
                        return "https://image.tmdb.org/t/p/w500/" + poster_path

        # Final fallback
        return "https://via.placeholder.com/500x750.png?text=No+Image"

    except requests.exceptions.RequestException as e:
        print(f"[ERROR] fetch_poster: {e}")
        return "https://via.placeholder.com/500x750.png?text=No+Image"


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_posters = []

    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id
        movie_title = movies.iloc[i[0]].title
        poster = fetch_poster(movie_id, movie_title)

        recommended_movies.append(movie_title)
        recommended_posters.append(poster)

    return recommended_movies, recommended_posters


# Load data
movies_dict = pickle.load(open("movie_dict.pkl", "rb"))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open("similarity.pkl", "rb"))

# Streamlit UI
st.markdown("<h1 style='color:#FFFFFF;'>🎬 Movie Recommender System</h1>", unsafe_allow_html=True)
movie_list = movies['title'].values
selected_movie = st.selectbox("Type or select a movie from the dropdown", movie_list)

if st.button("Show Recommendation"):
    names, posters = recommend(selected_movie)
    cols = st.columns(5)
    for i in range(5):
        with cols[i]:
            st.text(names[i])
            st.image(posters[i])
