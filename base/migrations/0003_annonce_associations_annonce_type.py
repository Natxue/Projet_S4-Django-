# Generated by Django 4.0.3 on 2022-03-16 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_annonce_prix_annonce_utilisateur_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='annonce',
            name='associations',
            field=models.ManyToManyField(blank=True, default=None, to='base.annonce'),
        ),
        migrations.AddField(
            model_name='annonce',
            name='type',
            field=models.IntegerField(default=0),
        ),
    ]
