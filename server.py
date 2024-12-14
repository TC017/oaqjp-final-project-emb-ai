"""Emotion Detection Server."""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def return_emotions():
    """
    Returns the emotions detected in the given text.

    """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')
    # Pass the text to the sentiment_analyzer function and store the response
    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] == 'None':
        return "Invalid text! Please try again!"
    return (
        f"For the given statement, the system response is "
        f"anger: {response['anger']}, "
        f"disgust: {response['disgust']}, "
        f"fear: {response['fear']}, "
        f"joy: {response['joy']} "
        f"and sadness: {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}"
    )


@app.route("/")
def render_index_page():
    """
    Renders the index page.
    """
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
