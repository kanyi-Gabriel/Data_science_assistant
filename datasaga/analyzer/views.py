from django.shortcuts import render
from django.http import HttpResponse
import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def home(request):
    greetings = None

    if request.method == 'GET':
        name = request.POST.get('name', 'Guest')

        # Generate a friendly greeting using OpenAI
        prompt = f"Generate a friendly greeting for {name}."

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )

        greetings = response.choices[0].message.content


    return HttpResponse(request, 'analyzer/home.html', {'greetings': greetings})