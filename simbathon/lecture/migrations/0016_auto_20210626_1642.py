# Generated by Django 3.2.4 on 2021-06-26 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lecture', '0015_auto_20210626_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecture',
            name='category',
            field=models.CharField(choices=[('python', '파이썬'), ('ozobot', '오조봇'), ('entry', '엔트리'), ('goorum', '구름'), ('etc', '기타')], default='', max_length=20),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
