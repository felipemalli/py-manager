from django.shortcuts import render

# Create your views here.

def index(request):
  return render(request, "index.html")

def carrinho(request):
  return render(request, "carrinho.html")
