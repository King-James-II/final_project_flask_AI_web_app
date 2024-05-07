# Import Flask, render_template, request from the flask pramework package
from flask import Flask, render_template, request
# Import the emotion_detector function from the package created
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emote_analyzer():
    text_to_analyze = str(request.args.get('textToAnalyze').lower())
    response = emotion_detector(text_to_analyze)
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
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
