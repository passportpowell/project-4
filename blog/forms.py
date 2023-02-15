from .models import Comment
from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import Event

template_name = 'my_template.html'


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('name', 'description', 'location', 'date_time')


class MyForm(forms.Form):
    my_text_field = forms.CharField(widget=CKEditorWidget())


class CommentForm(forms.ModelForm):
    body = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Comment
        fields = ('body', )
