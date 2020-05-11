from django import forms

from file_catalog.models import File

class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ('description', 'my_file')
         