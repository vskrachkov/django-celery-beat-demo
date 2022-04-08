from django.db import models


class WEBSiteResponse(models.Model):
    url = models.URLField(max_length=500)
    body = models.TextField()
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"<{self.__class__.__name__}: {self.url}>"
