# Generated by Django 4.1.2 on 2022-10-05 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_alter_category_options_rename_title_category_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='default.png', null=True, upload_to=''),
        ),
    ]
