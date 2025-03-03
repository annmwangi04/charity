# Generated by Django 5.1.6 on 2025-03-03 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventapp', '0003_event_date_alter_event_desc_alter_event_img_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cause',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('goal_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('current_amount', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='SuccessStory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('completion_date', models.DateField()),
                ('short_description', models.TextField()),
                ('full_description', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='success_stories/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Success Stories',
            },
        ),
    ]
