# Generated by Django 3.0 on 2021-04-23 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_product_product_dec'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='status',
            field=models.CharField(default='inactive', max_length=100),
        ),
    ]