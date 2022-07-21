# Generated by Django 4.0.6 on 2022-07-21 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_grocery_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grocery',
            name='category',
            field=models.CharField(choices=[('🍓Fruits', 'Fruits'), ('🥒Vegetables', 'Vegetables'), ('🥫Canned Goods', 'Canned Goods'), ('🥛Dairy', 'Dairy'), ('🥩Meat', 'Meat'), ('🐟Fish & Seafood', 'Seafood'), ('🧂Condiments and Spices', 'Condiments'), ('🍟Snacks', 'Snacks'), ('🍞Baked Goods', 'Baked Goods'), ('🧃Beverages', 'Beverages'), ('🍝Pasta', 'Pasta And Rice'), ('🥚Baking Products', 'Baking Products'), ('🍗Frozen Food', 'Frozen Food'), ('🚼Baby Items', 'Baby Items'), ('🐕Pet Care', 'Pet Care'), ('Miscellaneous', 'Miscellaneous')], default='blank', max_length=200),
        ),
    ]
