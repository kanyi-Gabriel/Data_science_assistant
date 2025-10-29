from django import forms
from django.core.files.storage import FileSystemStorage

class UploadFileForm(forms.Form):
    file = forms.FileField()