from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse

def hello(request):
   text = """<h1>Hello World !</h1>"""
   return HttpResponse(text)

def index(request):
   return render(request,'index.html', {'name':'Tom'})

def viewsArticle(request, articleId):
    return render(request, "detail.html", {"id": articleId})

def viewsArticles(request, month, year):
    return render(request, "details.html", {"month": month,"year":year})