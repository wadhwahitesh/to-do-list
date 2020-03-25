from django.shortcuts import render


# Create your views here.
def home(response):
    return render(response, 'home.html', {})


def display(response, n):
    return render(response, 'display.html', {'range':range(n+1)})
