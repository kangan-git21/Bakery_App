# Generated by Django 4.1 on 2022-08-09 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bakery', '0003_remove_item_ingredients_item_ingredients'),
    ]

    operations = [
        migrations.CreateModel(
            name='LoginUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=150)),
                ('password', models.CharField(max_length=120)),
            ],
        ),
    ]