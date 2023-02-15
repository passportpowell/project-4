from django.contrib import admin
from .models import Event
from django import forms
from ckeditor.widgets import CKEditorWidget

# Define a custom form for the Event model


class EventForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Event
        fields = '__all__'

# Define a custom ModelAdmin class for the Event model


class EventAdmin(admin.ModelAdmin):
    form = EventForm


# Register the Event model with the custom ModelAdmin
admin.site.register(Event, EventAdmin)
