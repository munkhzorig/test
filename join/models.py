# encoding=utf8
from django.db import models

class Join(models.Model):
    email = models.EmailField(unique=True, error_messages = {'unique': 'Таны хаяг урьд нь бүртгэгдсэн байна.'})
    full_name = models.CharField(max_length=250, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __unicode__(self):
        return self.email
