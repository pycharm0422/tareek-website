# Generated by Django 3.1 on 2021-05-21 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0003_auto_20210521_0710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='img',
            field=models.ImageField(default='https://images.unsplash.com/photo-1599420186985-5c3d1a038e84?ixid=MnwxMjA3fDB8MHxzZWFyY2h8NHx8aG91c2UlMjBwbGFufGVufDB8fDB8fA%3D%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=600&q=60', upload_to='images/'),
        ),
    ]
