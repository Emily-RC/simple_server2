import os
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_home():
    return "Hello, world!"

@app.route('/countries', methods=['GET'])
def get_countries():
    if request.method == 'GET':
        return render_template('countries.html') 

if __name__ == '__main__':
    app.run(
      debug=True,
      host="0.0.0.0" # Listen for connections _to_ any server
    )
