# Generated by Django 4.0.5 on 2022-11-26 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('design', '0003_delete_design_desc_design_model_date_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='design_model',
            name='content',
            field=models.TextField(null=True),
        ),
    ]
