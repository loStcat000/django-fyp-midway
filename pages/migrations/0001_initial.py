# Generated by Django 3.2.12 on 2023-02-14 10:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_name', models.CharField(max_length=200)),
                ('quantity', models.DecimalField(decimal_places=2, default=100.0, max_digits=7)),
                ('calories', models.IntegerField(default=0)),
                ('fat', models.DecimalField(decimal_places=2, max_digits=7)),
                ('carbohydrates', models.DecimalField(decimal_places=2, max_digits=7)),
                ('protein', models.DecimalField(decimal_places=2, max_digits=7)),
            ],
        ),
        migrations.CreateModel(
            name='FoodCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Food Category',
                'verbose_name_plural': 'Food Categories',
            },
        ),
        migrations.CreateModel(
            name='Weight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.DecimalField(decimal_places=2, max_digits=7)),
                ('entry_date', models.DateField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Weight',
                'verbose_name_plural': 'Weight',
            },
        ),
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=100)),
                ('birthday', models.DateField()),
                ('age', models.IntegerField()),
                ('height', models.DecimalField(decimal_places=2, max_digits=5)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=5)),
                ('activitylevel', models.CharField(choices=[('1', 'Sedentary (little to no exercise + work a desk job) '), ('2', 'Lightly Active : (light exercise 1-3 days / week)'), ('3', 'Moderately Active : (moderate exercise 3-5 days / week)'), ('4', 'Very Active : (heavy exercise 6-7 days / week)'), ('5', 'Extremely Active: (very heavy exercise, hard labor job, training 2x / day)')], max_length=100)),
                ('user', models.ForeignKey(default='DEFAULT VALUE', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='get_images', to='pages.food')),
            ],
        ),
        migrations.CreateModel(
            name='FoodLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_entry_date', models.DateField(default=django.utils.timezone.now)),
                ('food_consumed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.food')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Food Log',
                'verbose_name_plural': 'Food Log',
            },
        ),
        migrations.AddField(
            model_name='food',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='food_category', to='pages.foodcategory'),
        ),
    ]