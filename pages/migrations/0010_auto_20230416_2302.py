# Generated by Django 3.2.12 on 2023-04-16 17:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0009_auto_20230310_2129'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='food',
            name='calcium',
        ),
        migrations.RemoveField(
            model_name='food',
            name='cholesterol',
        ),
        migrations.RemoveField(
            model_name='food',
            name='dietaryfiber',
        ),
        migrations.RemoveField(
            model_name='food',
            name='iron',
        ),
        migrations.RemoveField(
            model_name='food',
            name='magnesium',
        ),
        migrations.RemoveField(
            model_name='food',
            name='potassium',
        ),
        migrations.RemoveField(
            model_name='food',
            name='sodium',
        ),
        migrations.RemoveField(
            model_name='food',
            name='sugar',
        ),
    ]
