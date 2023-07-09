

from django import forms
class DocumentUploadForm(forms.Form):
    document = forms.FileField(label='',widget=forms.FileInput(attrs={
            'class': 'form-control',
            'id': 'inputGroupFile04',
            'aria-describedby': 'inputGroupFileAddon04',
            'aria-label': 'Upload',
            
        })
    )
