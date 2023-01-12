from django.forms import ModelForm
from django import forms
from .models import Project, Review

# Model form binding for the project


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'featured_image', 'description', 'demo_link',
                  'source_link', 'tags']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        # self.fields['title'].widget.attrs.update({'class': 'input', 'placeholder': 'Enter project title'})
        for name,field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['value', 'message']
        labels = {
            'value': 'Place your vote',
            'message' : 'Add a comment with your vote'
        }

    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)
        # self.fields['title'].widget.attrs.update({'class': 'input', 'placeholder': 'Enter project title'})
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})
