# Generated by Django 4.2.4 on 2023-08-20 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_alter_package_max_member'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='packagefeatures',
            options={'verbose_name_plural': 'Package Details'},
        ),
        migrations.CreateModel(
            name='PackageDiscount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_months', models.PositiveIntegerField(default=0)),
                ('total_discounts', models.PositiveIntegerField(default=0)),
                ('package', models.ManyToManyField(null=True, to='main.package')),
            ],
            options={
                'verbose_name_plural': 'Package Discount',
            },
        ),
    ]
