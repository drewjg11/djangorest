# Generated by Django 3.2.8 on 2021-10-30 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blackbook', '0003_auto_20211030_1250'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='company',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
