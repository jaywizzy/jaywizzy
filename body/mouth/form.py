from django import forms
from . models import Post
from . models import UserLogin


class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = [
			"title",
			"content"
		]


class LoginForm(forms.Form):
   username = forms.CharField(max_length = 100)
   password = forms.CharField(widget = forms.PasswordInput())

   def clean_message(self):
      username = self.cleaned_data.get("username")
      dbuser = UserLogin.objects.filter(name = username)
      
      if not dbuser:
         raise forms.ValidationError("User does not exist in our db!")
      return username