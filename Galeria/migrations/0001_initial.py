# Generated by Django 4.0.3 on 2022-05-13 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Galeria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=50)),
                ('fecha', models.DateField(auto_now_add=True)),
                ('album', models.CharField(max_length=50)),
                ('imagen', models.ImageField(upload_to='')),
            ],
            options={
                'verbose_name': 'nombre',
                'verbose_name_plural': 'nombres',
            },
        ),
    ]