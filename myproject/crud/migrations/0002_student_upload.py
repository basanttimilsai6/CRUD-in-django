# Generated by Django 3.2.4 on 2021-10-19 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='upload',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]
