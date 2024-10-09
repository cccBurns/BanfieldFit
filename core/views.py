from django.shortcuts import render

def inicio(request):
    
    return render(request, 'core/inicio.html', {})

def about(request):
    
    return render(request, 'core/about.html', {})

def planes(request):
    
    return render(request, 'core/planes.html', {})

def horarios(request):
    
    return render(request, 'core/horarios.html', {})

def contacto(request):
    
    return render(request, 'core/contacto.html', {})