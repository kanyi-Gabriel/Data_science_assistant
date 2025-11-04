# analyzer/views.py

from django.shortcuts import render
# No need for HttpResponse if you only use render
import os
from openai import OpenAI

# Make sure your API key is loading (see next section)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def home(request):
    greetings = None

    # This block handles when the user submits the form
    if request.method == 'POST':
        # Get the name from the submitted form data
        name = request.POST.get('name', 'Guest')

        # Generate a friendly greeting using OpenAI
        prompt = f"Generate a friendly, 1-sentence greeting for {name}."

        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": prompt}
                ]
            )
            greetings = response.choices[0].message.content
        except Exception as e:
            # Handle potential API errors
            greetings = f"An error occurred: {e}"

    # This return statement handles BOTH GET and POST requests.
    # If it's a GET request, 'greetings' is None.
    # If it's a POST request, 'greetings' has the AI's response.
    return render(request, 'analyzer/home.html', {'greetings': greetings})