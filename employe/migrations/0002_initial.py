# Generated by Django 4.2.20 on 2025-04-18 08:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employe', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='personnel',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='paie',
            name='personnel',
            field=models.ManyToManyField(related_name='details_paie', through='employe.FichePaie', to='employe.personnel'),
        ),
        migrations.AddField(
            model_name='fichepaie',
            name='paie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employe.paie'),
        ),
        migrations.AddField(
            model_name='fichepaie',
            name='personnel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employe.personnel'),
        ),
        migrations.AddField(
            model_name='credit',
            name='paie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employe.paie'),
        ),
        migrations.AddField(
            model_name='credit',
            name='personnel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employe.personnel'),
        ),
        migrations.AddField(
            model_name='absence',
            name='fichePaie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employe.fichepaie'),
        ),
    ]
