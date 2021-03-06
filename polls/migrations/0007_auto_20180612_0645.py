# Generated by Django 2.0.5 on 2018-06-12 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_auto_20180611_1752'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='birth',
            field=models.DateField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='candidate',
            name='country',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='candidate',
            name='job',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='candidate',
            name='quote',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
    ]
