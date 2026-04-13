from flask import Flask

# Create an instance of the Flask class
app = Flask(__name__)

# Use a decorator to define the route for the home page
@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"

if __name__ == "__main__":
    # Start the local development server
    app.run(debug=True)
