# 309-Error
# 309-Error — BERT-Based Emotion & Sentiment Analysis Web App

A Flask web application that uses a fine-tuned BERT model to classify text into emotion categories, infer overall sentiment, assign an intensity score, and visualize sentiment progression over time.

## Overview

This project was built for **Megathon 2024** and combines:

- a Flask-based web interface
- a fine-tuned BERT sequence classification model
- emotion-to-sentiment mapping
- sentiment intensity scoring
- dynamic sentiment trend visualization

The app allows a user to enter text, receive an emotion prediction, view overall sentiment, and track how sentiment changes across multiple inputs.

## What the app does

For a given text input, the system:

1. tokenizes the text using a BERT tokenizer
2. runs inference using a fine-tuned `bert-base-uncased` sequence classification model
3. predicts one of the learned emotion labels
4. maps the predicted emotion to:
   - an overall sentiment (`positive` or `negative`)
   - an intensity score
5. stores results and plots sentiment intensity across multiple user inputs over time

## Model Details

The repository includes a fine-tuned BERT classification model based on:

- **Base model:** `bert-base-uncased`
- **Architecture:** `BertForSequenceClassification`
- **Classification type:** single-label classification
- **Number of labels:** 6

The app also uses a label encoder to convert model outputs back into human-readable emotion labels.

## Repository Structure

```text
megathon-24/
├── app/
│   ├── app.py
│   ├── config.json
│   ├── label_encoder.joblib
│   ├── static/
│   └── templates/
├── trained-model/
├── app.zip
└── README.md
```

> Note: Ensure the model path used in `app.py` matches the actual model folder name in the repository.

## Tech Stack

- **Backend:** Flask
- **Modeling:** Hugging Face Transformers, PyTorch
- **Visualization:** Matplotlib
- **Serialization:** Joblib
- **Frontend:** HTML, CSS, JavaScript

## How to Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/garimamittal13/megathon-24.git
cd megathon-24
```

### 2. Create and activate a virtual environment

#### macOS / Linux
```bash
python3 -m venv venv
source venv/bin/activate
```

#### Windows
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install flask torch transformers joblib matplotlib scikit-learn
```

### 4. Fix the model path if needed

Open `app/app.py` and make sure the model path matches your repository.

For example, if your model folder is:

```text
trained-model/
```

then update the loading lines accordingly.

Example:

```python
model = BertForSequenceClassification.from_pretrained('./trained-model')
tokenizer = BertTokenizer.from_pretrained('./trained-model')
label_encoder = joblib.load('./trained-model/label_encoder.joblib')
```

### 5. Run the Flask app

From inside the `app/` directory:

```bash
cd app
python app.py
```

### 6. Open the app in your browser

By default, Flask runs at:

```text
http://127.0.0.1:5000
```

## App Routes

The app currently includes these routes:

- `/` — introduction page
- `/home` — main input page
- `/in-depth-analysis` — analysis page
- `/predict` — returns emotion / sentiment prediction
- `/plot` — returns sentiment-over-time plot

## Example Output

For a text input, the app returns:

- **Predicted Label** — the emotion class predicted by the model
- **Overall Sentiment** — positive or negative
- **Intensity** — a derived sentiment intensity score

## Why this project matters

This project demonstrates:

- deployment of a transformer-based NLP model in a web app
- integration of machine learning inference with a user-facing interface
- emotion classification and sentiment reasoning
- lightweight analytics through temporal sentiment visualization
- full-stack hackathon prototyping with AI components

## Future Improvements

Potential extensions include:

- confidence score display for all classes
- batch analysis of multiple text entries
- persistent user sessions
- improved visualization dashboards
- deployment on Render / Hugging Face Spaces
- support for chat-style sentiment tracking

## Repository

GitHub: [garimamittal13/megathon-24](https://github.com/garimamittal13/megathon-24)
