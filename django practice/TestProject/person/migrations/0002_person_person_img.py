# Generated by Django 4.1.5 on 2023-02-12 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='person_img',
            field=models.FileField(default=None, max_length=250, null=True, upload_to='person/'),
        ),
    ]
