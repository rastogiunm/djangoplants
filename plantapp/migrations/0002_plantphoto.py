# Generated by Django 2.0.1 on 2018-01-18 20:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plantapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlantPhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.CharField(max_length=200)),
                ('plant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='plantapp.Plant')),
            ],
        ),
    ]
