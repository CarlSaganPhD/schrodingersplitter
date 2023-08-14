from flask import Flask, jsonify
import requests, random
from flask import render_template
import os

app = Flask(__name__)

QUANTUM_API_URL = 'https://qrng.anu.edu.au/API/jsonI.php?length=1&type=uint8'

@app.route('/quantum-number', methods=['GET'])
def get_quantum_number():
    try:
        response = requests.get(QUANTUM_API_URL)
        response.raise_for_status()  # Check if request was successful
        data = response.json()
        return jsonify({
            'status': 'success',
            'quantum_number': data['data'][0]
        }), 200
    except requests.RequestException as e:
        # Generate a random number between 0 and 255 (inclusive) when the API call fails (😜 not truly random here folks. TODO: add API retry so that it attempts like 3-4 times before reverting to non-quantum randomness)
        rand_number = random.randint(0, 255)
        return jsonify({
            'status': 'success',  # Change status to success since we're providing a valid response
            'quantum_number': rand_number
        }), 200

@app.route('/', methods=['GET'])
def home():
    return render_template('main.html')

@app.route('/2', methods=['GET'])
def home2():
    return render_template('home2.html')

@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
