from django.shortcuts import render, redirect
from django.contrib.auth import login
from accounts.forms import SignupForm
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

@method_decorator(csrf_exempt)

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
        else:
            form = SignupForm()
    else:
        form = SignupForm()
    return render(request, 'accounts/signup.html', {'form': form})