# Generated by Django 2.2 on 2020-12-08 00:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('total_time', models.CharField(max_length=200)),
                ('image', models.ImageField(default='recipe.jpg', upload_to='recipe_pics')),
                ('ingredients', models.TextField()),
                ('instructions', models.TextField()),
                ('notes', models.TextField()),
                ('user_name', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]