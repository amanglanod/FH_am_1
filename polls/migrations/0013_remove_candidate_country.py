# Generated by Django 2.0.5 on 2018-06-12 06:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0012_auto_20180612_0655'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidate',
            name='country',
        ),
    ]
