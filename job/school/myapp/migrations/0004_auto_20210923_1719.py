# Generated by Django 3.2.7 on 2021-09-23 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20210923_1313'),
    ]

    operations = [
        migrations.AddField(
            model_name='faculty',
            name='user_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='user_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
