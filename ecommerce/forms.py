from django import forms
from django.contrib.auth import get_user_model


class ContactForm(forms.Form):
	name = forms.CharField(
		widget=forms.TextInput(
			attrs={
				"class": "form-control",
				"id": "name",
				"placeholder": "Your full name"}))
	email = forms.EmailField(
		widget=forms.EmailInput(
			attrs={
				"class": "form-control",
				"id": "email",
				"placeholder": "Your E-mail Address"}))
	mobile = forms.CharField(
		widget=forms.TextInput(
			attrs={
				"class": "form-control",
				"id": "number",
				"placeholder": "Mobile Number"}))
	subject = forms.CharField(
		widget=forms.TextInput(
			attrs={
				"class": "form-control",
				"id": "subject",
				"placeholder": "Subject"}))
	message = forms.CharField(
		widget=forms.Textarea(
			attrs={
				"class": "form-control",
				"id": "message",
				"placeholder": "Your Message",
				"rows": "5"
			}))


class LoginForm(forms.Form):
	username = forms.CharField(
		widget=forms.TextInput(
			attrs={
				"class": "form-control",
				"id": "username",
				"placeholder": "Your username"}))
	password = forms.CharField(
		widget=forms.PasswordInput(
			attrs={
				"class": "form-control",
				"id": "password",
				"placeholder": "Your password"}))


class RegisterForm(forms.Form):
	first_name = forms.CharField(
		widget=forms.TextInput(
			attrs={
				"class": "form-control",
				"id": "first_name",
				"placeholder": "Your first name"}))
	last_name = forms.CharField(
		widget=forms.TextInput(
			attrs={
				"class": "form-control",
				"id": "last_name",
				"placeholder": "Your last name"}))
	username = forms.CharField(
		widget=forms.TextInput(
			attrs={
				"class": "form-control",
				"id": "username",
				"placeholder": "Your username"}))
	email = forms.EmailField(
		widget=forms.TextInput(
			attrs={
				"class": "form-control",
				"id": "email",
				"placeholder": "Your e-mail"}))
	password = forms.CharField(
		widget=forms.PasswordInput(
			attrs={
				"class": "form-control",
				"id": "password",
				"placeholder": "Your password"}))
	password2 = forms.CharField(
		label='Confirm password',
		widget=forms.PasswordInput(
			attrs={
				"class": "form-control",
				"id": "password2",
				"placeholder": "Confirm password"}))

	class Meta:
		fields = ('username', 'email', 'password')

	def clean_username(self):
		user = get_user_model()
		username = self.cleaned_data.get('username')
		new_username = user.objects.filter(username=username)
		if new_username.exists():
			raise forms.ValidationError("Username is taken")
		return username

	def clean_email(self):
		user = get_user_model()
		email = self.cleaned_data.get('email')
		new_email = user.objects.filter(email=email)
		if new_email.exists():
			raise forms.ValidationError("This Email has already exists")
		return email

	def clean(self):
		data = self.cleaned_data
		password = self.cleaned_data.get('password')
		password2 = self.cleaned_data.get('password2')
		if password != password2:
			raise forms.ValidationError("Passwords must match.")
		return data
