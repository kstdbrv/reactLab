from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'main/index.html')


def post(request):
    return render(request, 'main/post_template.html')
