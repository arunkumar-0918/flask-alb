import flask

app=flask.Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

@app.route('/fine')
def fine():
    return "I'm fine, thank you!"

@app.route('/weather')
def weather():
    return "The weather is great today!" 

if __name__ == '__main__':
    app.run(debug=True)