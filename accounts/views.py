from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import generics, permissions
from .serializers import RegisterSerializer
from django.contrib.auth.models import User
from .authentication import CsrfExempSessionAuthentication

def register_html_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request, user)
            return redirect('task_list')
        else:
            return render(request, 'accounts/register.html', {'form': form})
    else: 
        form = RegisterForm()
        return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password= password)

        if user:
            login(request, user)
            return redirect('task_list')
        else:
            return render(request, 'accounts/login.html', {
                'error': 'Credenciales incorrectas'
            })

    return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@method_decorator(csrf_exempt, name='dispatch')
class RegisterView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

