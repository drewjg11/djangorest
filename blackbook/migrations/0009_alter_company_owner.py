# Generated by Django 3.2.8 on 2021-11-08 12:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blackbook', '0008_company_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='owner',
            field=models.CharField(default=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL), max_length=50),
        ),
    ]
