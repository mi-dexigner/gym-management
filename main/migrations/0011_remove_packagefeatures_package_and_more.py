# Generated by Django 4.2.4 on 2023-08-15 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_remove_packagefeatures_package_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='packagefeatures',
            name='package',
        ),
        migrations.AddField(
            model_name='packagefeatures',
            name='package',
            field=models.ManyToManyField(null=True, to='main.package'),
        ),
    ]
