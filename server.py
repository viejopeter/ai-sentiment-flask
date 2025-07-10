from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Sentiment Detector")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/emotionDetector")
def sent_emotion_detector():

    text_to_analyze = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyze)
    return f"for the given statement, the system response is {response}"

if __name__ == "__main__":
   app.run(host="0.0.0.0",port=5000)

