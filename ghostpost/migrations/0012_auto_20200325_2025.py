# Generated by Django 3.0.4 on 2020-03-25 20:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ghostpost', '0011_ghostpost_is_boast'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ghostpost',
            old_name='dislike',
            new_name='downvote',
        ),
        migrations.RenameField(
            model_name='ghostpost',
            old_name='like',
            new_name='upvote',
        ),
    ]
