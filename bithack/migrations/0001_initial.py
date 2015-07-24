# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Hacker',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('school', models.CharField(max_length=256)),
                ('tshirt_size', models.CharField(max_length=30, choices=[(b'extra small', b'Adult Extra Small'), (b'small', b'Adult Small'), (b'medium', b'Adult Medium'), (b'large', b'Adult Large'), (b'extra large', b'Adult Extra Large')])),
                ('vegetarian', models.BooleanField(default=False)),
                ('source', models.CharField(max_length=256)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
