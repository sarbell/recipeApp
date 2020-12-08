# Generated by Django 2.2 on 2020-12-08 01:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recipeApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cookbook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=200)),
                ('book_description', models.TextField()),
                ('user_name', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='recipe',
            name='cookbook_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='recipeApp.Cookbook'),
        ),
    ]
