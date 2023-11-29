from django.shortcuts import render

def home(request):
    context = {
        'title': 'UNTELS',
        'content': 'Este es tu contenido.',
    }
    return render(request, 'miapp/home.html', context)