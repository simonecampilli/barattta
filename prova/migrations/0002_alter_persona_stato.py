# Generated by Django 4.1.7 on 2023-03-31 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prova', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='stato',
            field=models.CharField(choices=[('S', 'Single'), ('I', 'Impegnato'), ('O', 'Occupato')], max_length=1),
        ),
    ]