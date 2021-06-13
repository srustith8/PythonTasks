# Generated by Django 3.2 on 2021-05-13 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orm_app', '0002_article'),
    ]

    operations = [
        migrations.CreateModel(
            name='TempUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'temp_user',
                'managed': False,
            },
        ),
    ]