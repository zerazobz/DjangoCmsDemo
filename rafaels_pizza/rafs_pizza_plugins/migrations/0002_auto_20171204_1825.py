# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rafs_pizza_plugins', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='daily_specials',
            options={'verbose_name': 'Daily Special', 'verbose_name_plural': 'Daily Specials'},
        ),
        migrations.AlterField(
            model_name='daily_specials',
            name='image',
            field=models.ImageField(upload_to='daily_specials'),
        ),
    ]
