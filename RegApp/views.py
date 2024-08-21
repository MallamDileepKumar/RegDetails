from django.shortcuts import render, redirect
from django.views import View
from .models import Registration
from .forms import RegistrationForm, LoginForm
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

class RegisterView(View):
    def get(self, request):
        form = RegistrationForm()
        return render(request, 'register.html', {'form': form})

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return HttpResponse('Successfully Registered!')
        else:
            return HttpResponse('Registration Failed!')

class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', {'login': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = Registration.objects.filter(username=form.cleaned_data['username'],
                                               password=form.cleaned_data['password']).first()
            if user:
                return redirect('regdetails')
            else:
                return HttpResponse('Invalid email or password')
        return render(request, 'login.html', {'login': form})



class RegisterDetails(View):
    def get(self, request):
        registrations = Registration.objects.all()  # Fetch all registration records
        return render(request, 'regdetails.html', {'registrations': registrations})

