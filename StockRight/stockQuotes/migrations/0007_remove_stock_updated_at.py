# Generated by Django 3.0.4 on 2020-04-01 05:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stockQuotes', '0006_auto_20200331_2344'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock',
            name='updated_at',
        ),
    ]
