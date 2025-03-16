from django import forms
from .models import Comment

class NewCommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={ 
        'class':'md-textarea',
        'rows':'4',                                     
        'placeholder':'Comment here...',
    }),label='')
    
    class Meta:
        model = Comment
        fields = ['content']
