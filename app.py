from flask import Flask, render_template, request, jsonify
from sales_agent import SalesAgent
import stripe
import os

app = Flask(__name__)

# API Keys
stripe.api_key = ""
os.environ["OPENAI_API_KEY"] = ""

agent = SalesAgent()


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/process', methods=['POST'])
def process():
    user_input = request.json['message']
    response = agent.process_input(user_input)
    return jsonify({'response': response})


if __name__ == '__main__':
    app.run(debug=True)
