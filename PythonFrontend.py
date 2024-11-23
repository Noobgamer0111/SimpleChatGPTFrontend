# Run this in your terminal, not in the script
# pip install Flask
# pip install openai

from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# Set your OpenAI API key here
openai.api_key = 'your-api-key-here'

@app.route('/ask', methods=['POST'])
def chat():
    data = request.get_json()
    response = openai.Completion.create(
        engine="davinci",
        prompt=data['question'],
        max_tokens=150
    )
    return jsonify({'response': response.choices[0].text.strip()})

if __name__ == '__main__':
    app.run(debug=True)
