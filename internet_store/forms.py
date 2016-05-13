from django import forms
from .models import User


class UserForm(forms.Form):
    user_name = forms.CharField(label='User name', max_length=100)

    class Meta:
        model = User
        fields = '__all__'

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if email and User.objects.filter(email=email).count():
            raise forms.ValidationError(
                "This email address is already in use. Please supply a different email address.")
        return email
