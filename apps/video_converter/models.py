from django.db import models


class QueryHistory(models.Model):
    url = models.URLField(max_length=500, verbose_name='video link')
    query_date = models.DateTimeField(auto_now_add=True,
                                      verbose_name='query date')

    def __str__(self):
        return self.url
