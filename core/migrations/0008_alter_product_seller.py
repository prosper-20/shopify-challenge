# Generated by Django 4.0.3 on 2022-05-15 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_comment_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='seller',
            field=models.CharField(max_length=30),
        ),
    ]
