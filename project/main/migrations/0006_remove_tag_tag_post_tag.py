# Generated by Django 4.1.7 on 2023-02-23 17:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_remove_post_tag_tag_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='tag',
        ),
        migrations.AddField(
            model_name='post',
            name='tag',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.tag'),
        ),
    ]
