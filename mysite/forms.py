from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
#UserCreationForm
#It has three fields: username (from the user model), password1, and password2.
#It verifies that password1 and password2 match, validates the password using validate_password(),
#and sets the user’s password using set_password().


class UserCreateForm(UserCreationForm):

    class Meta:
        fields=('username','email','password1','password2')
        model=User
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['username'].label = 'Display Name'
        self.fields['email'].label = "Email Address"
        self.fields['password1'].label = "Password"
        #self.fields['password2'].label = "Confirm Password"
