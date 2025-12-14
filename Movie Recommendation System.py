import pickle
import pandas as pd
import streamlit as st


def recommend(movie1):
    movie_index=movie[movie["title"]==movie1].index[0]
    distances=similarity[movie_index]
    movie_list=sorted(list(enumerate(distances)),reverse= True,key=lambda x:x[1])[1:6]

    recommended_movie=[]

    for a in movie_list:
        movie_id = movie.iloc[a[0]].movie_id
        recommended_movie.append(movie.iloc[a[0]].title)
    return recommended_movie



movie_dict= pickle.load(open('movie_dict.pkl', 'rb'))
movie= pd.DataFrame(movie_dict)


similarity=pickle.load(open('similarity.pkl', 'rb'))

st.title("Movie Recommendation System")

selected_movie_name = st.selectbox("Enter the name of the movie", movie["title"].values)

if st.button("Recommend"):
    recommendations= recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)














