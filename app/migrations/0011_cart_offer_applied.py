# Generated by Django 4.0.4 on 2022-09-21 17:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_tax_alter_coupon_valid_to_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='offer_applied',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.coupon'),
        ),
    ]
