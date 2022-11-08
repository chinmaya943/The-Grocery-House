# Generated by Django 4.0.4 on 2022-11-07 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0024_alter_product_supplier_alter_supplier_supplier_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='alertment_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='manufacture_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='purchase_tax_type',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
    ]
