# Generated by Django 4.1.5 on 2023-02-04 02:20

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person_name', models.CharField(max_length=20)),
                ('person_age', models.CharField(max_length=3)),
                ('person_phone', models.CharField(max_length=10)),
                ('person_desc', tinymce.models.HTMLField()),
            ],
        ),
    ]