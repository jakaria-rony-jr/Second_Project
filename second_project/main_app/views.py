from django.shortcuts import render

# Create your views here.

def index(requsts):
    return render(requsts, 'main_app/index.html')