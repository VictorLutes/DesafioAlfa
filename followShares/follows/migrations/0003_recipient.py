# Generated by Django 4.1.3 on 2022-11-18 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('follows', '0002_stock_currentprice_stock_timecreated'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(default='victorclutes@gmail.com', max_length=30)),
            ],
        ),
    ]
