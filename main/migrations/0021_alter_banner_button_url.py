# Generated by Django 4.2.4 on 2023-09-02 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_alter_banner_options_remove_banner_alt_text_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='button_url',
            field=models.CharField(max_length=200),
        ),
    ]