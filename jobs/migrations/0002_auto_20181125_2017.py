# Generated by Django 2.1rc1 on 2018-11-25 20:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='link',
            field=models.CharField(default=django.utils.timezone.now, max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='job',
            name='status',
            field=models.CharField(choices=[('In Progress', 'In progress'), ('Done', 'Done')], default='Done', max_length=4),
        ),
    ]