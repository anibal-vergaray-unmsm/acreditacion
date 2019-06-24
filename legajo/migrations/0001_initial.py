# Generated by Django 2.2.1 on 2019-06-24 20:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DOCENTE',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DOC_COD', models.CharField(max_length=8, unique=True, verbose_name='Código')),
                ('DOC_DNI', models.CharField(max_length=10, unique=True, verbose_name='DNI')),
                ('DOC_CELU', models.CharField(max_length=10, unique=True, verbose_name='Celular')),
                ('DOC_EMAIL', models.CharField(max_length=50, unique=True, verbose_name='Email')),
                ('DOC_NOMBRE', models.CharField(max_length=50, verbose_name='Nombre')),
                ('DOC_APE', models.CharField(max_length=50, verbose_name='Apellido')),
                ('DOC_SEXO', models.CharField(max_length=15, verbose_name='Sexo')),
                ('DOC_NAC', models.DateField(verbose_name='Fecha de Nacimiento')),
                ('DOC_ESTADO', models.CharField(max_length=30, verbose_name='Estado')),
            ],
        ),
        migrations.CreateModel(
            name='ENTIDAD',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ENT_NOMBRE', models.CharField(max_length=100, verbose_name='Entidad')),
                ('ENT_SECTOR', models.CharField(max_length=15, verbose_name='Sector')),
                ('ENT_RUBRO', models.CharField(blank=True, max_length=80, verbose_name='Rubro')),
            ],
        ),
        migrations.CreateModel(
            name='INSTITUCION',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('INSTI_NOMBRE', models.CharField(max_length=150, verbose_name='Institución')),
                ('INSTI_PAIS', models.CharField(max_length=60, verbose_name='País')),
                ('INSTI_TIPO', models.CharField(max_length=40, verbose_name='Tipo de Institución')),
            ],
        ),
        migrations.CreateModel(
            name='RESOLUCION',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RES_FECHA', models.DateField(verbose_name='Fecha')),
                ('RES_DESCRIP', models.TextField(max_length=300, verbose_name='Descripción')),
                ('RES_EXPEDIENTE', models.CharField(max_length=18, verbose_name='Expediente')),
                ('RES_TIPO', models.CharField(max_length=20, verbose_name='Contratado u Ordinario')),
                ('RES_CATEG', models.CharField(max_length=30, verbose_name='Tipo de contrato')),
                ('RES_CLASE', models.CharField(max_length=30, verbose_name='Carga Académica')),
            ],
        ),
        migrations.CreateModel(
            name='TITULO',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TIT_NOMBRE', models.CharField(max_length=40, verbose_name='Nombre')),
                ('TIT_TIPO', models.CharField(max_length=20, verbose_name='Título o Bachiller')),
                ('TIT_INI', models.DateField(verbose_name='Fecha de Inicio')),
                ('TIT_FIN', models.DateField(verbose_name='Fecha de Fin')),
                ('docente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='legajo.DOCENTE')),
                ('institucion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='legajo.INSTITUCION')),
            ],
        ),
        migrations.CreateModel(
            name='produccionCIENTFICA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PROD_TIPO', models.CharField(max_length=50, verbose_name='Tipo de Producción Científica')),
                ('PROD_TITULO', models.CharField(max_length=150, verbose_name='Nombre')),
                ('PROD_PRIMER_AUTOR', models.CharField(max_length=100, verbose_name='Primer Autor')),
                ('PROD_FECHA', models.DateField(verbose_name='Fecha de Publicación')),
                ('PROD_REPOSI', models.CharField(max_length=100, verbose_name='Repositorio')),
                ('PROD_URL', models.URLField(max_length=300, verbose_name='URL del Repositorio')),
                ('docentes', models.ManyToManyField(to='legajo.DOCENTE')),
            ],
        ),
        migrations.CreateModel(
            name='grupoInvestigacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('GI_TEMA', models.CharField(max_length=100, verbose_name='Tema de Investigación')),
                ('GI_NOMBRE', models.CharField(max_length=100, verbose_name='Título de la Investigación')),
                ('GI_INV_PRINCIPAL', models.CharField(max_length=100, verbose_name='Investigador Principal')),
                ('GI_FECHA_INI', models.DateField(verbose_name='Fecha de Inicio')),
                ('GI_FECHA_FIN', models.DateField(default='1900-01-01', verbose_name='Fecha de Fin')),
                ('GI_DESCRIPCION', models.TextField(max_length=300, verbose_name='Descripcion')),
                ('docentes', models.ManyToManyField(to='legajo.DOCENTE')),
            ],
        ),
        migrations.CreateModel(
            name='experienciaLABORAL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EXL_CARGO', models.CharField(max_length=60, verbose_name='Cargo')),
                ('EXL_FECHA_INI', models.DateField(verbose_name='Fecha de Inicio')),
                ('EXL_FECHA_FIN', models.DateField(default='1900-01-01', verbose_name='Fecha de Fin')),
                ('EXL_SUELDO', models.IntegerField(blank=True, default=0, verbose_name='Sueldo en Soles')),
                ('EXL_DESCRIP', models.TextField(max_length=200, verbose_name='Descripcion')),
                ('docentes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='legajo.DOCENTE')),
                ('entidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='legajo.ENTIDAD')),
            ],
        ),
        migrations.CreateModel(
            name='experienciaDOCENTE',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EXD_FECHA_INI', models.DateField(verbose_name='Fecha de Inicio')),
                ('EXD_FECHA_FIN', models.DateField(default='1900-01-01', verbose_name='Fecha de Fin')),
                ('EXD_CARGO', models.CharField(default='', max_length=60, verbose_name='Cargo')),
                ('docente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='legajo.DOCENTE')),
                ('institucion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='legajo.INSTITUCION')),
            ],
        ),
        migrations.CreateModel(
            name='ESPECIALIZACION',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ESP_TIPO', models.CharField(max_length=40, verbose_name='Tipo')),
                ('ESP_NOMBRE', models.CharField(max_length=60, verbose_name='Nombre de la Especialización')),
                ('ESP_FECHA_INI', models.DateField(verbose_name='Fecha de Inicio')),
                ('ESP_FECHA_FIN', models.DateField(verbose_name='Fecha de Fin')),
                ('docente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='legajo.DOCENTE')),
                ('institucion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='legajo.INSTITUCION')),
            ],
        ),
        migrations.CreateModel(
            name='CURSO',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CUR_COD', models.CharField(max_length=20, unique=True, verbose_name='Código')),
                ('CUR_CRED', models.IntegerField(default=0, verbose_name='Créditos')),
                ('CUR_HOR_SEM', models.IntegerField(default=0, verbose_name='Horas Semanales')),
                ('CUR_CICLO', models.CharField(max_length=4, verbose_name='Ciclo')),
                ('CUR_SEMES', models.CharField(max_length=8, verbose_name='Semestre Académico')),
                ('CUR_NOMBRE', models.CharField(max_length=20, verbose_name='Asignatura')),
                ('docentes', models.ManyToManyField(to='legajo.DOCENTE')),
            ],
        ),
        migrations.CreateModel(
            name='evaluacionyPerfeccionamiento',
            fields=[
                ('EVA_TIPO', models.CharField(max_length=50, verbose_name='Tipo de Evaluación')),
                ('EVA_OBSERVACION', models.TextField(blank=True, max_length=200, verbose_name='Observación')),
                ('docentes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='legajo.DOCENTE')),
                ('resolucion', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='legajo.RESOLUCION')),
            ],
        ),
        migrations.CreateModel(
            name='CARGO',
            fields=[
                ('CAR_NOM', models.CharField(max_length=50, verbose_name='Cargo')),
                ('CAR_DESCRIP', models.TextField(verbose_name='Descripción de su Cargo')),
                ('docente', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='legajo.DOCENTE')),
                ('resolucion', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='legajo.RESOLUCION')),
            ],
        ),
    ]
