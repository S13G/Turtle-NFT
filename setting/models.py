from django.db import models

# Create your models here.

class Settings(models.Model):
    logo = models.ImageField(default='default.png')
    trade_mark = models.CharField(max_length=255, default='TURTLE NFT')
    title = models.CharField(max_length=1000, default="The #1 source for NFT lookup")
    slogan = models.TextField(default="Your best choice when you're on the lookup for NFTs.")

    def __str__(self) -> str:
        return 'Edit Settings'

    class Meta:
        verbose_name = 'Setting'
