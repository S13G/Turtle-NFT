from django.db import models

# Create your models here.

class Settings(models.Model):
    logo = models.ImageField(default='default.png')
    trade_mark = models.CharField(max_length=255, default='TURTLE NFT')
    slogan = models.TextField()

    def __str__(self) -> str:
        return 'Edit Settings'

    class Meta:
        verbose_name = 'Setting'
