# Generated by Django 5.1 on 2024-09-10 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='book_image',
            field=models.ImageField(default='', upload_to='images'), 
        ),
    ]
