from flask import Flask, render_template, request, redirect, jsonify
import string
import random

app = Flask(__name__)

# Dictionary to store the URLs
urls = {}

# Function to generate a random string of length 6 for short URLs
def generate_short_url():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(6))

# Route for the homepage
@app.route('/')
def home():
    return render_template('index.html')

# Route to handle shortening URLs
@app.route('/shorten', methods=['POST'])
def shorten_url():
    long_url = request.form['long_url']
    short_url = generate_short_url()

    # Store the URL in the dictionary
    urls[short_url] = long_url

    return jsonify({'short_url': short_url})

# Route to redirect short URLs to their corresponding long URLs
@app.route('/<short_url>')
def redirect_to_long_url(short_url):
    long_url = urls.get(short_url)
    if long_url:
        return redirect(long_url)
    else:
        return 'URL not found', 404

if __name__ == '__main__':
    app.run(debug=True)
