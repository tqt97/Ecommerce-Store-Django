# Generated by Django 4.0.5 on 2022-06-18 09:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={},
        ),
        migrations.RenameField(
            model_name='order',
            old_name='created',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='updated',
            new_name='updated_at',
        ),
    ]
