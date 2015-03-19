# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('join', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='join',
            name='zip_code',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='join',
            name='email',
            field=models.EmailField(max_length=250),
            preserve_default=True,
        ),
    ]
