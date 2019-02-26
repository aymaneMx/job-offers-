from django.db import models


class Offer(models.Model):
    title = models.CharField(max_length=32)
    description = models.TextField()
    skills_list = models.TextField(default='django, doker , graghQl')
    creation_date = models.DateField(auto_now_add=True)
    modification_date = models.DateField(auto_now=True)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


