# Generated by Django 4.0.1 on 2022-03-23 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0038_merge_20220323_1156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='following',
            field=models.ManyToManyField(blank=True, related_name='following_profile', to='base.Profile'),
        ),
    ]
