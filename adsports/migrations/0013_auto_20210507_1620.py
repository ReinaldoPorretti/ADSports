# Generated by Django 3.1.7 on 2021-05-07 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adsports', '0012_administradores'),
    ]

    operations = [
        migrations.AlterField(
            model_name='administradores',
            name='cpf',
            field=models.CharField(max_length=50),
        ),
    ]
