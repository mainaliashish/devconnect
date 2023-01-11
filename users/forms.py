from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'email', 'username', 'password1', 'password2']
        labels = {
            'first_name': 'Name',
        }
        placeholders = {
            'first_name': 'Ram Lama'
        }

    # Override inbuilt classes for from
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        # self.fields['title'].widget.attrs.update({'class': 'input', 'placeholder': 'Enter project title'})
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input input--text'})
