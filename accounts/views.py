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
    '''
    # Save the chart to static/images
    image_name = 'bar_chart.png'
    image_path = os.path.join(settings.STATIC_ROOT, 'images', image_name)
    plt.savefig(image_path)
    '''
    image_name = f'Image{str(datetime.now())}.jpg'
    pic_url = f'Finalmage/{image_name}'
    repo.create_file(pic_url, "commit", base64.b64decode(plt))

    # Render the template with the image URL
    context = {'image_url': f"{pic_url}"}
    return render(request, 'my_template.html', context)

                      
                
    
    
 





    
