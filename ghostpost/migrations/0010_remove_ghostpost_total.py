# Generated by Django 3.0.3 on 2020-02-11 00:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ghostpost', '0009_ghostpost_total'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ghostpost',
            name='total',
        ),
    ]