# Generated by Django 4.2.3 on 2023-07-10 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=32)),
                ('delivery_address', models.CharField(max_length=32)),
                ('delivery_date', models.DateTimeField(auto_now_add=True)),
                ('order_id', models.IntegerField()),
                ('delivery_cost', models.DecimalField(decimal_places=2, default=0.0, max_digits=8)),
            ],
        ),
    ]
