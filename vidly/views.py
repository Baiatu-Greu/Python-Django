from django.shortcuts import render

# we need to map this view function to a url endpoint


def home(request):
    return render(request, 'home.html')
