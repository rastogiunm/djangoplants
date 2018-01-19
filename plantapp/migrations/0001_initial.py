# Generated by Django 2.0.1 on 2018-01-13 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SpeciesId', models.IntegerField()),
                ('Name', models.CharField(max_length=500)),
                ('Family', models.TextField(blank=True)),
                ('ScientificName', models.TextField(blank=True)),
                ('Synonyms', models.TextField(blank=True)),
                ('VernacularName', models.TextField(blank=True)),
                ('REDCode', models.TextField(blank=True)),
                ('Description', models.TextField(blank=True)),
                ('CreatedDate', models.DateTimeField(auto_now_add=True)),
                ('UpdateDate', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
