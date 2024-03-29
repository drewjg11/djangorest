# Generated by Django 3.2.8 on 2021-10-30 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blackbook', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='category',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='facebook',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='instagram',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='website',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='industry',
            field=models.CharField(default='', max_length=25),
        ),
    ]
