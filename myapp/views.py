from django.shortcuts import render
from django.http import HttpResponse
from .models import Student

# Create your views here.
def hello_world(request):
    return HttpResponse("""
                        <html>
                        <head>
                        <title>Learning Django</title>
                        </head>
                        <body>
                        <h1>Heading 1</h1>
                        <h2>Heading 2</h2>
                        <h3>Heading 3</h3>
                        <h4>Heading 4</h4>
                        </body>
                        
                        </html>
                        
                        
                        """)
    
def hello(request):
    return HttpResponse("<h1> Hello</h1>")

def world(request):
    return HttpResponse("<h1>World</h1>")

def home(request):
    return render(request, template_name='myapp/home.html')

def portfolio(request):
    return render(request, template_name='myapp/index.html')

def temp_inherit_home(request):
    items=[
        {"name": "butter", "shop_location":"KTM", "price":300 },
        {"name": "sugar", "shop_location":"BKT", "price":300 },
        {"name": "coffee", "shop_location":"KTM", "price":30 },
        {"name": "milk", "shop_location":"LTP", "price":50 },
    ]
    return render(request, template_name='myapp/temp_inherit_home.html', context={"name":"John", "age":30, "address":"KTM", "items":items})

def temp_inherit_features(request):
    items=[
        {"name":"butter", "desc":"This is butter"},
        {"name":"bread", "desc":"This is bread"},
        {"name":"cheese", "desc":"This is cheese"},
    ]
    return render(request,template_name='myapp/temp_inherit_features.html', context={"items":items})

def temp_inherit_pricing(request):
    students= Student.objects.all()
    return render(request,template_name='myapp/temp_inherit_pricing.html', context={"students":students})