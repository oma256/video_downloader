from django.shortcuts import render,redirect
from django.http import JsonResponse

import youtube_dl as yt

from .forms import DownloadForm
from .models import QueryHistory


def redirect_page(request):
    return redirect('video_converter:index')


def index(request):
    if request.method == 'POST':
        form = DownloadForm(request.POST)
        if form.is_valid():
            link = form.cleaned_data.get('link')
            if 'https://www.youtube.com/watch?v=' in link:
                QueryHistory.objects.create(**form.cleaned_data)
                return redirect('video_converter:download')
        return redirect('video_converter:index')
    form = DownloadForm()
    return render(request, 'video_converter/index.html', {'form': form})


def download(request):
    return render(request, 'video_converter/download.html', {})
