from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from rest_framework.decorators import api_view
from django.core import exceptions, validators
from rest_framework.response import Response
import smtplib
import requests
import json
import os
import os.path
import base64
from io import BytesIO
from pathlib import Path
from PIL import Image, ImageOps
from datetime import datetime
import openai

# Create your views here.
@api_view(['GET', 'POST'])
def ask(request):
                
              if request.method== 'POST':
                    openai.api_key = "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"
                    question = request.POST['question']
                    prompt = (f"Question: {question}\n")
                    response = openai.Completion.create(
                    engine="text-davinci-002",
                    prompt=prompt,
                    max_tokens=2000,
                    n=1,
                    stop=None,
                    temperature=0.5,
                    )
                    text = response['choices'][0]['text']
                    text = text.replace("\n", "")
                    return Response({"output":text})
                       
              else:
                return render(request,'dhwani.html')
   # [(0 is Happy), (1 is Angry), (2 is Sad), (3 is Fear)]


                      
                
    
    
 





    
