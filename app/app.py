
from flask import Flask, render_template, request, jsonify
import torch
import joblib
import torch.nn.functional as F
import matplotlib.pyplot as plt
from transformers import BertTokenizer, BertForSequenceClassification
import io
import base64
from matplotlib.figure import Figure

app = Flask(__name__)

# Load the model, tokenizer, and label encoder (adjust paths as needed)
model = BertForSequenceClassification.from_pretrained('./trained_model2')
tokenizer = BertTokenizer.from_pretrained('./trained_model2')
label_encoder = joblib.load('./trained_model2/label_encoder.joblib')
model.eval()
sentiment_data = []

def predict(text):
    # Tokenize and classify text as per your function
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=128)
    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits
        probabilities = F.softmax(logits, dim=1)
    predicted_class_id = logits.argmax().item()
    predicted_label = label_encoder.inverse_transform([predicted_class_id])[0]
    probability_percentage = probabilities[0][predicted_class_id].item() * 100
    negative_labels = {"anger", "sadness", "fear"}
    positive_labels = {"happy", "love", "surprise"}
    overall_sentiment = "negative" if predicted_label in negative_labels else "positive"
    intensity = (probability_percentage // 10) + 1
    return {"Overall Sentiment": overall_sentiment, "Intensity": intensity, "Predicted_label": predicted_label}

def plot_sentiment_over_time(sentiment_data):
    time_steps = list(range(1, len(sentiment_data) + 1))
    intensities = [
        data['Intensity'] if data['Overall Sentiment'] == 'positive' else -data['Intensity']
        for data in sentiment_data
    ]
    fig = Figure()
    ax = fig.subplots()
    ax.plot(time_steps, intensities, marker='o', linestyle='-', color='blue')
    ax.axhline(0, color='black', linewidth=1)
    ax.set_title("User Sentiment Over Time")
    ax.set_xlabel("Input Number")
    ax.set_ylabel("Sentiment Intensity")
    ax.grid(True)
    buf = io.BytesIO()
    fig.savefig(buf, format="png")
    buf.seek(0)
    plot_url = base64.b64encode(buf.getvalue()).decode('utf8')
    return plot_url

@app.route('/')
def introduction():
    return render_template('intro.html')  # Replace with the name of your introduction page template

# Route for the index page (where you'll go after clicking the "Start" button)
@app.route('/home')
def home():
    return render_template('index.html')  # This serves your index.html page

@app.route('/in-depth-analysis')
def in_depth_analysis():
    return render_template('analysis.html')

@app.route('/predict', methods=['POST'])
def analyze():
    text_input = request.form['text']
    result = predict(text_input)
    sentiment_data.append(result)
    return jsonify(result)

@app.route('/plot')
def plot():
    plot_url = plot_sentiment_over_time(sentiment_data)
    return jsonify({'plot_url': plot_url})

if __name__ == "__main__":
    app.run(debug=True)