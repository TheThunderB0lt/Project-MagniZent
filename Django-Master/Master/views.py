from django.shortcuts import render, HttpResponse

# Create your views here.
def home_screen_view(request):
    # return HttpResponse("This is home page")
    return render(request, "Master/index.html")

def about_view(request):
    return HttpResponse("This is about page")

def team_view(request):
    return HttpResponse("This is team page")

def contact_view(request):
    return HttpResponse("This is contact page")
