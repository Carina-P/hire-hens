# Generated by Django 3.2 on 2021-05-28 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0007_alter_orderrentalitem_item_returned'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='postcode',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='order',
            name='street_address2',
            field=models.CharField(blank=True, default='', max_length=80),
        ),
    ]