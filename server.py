"""
This script defines a Flask application for detecting emotions in text using the EmotionDetection 
package.

The application provides an endpoint "/emotionDetector" for analyzing text input and detecting 
emotions.
It utilizes the `emotion_detector` function from the EmotionDetection package.

"""

# Import Flask, render_template, request from the flask pramework package
from flask import Flask, render_template, request
# Import the emotion_detector function from the package created
from EmotionDetection.emotion_detection import emotion_detector

# Initiate the Flask app
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emote_analyzer():
    """
    This function analyzes the text input provided through the "/emotionDetector" endpoint
    and detects the emotions expressed in the text using the `emotion_detector` function.

    Returns:
        str: A response message indicating the detected emotions and the dominant emotion.
    """
    text_to_analyze = str(request.args.get('textToAnalyze').lower())
    response = emotion_detector(text_to_analyze)

    # Error handling if response is empty.
    if response['dominant_emotion'] is None:
        return "Invalid test! Please try again!"

    anger = f"'anger': {response['anger']}"
    disgust = f"'disgust': {response['disgust']}"
    fear = f"'fear': {response['fear']}"
    joy = f"'joy': {response['joy']}"
    sadness = f"'sadness': {response['sadness']}"
    dominant = response['dominant_emotion']

    text_response = (f"For the given statement, the system response is {anger}, {disgust}, {fear},"
                     f" {joy} and {sadness}. The dominant emotion is {dominant}.")
    return text_response

@app.route("/")
def render_index_page():
    ''' 
    This function initiates the rendering of the main application
    page over the Flask channel.
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
