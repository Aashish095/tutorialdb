# Generated by Django 3.2.21 on 2023-10-01 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20190829_1937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='tags',
            field=models.ManyToManyField(to='app.Tag'),
        ),
    ]
