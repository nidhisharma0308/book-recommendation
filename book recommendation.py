from flask import Flask, render_template, request
import pickle
import pandas as pd


# Load the model from the pickle file
with open('books.pkl', 'rb') as f:
    model = pickle.load(f)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('books.html')

def get_recommendations(title):
    # Example logic using the loaded model
    # Replace this with your actual model logic
    return model.predict(title)



@app.route('/recommendations', methods=['POST'])
def recommendations():
    book = request.form['book']
    recommended_books = get_recommendations(book)
    return render_template('recommendations.html', book=book, recommended_books=recommended_books)


if __name__ == '__main__':
    app.run(debug=True)
