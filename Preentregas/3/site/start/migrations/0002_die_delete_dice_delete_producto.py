# Generated by Django 4.2.6 on 2023-10-31 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('start', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Die',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('style', models.CharField(max_length=60)),
                ('faces', models.IntegerField()),
                ('numbering', models.CharField(max_length=40)),
            ],
        ),
        migrations.DeleteModel(
            name='Dice',
        ),
        migrations.DeleteModel(
            name='Producto',
        ),
    ]
