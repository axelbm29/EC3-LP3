from django.shortcuts import render

def home(request):
    title = "Untels"
    elementos_lista = [
        "Análisis y Diseño de Sistemas",
        "Introducción a la Programación",
        "Algoritmos y Estructura de Datos",
        "Sistemas de Información",
        "Sistemas Operativos",
        "Arquitectura de Computadoras"
    ]
    return render(request, 'miapp/home.html', {'title': title, 'elementos_lista': elementos_lista})
