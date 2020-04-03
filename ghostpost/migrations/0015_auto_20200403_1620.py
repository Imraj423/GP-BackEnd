# Generated by Django 3.0.3 on 2020-04-03 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ghostpost', '0014_auto_20200403_1540'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ghostpost',
            name='num_vote_down',
        ),
        migrations.RemoveField(
            model_name='ghostpost',
            name='num_vote_up',
        ),
        migrations.RemoveField(
            model_name='ghostpost',
            name='vote_score',
        ),
        migrations.AddField(
            model_name='ghostpost',
            name='secret_id',
            field=models.CharField(default=None, max_length=6, null=True),
        ),
    ]