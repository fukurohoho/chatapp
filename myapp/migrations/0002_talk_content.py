# Generated by Django 4.2.1 on 2023-06-20 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Talk_content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_from', models.CharField(max_length=255)),
                ('user_to', models.CharField(max_length=255)),
                ('content', models.CharField(max_length=2048)),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]