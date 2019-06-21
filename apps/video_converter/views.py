from django.shortcuts import render
from django.http import HttpResponsePermanentRedirect

import youtube_dl

from .forms import DownloadForm


def index(request):
    if request.method == 'POST':
        form = DownloadForm(request.POST)
        if form.is_valid():
                url = form.cleaned_data.get('url')
                options = {
                    'outtmpl': '%(title)s-%(id)s.%(ext)s',
                    'format': 'best'
                }
                with youtube_dl.YoutubeDL(options) as ydl:
                    r = ydl.extract_info(url, download=False)
                    video_url = r['url']
                    form.save()
                    file_name = 'video.mp4'
                    r = HttpResponsePermanentRedirect(video_url)
                    r['Content-Type'] = 'application/force-download'
                    r['Content-Disposition'] = f'attachment; filename={file_name}'

                    return r

        return render(request, 'video_converter/index.html', {'form': form})
    form = DownloadForm()
    return render(request, 'video_converter/index.html', {'form': form})



