from django.db import models

# Create your models here.
class Victim(models.Model):
    ip = models.GenericIPAddressField(blank=False, null=False)
    key = models.CharField(max_length=200, blank=False, null=False)
    sys_information = models.CharField(max_length=300, blank=False, null=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.ip} | {self.id}"
