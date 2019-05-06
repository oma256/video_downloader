from django import forms


class DownloadForm(forms.Form):
    link = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Введите ссылку для скачивания'}),
        label=False, required=True, max_length=500)
