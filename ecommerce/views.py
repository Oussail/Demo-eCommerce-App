from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm, LoginForm, RegisterForm


def index(request):
	return render(request, "index.html", {})


def login_auth(request):
	form = LoginForm(request.POST or None)
	context = {
		"form": form
	}
	if form.is_valid():
		username = form.cleaned_data.get('username')
		password = form.cleaned_data.get('password')
		user = authenticate(request, username=username, password=password)
		if user is not None:
			print(request.user.is_authenticated)
			login(request, user)
			print(request.user.is_authenticated)
			# context['form'] = LoginForm()
			return redirect("/")
		else:
			print('error')
	return render(request, "auth/login.html", context)


def register(request):
	user = get_user_model()
	form = RegisterForm(request.POST or None)
	context = {
		"form": form
	}
	if form.is_valid():
		first_name = form.cleaned_data.get('first_name')
		last_name = form.cleaned_data.get('last_name')
		username = form.cleaned_data.get('username')
		email = form.cleaned_data.get('email')
		password = form.cleaned_data.get('password')
		new_user = user.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
		new_user.save()
	return render(request, "auth/register.html", context)


def contact(request):
	if request.method == "POST":
		contact_form = ContactForm(request.POST)
		if contact_form.is_valid():
			return HttpResponseRedirect('/thanks/')
	else:
		contact_form = ContactForm(auto_id=False)
		context = {
			"form": contact_form
		}
		return render(request, "contact/view.html", context)


def thanks(request):
	return render(request, "thanks.html", {})
