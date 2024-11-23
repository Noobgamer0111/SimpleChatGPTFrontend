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
    user_input = request.json.get('message')
    response = openai.Completion.create(
        engine="davinci",
        prompt=user_input,
        max_tokens=100
    )
    return jsonify({'message': response.choices[0].text.strip()})

if __name__ == '__main__':
    app.run(debug=True)
