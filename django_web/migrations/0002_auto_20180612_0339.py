# Generated by Django 2.0.6 on 2018-06-12 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DjangoWebProductmessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(blank=True, null=True)),
                ('img_url', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'django_web_productmessage',
            },
        ),
        migrations.DeleteModel(
            name='ProductMessage',
        ),
    ]
