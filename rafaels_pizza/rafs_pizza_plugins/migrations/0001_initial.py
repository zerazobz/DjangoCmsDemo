# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
    ]

    operations = [
        migrations.CreateModel(
            name='Daily_Specials',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(primary_key=True, serialize=False, auto_created=True, related_name='rafs_pizza_plugins_daily_specials', parent_link=True, to='cms.CMSPlugin')),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='daily_specails')),
                ('description', models.TextField()),
                ('url', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': ('Daily Special',),
                'verbose_name_plural': 'Daily Specials',
            },
            bases=('cms.cmsplugin',),
        ),
    ]
