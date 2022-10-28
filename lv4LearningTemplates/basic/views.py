from django.shortcuts import render

# Create your views here.

def index(request):
    context_dic = {"text" : "hello world" , 'number' : 100}
    return render(request , "basic/index.html" , context_dic)

def other(request):
    return render(request, "basic/other.html")

def relative(request):
    return render(request , "basic/relative_url_templates.html")
