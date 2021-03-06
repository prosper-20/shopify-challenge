# Generated by Django 4.0.3 on 2022-05-18 08:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_product_specifications'),
    ]

    operations = [
        migrations.CreateModel(
            name='Warehouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(choices=[('1', 'AFRICA'), ('2', 'EUROPE'), ('3', 'AUSTRALIA'), ('4', 'SOUTH AMERICA'), ('5', 'OTHER')], max_length=20)),
                ('date_stored', models.DateTimeField(default=django.utils.timezone.now)),
                ('item', models.ManyToManyField(related_name='warehouse_item', to='core.product')),
            ],
        ),
    ]
