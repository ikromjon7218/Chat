from django.db import models

class Xabar(models.Model):
    matn = models.CharField(max_length=500)
    sana = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.matn[:10]}"

