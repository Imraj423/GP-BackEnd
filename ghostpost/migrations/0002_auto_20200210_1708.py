# Generated by Django 3.0.3 on 2020-02-10 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ghostpost', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ghostpost',
            name='downvote',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='ghostpost',
            name='message',
            field=models.CharField(default=0, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ghostpost',
            name='upvote',
            field=models.IntegerField(default=0),
        ),
    ]
