# Generated by Django 4.2.3 on 2023-07-25 23:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articulo', '0007_remove_comentario_usuarios_comentario_author_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=100)),
                ('text', models.TextField()),
                ('fecha_publicacion', models.DateTimeField(auto_now_add=True)),
                ('articulo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comentario', to='articulo.articulo')),
            ],
        ),
        migrations.DeleteModel(
            name='Comentario',
        ),
    ]
