# Generated by Django 2.1.7 on 2019-02-17 01:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('q_n_a', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('description', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='qna',
            name='images',
        ),
        migrations.AddField(
            model_name='photo',
            name='qna',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='q_n_a.QNA'),
        ),
    ]
