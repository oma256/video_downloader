from django.shortcuts import render,redirect
from django.http import JsonResponse

from .forms import DownloadForm
from .models import QueryHistory


def index(request):
    if request.method == 'POST':
        form = DownloadForm(request.POST)
        if form.is_valid():
            QueryHistory.objects.create(**form.cleaned_data)
            return redirect('video_converter:index')
    form = DownloadForm()
    return render(request, 'video_converter/index.html', {'form': form})
