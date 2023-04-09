# Generated by Django 3.2.12 on 2023-03-10 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0008_food_sodium'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='calcium',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=7),
        ),
        migrations.AddField(
            model_name='food',
            name='cholesterol',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=7),
        ),
        migrations.AddField(
            model_name='food',
            name='dietaryfiber',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=7),
        ),
        migrations.AddField(
            model_name='food',
            name='iron',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=7),
        ),
        migrations.AddField(
            model_name='food',
            name='magnesium',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=7),
        ),
        migrations.AddField(
            model_name='food',
            name='potassium',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=7),
        ),
        migrations.AddField(
            model_name='food',
            name='sugar',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=7),
        ),
        migrations.AlterField(
            model_name='food',
            name='sodium',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=7),
        ),
    ]