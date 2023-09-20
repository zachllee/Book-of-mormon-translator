from flask import Flask, render_template, request, redirect, url_for
import openai

app = Flask(__name__)

# Initialize OpenAI API with your API key
openai.api_key = 'YOUR_OPENAI_API_KEY'


@app.route('/', methods=['GET', 'POST'])
def index():
    response_text = ""
    if request.method == 'POST':
        user_query = request.form['query']
        response_text = generate_transform(user_query)

    return render_template('index.html', response=response_text)


def generate_transform(sample_input):
    _prompt = f"""
    I want you to translate the following input using the prose found in the book of mormon. You will take the input, and "translate" them into book of mormon speak:
    {sample_input}
    """
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": _prompt}],
        temperature=0.1
    )

    return response.choices[0].message.content


if __name__ == '__main__':
    app.run(debug=True)
