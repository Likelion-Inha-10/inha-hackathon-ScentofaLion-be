# Generated by Django 4.0.6 on 2022-07-24 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='pay_price',
            field=models.IntegerField(),
        ),
    ]