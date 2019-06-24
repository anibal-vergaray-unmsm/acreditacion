from django.db import models


class DOCENTE(models.Model):
    DOC_COD = models.CharField('Código',max_length=8,unique=True)
    DOC_DNI = models.CharField('DNI',max_length=10,unique=True)
    DOC_CELU = models.CharField('Celular',max_length=10,unique=True)
    DOC_EMAIL = models.CharField('Email',max_length=50,unique=True)
    DOC_NOMBRE = models.CharField('Nombre',max_length=50)
    DOC_APE = models.CharField('Apellido',max_length=50)
    DOC_SEXO = models.CharField('Sexo',max_length=15)
    DOC_NAC = models.DateField('Fecha de Nacimiento')
    DOC_ESTADO = models.CharField('Estado',max_length=30)

    def __str__(self):
        return self.DOC_NOMBRE + " " +  self.DOC_APE


class CURSO(models.Model):
    CUR_COD = models.CharField('Código',max_length = 20,unique=True)
    CUR_CRED = models.IntegerField('Créditos',default=0)
    CUR_HOR_SEM = models.IntegerField('Horas Semanales',default=0)
    CUR_CICLO = models.CharField('Ciclo',max_length=4)
    CUR_SEMES = models.CharField('Semestre Académico',max_length=8)
    CUR_NOMBRE = models.CharField('Asignatura',max_length=20)
    docentes = models.ManyToManyField(DOCENTE)

    def __str__(self):
        return self.CUR_NOMBRE

class ENTIDAD(models.Model):
    ENT_NOMBRE = models.CharField('Entidad',max_length=100)
    ENT_SECTOR = models.CharField('Sector',max_length=15)
    ENT_RUBRO = models.CharField('Rubro',max_length=80,blank=True)

    def __str__(self):
        return self.ENT_NOMBRE


class experienciaLABORAL(models.Model):
    EXL_CARGO = models.CharField('Cargo',max_length=60)
    EXL_FECHA_INI = models.DateField('Fecha de Inicio')
    EXL_FECHA_FIN = models.DateField('Fecha de Fin',default='1900-01-01')
    EXL_SUELDO = models.IntegerField('Sueldo en Soles',default=0,blank=True)
    EXL_DESCRIP = models.TextField('Descripcion',max_length=200)
    entidad = models.ForeignKey(ENTIDAD,on_delete=models.CASCADE)
    docentes = models.ForeignKey(DOCENTE,on_delete=models.CASCADE)

    def __str__(self):
        return self.EXL_CARGO


class INSTITUCION(models.Model):
    INSTI_NOMBRE = models.CharField('Institución',max_length=150)
    INSTI_PAIS = models.CharField('País',max_length=60)
    INSTI_TIPO = models.CharField('Tipo de Institución',max_length=40)

    def __str__(self):
        return self.INSTI_NOMBRE


class experienciaDOCENTE(models.Model):
    EXD_FECHA_INI = models.DateField('Fecha de Inicio',)
    EXD_FECHA_FIN = models.DateField('Fecha de Fin',default='1900-01-01')
    EXD_CARGO = models.CharField('Cargo',max_length=60,default='')
    docente = models.ForeignKey(DOCENTE, on_delete=models.CASCADE)
    institucion = models.ForeignKey(INSTITUCION, on_delete=models.CASCADE)

    def __str__(self):
        return self.EXD_CARGO


class grupoInvestigacion(models.Model):
    GI_TEMA = models.CharField('Tema de Investigación',max_length=100)
    GI_NOMBRE = models.CharField('Título de la Investigación',max_length=100)
    GI_INV_PRINCIPAL = models.CharField('Investigador Principal',max_length=100)
    GI_FECHA_INI = models.DateField('Fecha de Inicio')
    GI_FECHA_FIN = models.DateField('Fecha de Fin',default='1900-01-01')
    GI_DESCRIPCION = models.TextField('Descripcion',max_length=300)
    docentes = models.ManyToManyField(DOCENTE)

    def __str__(self):
        return self.GI_NOMBRE


class TITULO(models.Model):
    TIT_NOMBRE = models.CharField('Nombre',max_length=40)
    TIT_TIPO = models.CharField('Título o Bachiller',max_length=20)
    TIT_INI = models.DateField('Fecha de Inicio')
    TIT_FIN = models.DateField('Fecha de Fin')
    docente = models.ForeignKey(DOCENTE, on_delete=models.CASCADE)
    institucion = models.ForeignKey(INSTITUCION, on_delete=models.CASCADE)

    def __str__(self):
        return self.TIT_NOMBRE


class ESPECIALIZACION(models.Model):
    ESP_TIPO = models.CharField('Tipo',max_length=40)
    ESP_NOMBRE = models.CharField('Nombre de la Especialización',max_length=60)
    ESP_FECHA_INI = models.DateField('Fecha de Inicio')
    ESP_FECHA_FIN = models.DateField('Fecha de Fin')
    docente = models.ForeignKey(DOCENTE, on_delete=models.CASCADE)
    institucion = models.ForeignKey(INSTITUCION, on_delete=models.CASCADE)

    def __str__(self):
        return self.ESP_NOMBRE


class produccionCIENTFICA(models.Model):
    PROD_TIPO = models.CharField('Tipo de Producción Científica',max_length=50)
    PROD_TITULO = models.CharField('Nombre',max_length=150)
    PROD_PRIMER_AUTOR = models.CharField('Primer Autor',max_length=100)
    PROD_FECHA = models.DateField('Fecha de Publicación')
    PROD_REPOSI = models.CharField('Repositorio',max_length=100)
    PROD_URL = models.URLField('URL del Repositorio',max_length=300)
    docentes = models.ManyToManyField(DOCENTE)

    def __str__(self):
        return self.PROD_TITULO




class RESOLUCION(models.Model):
    RES_FECHA = models.DateField('Fecha')
    RES_DESCRIP = models.TextField('Descripción', max_length=300)
    RES_EXPEDIENTE = models.CharField('Expediente', max_length=18)
    RES_TIPO = models.CharField('Contratado u Ordinario', max_length=20) #Ordinario o Contratado
    RES_CATEG = models.CharField('Tipo de contrato', max_length=30) #Principal, Asociado, Auxiliar; Tipo A,B
    RES_CLASE = models.CharField('Carga Académica', max_length=30) #Tiempo Completo, Parcial; Tipo A-1,etc...
    def __str__(self):
        return self.RES_EXPEDIENTE



class evaluacionyPerfeccionamiento(models.Model):
    EVA_TIPO = models.CharField('Tipo de Evaluación', max_length=50)#Nombramiento, última ratificación, última promoción
    EVA_OBSERVACION = models.TextField('Observación', max_length=200,blank=True)
    docentes = models.ForeignKey(DOCENTE, on_delete=models.CASCADE, primary_key=True)
    resolucion = models.OneToOneField(
        RESOLUCION,
        on_delete= models.CASCADE,
    )

    def __str__(self):
        return self.EVA_TIPO


class CARGO(models.Model): #Esto se refiere a cargos que desempeña en la Universidad
    CAR_NOM = models.CharField('Cargo',max_length=50)
    CAR_DESCRIP = models.TextField('Descripción de su Cargo')
    docente = models.OneToOneField(
        DOCENTE,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    resolucion = models.OneToOneField(
        RESOLUCION,
        on_delete=models.CASCADE,
    )
    def __str__(self):
        return self.CAR_NOM

