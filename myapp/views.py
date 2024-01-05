from django.shortcuts import render
from django.http import HttpResponse

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