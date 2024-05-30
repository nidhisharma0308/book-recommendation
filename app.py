import streamlit as st
import pickle
import numpy as np

# Load the pickled data
pt = pickle.load(open("pt.pkl", "rb"))
books = pickle.load(open("books.pkl", "rb"))
similarity_score = pickle.load(open("similarity_scores.pkl", "rb"))

def display_available_books():
    st.write("List of Available Books:")
    book_list = pt.index.tolist()
    selected_book = st.selectbox("Select a book:", book_list)
    return selected_book

# Define the recommendation function
def recommend(book_name):
    index = np.where(pt.index == book_name)[0][0]
    similar_items = sorted(list(enumerate(similarity_score[index])), key=lambda x: x[1], reverse=True)[1:6]
    recommended_books = [pt.index[i[0]] for i in similar_items]
    return recommended_books


# Streamlit app code
st.title("Book Recommendation System")


book_name = display_available_books()


# User input for the book name
#book_name = st.text_input("Enter a book name:")

# Recommendation button
if st.button("Recommend"):
    if book_name in pt.index:
        recommendations = recommend(book_name)
        st.write("Recommended Books:")
        for book in recommendations:
            st.write(book)
    else:
        st.write("Book not found in the dataset. Please try another book.")
