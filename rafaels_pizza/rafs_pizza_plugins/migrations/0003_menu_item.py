# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
        ('rafs_pizza_plugins', '0002_auto_20171204_1825'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu_Item',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(primary_key=True, serialize=False, auto_created=True, related_name='rafs_pizza_plugins_menu_item', parent_link=True, to='cms.CMSPlugin')),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='menu_items')),
                ('price', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('url', models.CharField(max_length=200)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
