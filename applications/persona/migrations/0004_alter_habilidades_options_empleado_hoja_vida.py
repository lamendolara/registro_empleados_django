# Generated by Django 4.1.7 on 2023-03-17 08:15

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0003_empleado_avatar_empleado_habilidades'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='habilidades',
            options={'verbose_name': 'Habilidad', 'verbose_name_plural': 'Habilidades'},
        ),
        migrations.AddField(
            model_name='empleado',
            name='hoja_vida',
            field=ckeditor.fields.RichTextField(default='texto'),
            preserve_default=False,
        ),
    ]
