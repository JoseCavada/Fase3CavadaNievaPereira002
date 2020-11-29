from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm


#class SignUp(generic.CreateView):
def register(request):
    #form_class = UserCreationForm
    #success_url = reverse_lazy('login')
    #template_name = 'signup.html'
    if request.method == 'POST':
        f = CustomUserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, 'Account created successfully')
            return redirect('creado')

    else:
        f = CustomUserCreationForm()

    return render(request, 'signup.html', {'form': f})

def creado(request):
	return render(request,
		'creado.html',
		)
