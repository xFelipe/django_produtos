# Generated by Django 5.0.1 on 2024-02-03 19:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='nome',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='preco',
            new_name='price',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='estoque',
            new_name='stock',
        ),
    ]
