# Generated by Django 5.0.3 on 2024-04-09 10:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_rename_tags_post_tag'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='tag',
            new_name='tags',
        ),
    ]
