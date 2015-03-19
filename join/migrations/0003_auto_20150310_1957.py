# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('join', '0002_auto_20150310_1409'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='join',
            name='zip_code',
        ),
        migrations.AlterField(
            model_name='join',
            name='email',
            field=models.EmailField(unique=True, max_length=75, error_messages={b'unique': b'\xd0\xa2\xd0\xb0\xd0\xbd\xd1\x8b \xd1\x85\xd0\xb0\xd1\x8f\xd0\xb3 \xd1\x83\xd1\x80\xd1\x8c\xd0\xb4 \xd0\xbd\xd1\x8c \xd0\xb1\xd2\xaf\xd1\x80\xd1\x82\xd0\xb3\xd1\x8d\xd0\xb3\xd0\xb4\xd1\x81\xd1\x8d\xd0\xbd \xd0\xb1\xd0\xb0\xd0\xb9\xd0\xbd\xd0\xb0.'}),
            preserve_default=True,
        ),
    ]
