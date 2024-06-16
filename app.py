from flask import Flask, jsonify
import json

app = Flask(__name__)

# Load quotes from JSON file
with open('quotes.json', 'r', encoding='utf-8') as f:
    quotes = json.load(f)

# Function to count total unique authors
def count_unique_authors():
    author_set = set()
    for quote in quotes:
        author_set.add(quote['author'])
    return len(author_set)

@app.route('/')
def home():
    total_quotes = len(quotes)
    total_authors = count_unique_authors()
    return f"Welcome to Quote API<br>Total quotes: {total_quotes}<br>Total authors: {total_authors}"

@app.route('/random-quote', methods=['GET'])
def random_quote():
    import random
    random_quote = random.choice(quotes)
    return jsonify(random_quote)

if __name__ == '__main__':
    app.run(debug=True)
