# Generated by Django 3.2 on 2021-06-02 11:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_comment_created_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='name',
            new_name='author',
        ),
    ]