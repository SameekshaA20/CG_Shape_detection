from django.shortcuts import render

# Create your views here.
def uploadForm(request):
    return render(request,'layout.html')