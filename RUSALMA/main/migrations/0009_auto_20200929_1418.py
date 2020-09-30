# Generated by Django 3.1.1 on 2020-09-29 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_portfolio'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='direction',
            field=models.CharField(choices=[('веб-разработка', 'веб-разработка'), ('интернет-маркетинг', 'интернет-маркетинг')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='link',
            field=models.CharField(max_length=255, null=True, verbose_name='Ссылка'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='tag',
            field=models.ManyToManyField(blank=True, to='main.Tag', verbose_name='Тег'),
        ),
    ]