# Generated by Django 2.0.5 on 2018-06-12 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0011_auto_20180612_0653'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='country',
            field=models.CharField(default='The World', max_length=20),
        ),
        migrations.AddField(
            model_name='candidate',
            name='quote',
            field=models.CharField(default='Hello', max_length=200),
        ),
    ]
