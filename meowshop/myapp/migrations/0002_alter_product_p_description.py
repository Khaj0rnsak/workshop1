# Generated by Django 4.0.5 on 2022-06-07 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='p_description',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
    ]
