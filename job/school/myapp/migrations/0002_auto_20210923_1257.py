# Generated by Django 3.2.7 on 2021-09-23 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='faculty',
            name='email',
            field=models.CharField(default=1, max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='email',
            field=models.CharField(default=1, max_length=40),
            preserve_default=False,
        ),
    ]