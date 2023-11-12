import os

from flask import Flask, redirect, render_template, request, url_for
from openai import OpenAI
api_key=os.environ.get(".env")
print(api_key)
client = OpenAI(
    api_key=os.environ.get(".env"),
)

app = Flask(__name__)


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        reflection = request.form["skills"]
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            temperature=0.6,
            messages=[
                {"role": "system","content": "Students will provide you with a list of soft and hard skills that they posses. In an HTML table without showing Markdown code like ```html, provide a list of career paths they can choose or transition to. Only include the HTML table in your response."},
                {"role": "user", "content": reflection}
            ]
        )
        return redirect(url_for("index", result=response.choices[0].message.content))

    result = request.args.get("result")
    return render_template("index.html", result=result)

'''
Sample prompt:

Strong:
I appreciated Walmart's implementation of sustainable practices. Their implementation of LED lighting and sustainable energy will likely have a measurable impact. I am not sure whether this is an example of greenwashing, though, because they provided their statistics in cumulative terms, rather than their annual emissions reductions.

Weak:


'''
