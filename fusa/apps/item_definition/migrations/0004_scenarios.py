# Generated by Django 3.2.8 on 2021-11-08 12:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('item_definition', '0003_alter_function_hara_rationale'),
    ]

    operations = [
        migrations.CreateModel(
            name='Scenarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(choices=[('ANY', 'ANY LOCATION'), ('PRK', 'PARKING'), ('LOW', 'LOW SPEED ROAD'), ('MED', 'MEDIUM SPEED ROAD'), ('HIH', 'HIGH SPEED ROAD'), ('OFF', 'OFF ROAD'), ('INT', 'INTERSECTION'), ('WAS', 'CAR WASH'), ('REM', 'STRANDED'), ('VOT', 'VEHICLE ON TRANSPORT'), ('SER', 'VEHICLE ON SERVICE')], max_length=75)),
                ('function', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scenarios', to='item_definition.function')),
            ],
        ),
    ]
