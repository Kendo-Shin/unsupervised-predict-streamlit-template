"""

    Streamlit webserver-based Recommender Engine.

    Author: Explore Data Science Academy.

    Note:
    ---------------------------------------------------------------------
    Please follow the instructions provided within the README.md file
    located within the root of this repository for guidance on how to use
    this script correctly.

    NB: !! Do not remove/modify the code delimited by dashes !!

    This application is intended to be partly marked in an automated manner.
    Altering delimited code may result in a mark of 0.
    ---------------------------------------------------------------------

    Description: This file is used to launch a minimal streamlit web
	application. You are expected to extend certain aspects of this script
    and its dependencies as part of your predict project.

	For further help with the Streamlit framework, see:

	https://docs.streamlit.io/en/latest/

"""
# Streamlit dependencies
import streamlit as st

# Data handling dependencies
import pandas as pd
import numpy as np
from pathlib import Path

# Function to import markdowns
def read_markdown_file(markdown_file):
    return Path(markdown_file).read_text()

# Custom Libraries
from utils.data_loader import load_movie_titles
from recommenders.collaborative_based import collab_model
from recommenders.content_based import content_model

# Data Loading
title_list = load_movie_titles('resources/data/movies.csv')

# App declaration
def main():

    # DO NOT REMOVE the 'Recommender System' option below, however,
    # you are welcome to add more options to enrich your app.
    page_options = ["Recommender System","Homepage","Information","About us"]

    # -------------------------------------------------------------------
    # ----------- !! THIS CODE MUST NOT BE ALTERED !! -------------------
    # -------------------------------------------------------------------
    page_selection = st.sidebar.selectbox("Choose Option", page_options)
    if page_selection == "Recommender System":
        # Header contents
        st.write('# Movie Recommender Engine')
        st.write('### EXPLORE Data Science Academy Unsupervised Predict')
        st.image('resources/imgs/Image_header.png',use_column_width=True)
        # Recommender System algorithm selection
        sys = st.radio("Select an algorithm",
                       ('Content Based Filtering',
                        'Collaborative Based Filtering'))

        # User-based preferences
        st.write('### Enter Your Three Favorite Movies')
        movie_1 = st.selectbox('First Option',title_list[14930:15200])
        movie_2 = st.selectbox('Second Option',title_list[25055:25255])
        movie_3 = st.selectbox('Third Option',title_list[21100:21200])
        fav_movies = [movie_1,movie_2,movie_3]

        # Perform top-10 movie recommendation generation
        if sys == 'Content Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = content_model(movie_list=fav_movies,
                                                            top_n=10)
                    st.title("We think you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")


        if sys == 'Collaborative Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = collab_model(movie_list=fav_movies,
                                                           top_n=10)
                    st.title("We think you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")


    # -------------------------------------------------------------------

    # ------------- SAFE FOR ALTERING/EXTENSION -------------------

    # Building out the "Homepage" page
    if page_selection == "Homepage":
        st.write('# uMovies :film_frames:')
        st.write('### We know our movies, and yours too...')
        st.image('resources/imgs/movies.jpg', use_column_width=True)
        st.subheader("Welcome to uMovies:registered:  :man-raising-hand:")
        st.subheader("your № 1 Movie Recommender")
        st.subheader("   ")# just a way to create space between texts
        st.subheader("   ")
        st.write("Navigate through the app with the side bar...")

    # Building out the "Information" page
    if page_selection == "Information":
        options = ["make a choice here ↓", "General Information", "EDA", "Model Information"]
        selection = st.sidebar.selectbox("What do you want to know?", options)

        if selection == "make a choice here ↓":
            st.image('resources/imgs/info_page.jpg', width=500)
            st.subheader("What kind of info do you need :question:")
            st.subheader(":arrow_upper_left: Make your choice from the side bar")

        if selection == "General Information":
            st.info("General Information")
			# You can read a markdown file from supporting resources folder
            info_markdown = read_markdown_file("resources/info1.md")
            st.markdown(info_markdown)
            
            st.image('resources/imgs/recommend.png', use_column_width=True)

            info_markdown = read_markdown_file("resources/info2.md")
            st.markdown(info_markdown)

        
        if selection == "EDA":
            st.info("Exploratory Data Analysis")
            st.write('## Some cool insights we got from the data')
            st.subheader("   ")# just a way to create space between texts
            st.subheader("   ")
            st.subheader("   ")

            st.image('resources/imgs/eda2.png', width=600,)
			# You can read a markdown file from supporting resources folder
            info_markdown = read_markdown_file("resources/eda2.md")
            st.markdown(info_markdown)
            st.subheader("   ")# just a way to create space between texts
            st.subheader("   ")

            st.image('resources/imgs/eda3.png', width=700)
			# You can read a markdown file from supporting resources folder
            info_markdown = read_markdown_file("resources/eda3.md")
            st.markdown(info_markdown)
            st.subheader("   ")# just a way to create space between texts
            st.subheader("   ")

            st.image('resources/imgs/eda4.png', width=700)
			# You can read a markdown file from supporting resources folder
            info_markdown = read_markdown_file("resources/eda4.md")
            st.markdown(info_markdown)
            st.subheader("   ")# just a way to create space between texts
            st.subheader("   ")
        
        if selection == "Model Information":
            st.info("Model Information")
			# You can read a markdown file from supporting resources folder
            info_markdown = read_markdown_file("resources/models.md")
            st.markdown(info_markdown)
    
    # Building out the "About us" page
    if page_selection == "About us":
        st.image('resources/imgs/logo.jpg', width=600)
        info_markdown = read_markdown_file("resources/mission.md")
        st.markdown(info_markdown)
        st.subheader("   ")# just a way to create space between texts
        st.subheader("   ")

        st.image('resources/imgs/tristan.png', width=300)
        st.write('### Tristan Krafft')
        st.write('#### - Data Scientist')
        st.write('#### - Team Lead')
        st.subheader("   ")# just a way to create space between texts
        st.subheader("   ")

        st.image('resources/imgs/kenny.jpeg', width=300)
        st.write('### Kenny Ozojie')
        st.write('#### - Data Scientist')
        st.write('#### - Product Lead')
        st.subheader("   ")# just a way to create space between texts
        st.subheader("   ")

        st.image('resources/imgs/felix.jpg', width=300)
        st.write('### Olasunkanmi Oyadokun')
        st.write('#### - Data Scientist')
        st.write('#### - Technical Lead')
        st.subheader("   ")# just a way to create space between texts
        st.subheader("   ")

        
    # You may want to add more sections here for aspects such as an EDA,
    # or to provide your business pitch.


if __name__ == '__main__':
    main()
