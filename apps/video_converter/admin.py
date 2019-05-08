from django.contrib import admin

from .models import QueryHistory


class QueryHistoryAdmin(admin.ModelAdmin):
    list_display = ('url', 'query_date')


admin.site.register(QueryHistory, QueryHistoryAdmin)
