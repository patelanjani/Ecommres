# Generated by Django 3.0 on 2021-04-30 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0018_auto_20210430_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='carts',
            field=models.CharField(default='', max_length=100),
        ),
    ]