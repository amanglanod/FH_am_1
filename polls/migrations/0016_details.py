# Generated by Django 2.0.5 on 2018-06-13 14:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0015_auto_20180612_0852'),
    ]

    operations = [
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('age', models.IntegerField(default=0)),
                ('nationality', models.CharField(max_length=200)),
                ('experience', models.CharField(max_length=1000)),
                ('anthem', models.FileField(upload_to='candidate_photo')),
                ('socialmedia', models.URLField(default=0)),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Candidate')),
            ],
        ),
    ]
