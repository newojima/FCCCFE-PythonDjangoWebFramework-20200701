# Generated by Django 3.0.7 on 2020-06-30 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('content', models.TextField()),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]