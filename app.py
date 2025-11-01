from flask import Flask, render_template, request
from transformers import AutoTokenizer, AutoModelForQuestionAnswering
import torch
import os

app = Flask(__name__, template_folder="./website", static_folder="./website")

# Load the model and tokenizer from the 'model' directory
model_path = os.path.join(os.getcwd(), "model")
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForQuestionAnswering.from_pretrained(model_path)

@app.route('/')
def home():
    return render_template('Home.html')

@app.route('/qa')
def qa():
    return render_template('qa.html')

@app.route('/sample')
def sample():
    return render_template('sample.html')

@app.route('/tiles') 
def tiles():
    return render_template('tiles.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/answer', methods=['POST'])
def answer():
    try:
        context = request.form.get('report', '')
        question = request.form.get('question', '')
        
        if not context or not question:
            return {'error': 'Please provide both report and question'}, 400

        inputs = tokenizer.encode_plus(question, context, return_tensors='pt', truncation=True, max_length=512)
        with torch.no_grad():
            outputs = model(**inputs)
            start_scores = outputs.start_logits
            end_scores = outputs.end_logits

        start = torch.argmax(start_scores)
        end = torch.argmax(end_scores) + 1
        answer = tokenizer.convert_tokens_to_string(tokenizer.convert_ids_to_tokens(inputs["input_ids"][0][start:end]))

        if not answer:
            return {'answer': 'No clear answer found in the text'}

        return {'answer': answer}

    except Exception as e:
        return {'error': f'Error processing your request: {str(e)}'}, 500

if __name__ == '__main__':
    app.run(debug=True)
