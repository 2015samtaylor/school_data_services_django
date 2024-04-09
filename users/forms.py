from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    #additional fields added to UserCreationForm
    #inheriting the template
    email = forms.EmailField()

    class Meta:
        #specifying the model we want this form to interact with
        #When this form validates it is going to create a new user
        #nested namespace for configs. We are saying the user model 
        #will occur the saves. Form.save() saves to the model
        model = User
        fields = ['username', 'email', 'password1', 'password2']

        #now we can use this instead of UserCreationForm

