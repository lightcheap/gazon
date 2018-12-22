from django import forms

class imageUploadForm(forms.Form):
    
    imageUpload = forms.ImageField()