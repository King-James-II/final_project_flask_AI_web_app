import json
import requests

def emotion_detector(text_to_analyse): 
    # Define the URL for the sentiment analysis API
    url = ("https://sn-watson-emotion.labs.skills.network/"
    "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict")

    # Define the header with necessary metadata
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Prepare the request body with the text to be analyzed
    req_body = { "raw_document": { "text": text_to_analyse } }

    # Send a POST request to the emotion prediction API
    response = requests.post(url, json=req_body, headers=header, timeout=10)

    if response.status_code == 400:
        # Handle server error by setting labels to None are return the empty dictionary
        emotions = {
            'anger': None, 
            'disgust': None, 
            'fear': None, 
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
        return emotions
    # Parse the JSON response
    formatted_response = json.loads(response.text)

    # Extract emotions and scores from the response
    emotions = formatted_response['emotionPredictions'][0]['emotion']

    # Determine the dominant emotion and set the value within the dictionary
    dominant_emotion = ""
    highest_score = 0
    for key, value in emotions.items():
        if value > highest_score:
            highest_score = value
            dominant_emotion = key
    emotions["dominant_emotion"] = dominant_emotion

    # Return the result as a dictionary
    return emotions
