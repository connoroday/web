# Generated by Django 2.1.7 on 2019-04-25 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kudos', '0005_token_suppress_sync'),
    ]

    operations = [
        migrations.AddField(
            model_name='token',
            name='override_display_name',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]