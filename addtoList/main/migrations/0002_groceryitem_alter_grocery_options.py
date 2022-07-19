# Generated by Django 4.0.6 on 2022-07-19 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroceryItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.AlterModelOptions(
            name='grocery',
            options={'verbose_name': 'Grocery', 'verbose_name_plural': 'Groceries'},
        ),
    ]
