from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

# Create your views here.
from users.forms import CustomUserCreationForm, CustomUserChangeForm

def login_user(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request, ('Logged in!'))
			return redirect('main-urls:home')

		else:
			messages.success(request, ('Error. Please try again'))
			return redirect('main-urls:login')
	else:
		return render(request, 'users/login.html', {})


def logout_user(request):
	logout(request)
	messages.success(request, ('Logged out!'))
	return redirect('main-urls:home')


def register_user(request):
	if request.method == 'POST':
		form = CustomUserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, ('Yay! You have registered'))
			return redirect('main-urls:home')
	else:
		form = CustomUserCreationForm()

	context = {'form': form}
	return render(request, 'users/register.html', context)


def edit_profile(request):
	if request.method == 'POST':
		form = CustomUserChangeForm(request.POST, instance=request.user)
		if form.is_valid():
			form.save()
			messages.success(request, ('Wohoo! You have successfully edited your profile'))
			return redirect('main-urls:home')
	else:
		form = CustomUserChangeForm(instance=request.user)

	context = {'form': form}
	return render(request, 'users/edit_profile.html', context)
