# Generated by Django 3.2.12 on 2023-03-10 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0007_alter_foodlog_food_entry_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='sodium',
            field=models.IntegerField(default=0),
        ),
    ]
