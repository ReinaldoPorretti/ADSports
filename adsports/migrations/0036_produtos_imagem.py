# Generated by Django 3.1.7 on 2021-06-11 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adsports', '0035_auto_20210611_1854'),
    ]

    operations = [
        migrations.AddField(
            model_name='produtos',
            name='imagem',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]