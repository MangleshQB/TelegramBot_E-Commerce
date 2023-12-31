# Generated by Django 4.2.3 on 2023-07-26 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0008_alter_customuser_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='first_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='last_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='password',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
