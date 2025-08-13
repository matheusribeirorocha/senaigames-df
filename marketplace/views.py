from django.shortcuts import render

def index(request):
    return render(request,'marketplace/index.html')

# Create your views here.
def painel(request):
    return render(request,'marketplace/painel.html')