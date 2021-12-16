# Generated by Django 3.2.8 on 2021-10-19 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='login_method',
            field=models.CharField(choices=[('kakao', 'Kakao'), ('naver', 'Naver'), ('google', 'Google')], default='kakao', max_length=50),
        ),
    ]