# Generated by Django 3.2.6 on 2021-08-26 22:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0007_categoria_usuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='livros',
            name='data_devolucao',
        ),
        migrations.RemoveField(
            model_name='livros',
            name='data_emprestimo',
        ),
        migrations.RemoveField(
            model_name='livros',
            name='nome_emprestado',
        ),
        migrations.RemoveField(
            model_name='livros',
            name='tempo_duracao',
        ),
        migrations.CreateModel(
            name='Emprestimos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_emprestado', models.CharField(blank=True, max_length=30, null=True)),
                ('data_emprestimo', models.DateTimeField(blank=True, null=True)),
                ('data_devolucao', models.DateTimeField(blank=True, null=True)),
                ('tempo_duracao', models.DateField(blank=True, null=True)),
                ('livro', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='livro.livros')),
            ],
        ),
    ]
  