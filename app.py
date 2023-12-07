# Import necessary libraries
import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

# Create flask app instance
flask_app = Flask(__name__)

# Load the pre-trained machine learning model from a saved file
model = pickle.load(open('model.pkl', 'rb'))

# Define the route for the home page
@flask_app.route("/")
def Home():
    # Render the HTML template for the home page
    return render_template("index.html")

# Define the route for predicting based on user input
@flask_app.route("/predict", methods=["POST"])
def predict():
    # Retrieve the input features from the HTML form as a list of floats
    float_features = [float(x) for x in request.form.values()]
    
    # Convert the list of features into a NumPy array
    features = [np.array(float_features)]
    
    # Make a prediction using the loaded machine learning model
    prediction = model.predict(features)
    
    # Render the HTML template with the prediction result
    return render_template("index.html", prediction_text="The flower species is {}".format(prediction))

# Entry point to run the Flask web application
if __name__ == "__main__":
    # Run the Flask app in debug mode for development
    flask_app.run(debug=True)
