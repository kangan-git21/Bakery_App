# Generated by Django 4.1 on 2022-08-09 08:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bakery', '0004_loginuser'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ingredient',
            old_name='Price',
            new_name='cost_price',
        ),
        migrations.RenameField(
            model_name='ingredient',
            old_name='Name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='ingredient',
            old_name='Quantity',
            new_name='quantity',
        ),
        migrations.RemoveField(
            model_name='item',
            name='ingredients',
        ),
        migrations.AddField(
            model_name='item',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='Requirements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('need_quantity', models.IntegerField(default=0)),
                ('item_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bakery.item')),
                ('need_ingredients', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bakery.ingredient')),
            ],
        ),
    ]
