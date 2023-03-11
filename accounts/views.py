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
import matplotlib.pyplot as plt
import numpy as np
from github import Github
import telusko

BASE_DIR = Path(__file__).resolve().parent.parent
g = Github("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")
repo = g.get_repo("RohaanJohn/MatPlotLibIt")

# Create your views here.
@api_view(['GET', 'POST'])
def matplotlibit(request):
    # Generate data and create bar chart
    categories = ['A', 'B', 'C', 'D', 'E']
    counts = np.random.randint(1, 20, size=len(categories))
    plt.bar(categories, counts)
    plt.title('Bar chart of random data')
    plt.xlabel('Category')
    plt.ylabel('Count')
    
    # Save the chart as an image file
    image_name = f'Image{str(datetime.now())}.jpg'
    STATIC_URL = '/static/'
    STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
    ]
    STATIC_ROOT = os.path.join(BASE_DIR, 'assests')
    image_path = os.path.join(STATIC_ROOT, 'images', image_name)
    plt.savefig(image_path)
    
    # Open the image file, encode it as base64, and create a new file in a GitHub repo
    with open(image_path, 'rb') as f:
        image_bytes = f.read()
        string = base64.b64encode(image_bytes)
        pic_url = f'FinalImage/{image_name}'
        repo.create_file(pic_url, "commit", base64.b64decode(string))

    # Render the template with the image URL
    #context = {'image_url': f"{pic_url}"}
    context = {'image_url': f"{image_path}"}
    return render(request, 'my_template.html', context)

                      
                
    
    
 





    
