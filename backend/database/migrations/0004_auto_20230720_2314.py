# Generated by Django 3.2.20 on 2023-07-20 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0003_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='name',
            field=models.CharField(max_length=26),
        ),
        migrations.AlterField(
            model_name='link',
            name='source',
            field=models.CharField(max_length=26),
        ),
        migrations.AlterField(
            model_name='link',
            name='target',
            field=models.CharField(max_length=26),
        ),
    ]
