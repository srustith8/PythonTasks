# Generated by Django 3.2.2 on 2021-05-18 09:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.CharField(max_length=9, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('rule', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='channels', to='inlineapp.rule')),
            ],
        ),
    ]
