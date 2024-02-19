# Generated by Django 4.2.10 on 2024-02-18 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='id',
        ),
        migrations.AddField(
            model_name='product',
            name='Image',
            field=models.ImageField(null=True, upload_to='product_image'),
        ),
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(default=2),
            preserve_default=False,
        ),
    ]
