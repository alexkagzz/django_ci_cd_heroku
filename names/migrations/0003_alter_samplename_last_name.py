# Generated by Django 3.2.5 on 2021-08-02 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('names', '0002_rename_samplenames_samplename'),
    ]

    operations = [
        migrations.AlterField(
            model_name='samplename', name='last_name', field=models.CharField(
                help_text='Enter your last name', max_length=50),), ]