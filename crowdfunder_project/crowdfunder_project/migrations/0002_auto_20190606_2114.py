# Generated by Django 2.2.2 on 2019-06-06 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crowdfunder_project', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='owner',
            field=models.CharField(max_length=255),
        ),
        migrations.DeleteModel(
            name='Owner',
        ),
    ]