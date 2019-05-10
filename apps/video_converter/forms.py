from django import forms

from .models import QueryHistory


class DownloadForm(forms.ModelForm):
    url = forms.RegexField(
        regex=r'^(https?\:\/\/)?(www\.youtube\.com|youtu\.?be)\/.+$',
        widget=forms.TextInput(attrs={
            'placeholder': 'вставьте ссылку для скачивания'}),
        label=False, required=True, max_length=500)

    class Meta:
        model = QueryHistory
        fields = ('url',)
