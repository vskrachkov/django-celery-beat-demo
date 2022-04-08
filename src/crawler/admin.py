from django.contrib import admin

from crawler.models import WEBSiteResponse


@admin.register(WEBSiteResponse)
class WEBSiteResponseAdmin(admin.ModelAdmin):
    list_display = ["url", "timestamp"]
