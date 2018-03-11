from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import ContactForm


def index(request):
	return render(request, "index.html", {})


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
