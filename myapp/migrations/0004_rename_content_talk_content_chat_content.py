# Generated by Django 4.2.1 on 2023-06-26 09:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_content_alter_talk_content_content'),
    ]

    operations = [
        migrations.RenameField(
            model_name='talk_content',
            old_name='content',
            new_name='chat_content',
        ),
    ]
