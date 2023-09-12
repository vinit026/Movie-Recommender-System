import streamlit as st
import pickle
import pandas as pd

df = pickle.load(open("movie_dict.pkl", "rb"))
df = pd.DataFrame(df)

similarity = pickle.load(open("similarity.pkl","rb"))


def recommend(movie):
    movie_index = df[df["title"] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse = True, key = lambda x:x[1])[1:6]
    
    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(df.iloc[i[0]].title)
    return recommended_movies

st.title("
███╗░░░███╗░█████╗░██╗░░░██╗██╗███████╗  ██████╗░███████╗░█████╗░░█████╗░███╗░░░███╗███╗░░░███╗███████╗███╗░░██╗██████╗░
████╗░████║██╔══██╗██║░░░██║██║██╔════╝  ██╔══██╗██╔════╝██╔══██╗██╔══██╗████╗░████║████╗░████║██╔════╝████╗░██║██╔══██╗
██╔████╔██║██║░░██║╚██╗░██╔╝██║█████╗░░  ██████╔╝█████╗░░██║░░╚═╝██║░░██║██╔████╔██║██╔████╔██║█████╗░░██╔██╗██║██║░░██║
██║╚██╔╝██║██║░░██║░╚████╔╝░██║██╔══╝░░  ██╔══██╗██╔══╝░░██║░░██╗██║░░██║██║╚██╔╝██║██║╚██╔╝██║██╔══╝░░██║╚████║██║░░██║
██║░╚═╝░██║╚█████╔╝░░╚██╔╝░░██║███████╗  ██║░░██║███████╗╚█████╔╝╚█████╔╝██║░╚═╝░██║██║░╚═╝░██║███████╗██║░╚███║██████╔╝
╚═╝░░░░░╚═╝░╚════╝░░░░╚═╝░░░╚═╝╚══════╝  ╚═╝░░╚═╝╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚══╝╚═════╝░

░██████╗██╗░░░██╗░██████╗████████╗███████╗███╗░░░███╗
██╔════╝╚██╗░██╔╝██╔════╝╚══██╔══╝██╔════╝████╗░████║
╚█████╗░░╚████╔╝░╚█████╗░░░░██║░░░█████╗░░██╔████╔██║
░╚═══██╗░░╚██╔╝░░░╚═══██╗░░░██║░░░██╔══╝░░██║╚██╔╝██║
██████╔╝░░░██║░░░██████╔╝░░░██║░░░███████╗██║░╚═╝░██║
╚═════╝░░░░╚═╝░░░╚═════╝░░░░╚═╝░░░╚══════╝╚═╝░░░░░╚═╝")

selected_movie_name = st.selectbox("Select Movie Name", df["title"].values)

if st.button("Recommend"):
    recommendations = recommend(selected_movie_name)
    st.write(recommendations)
