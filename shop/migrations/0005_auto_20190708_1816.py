# Generated by Django 2.2.2 on 2019-07-08 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_orders'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orders',
            old_name='adress',
            new_name='address',
        ),
        migrations.AddField(
            model_name='orders',
            name='phone',
            field=models.CharField(default='3654725498', max_length=111),
        ),
    ]
