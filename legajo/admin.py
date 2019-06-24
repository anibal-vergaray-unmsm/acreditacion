from django.contrib import admin

from .models import DOCENTE
from .models import CURSO
from .models import ENTIDAD, experienciaLABORAL
from .models import INSTITUCION, experienciaDOCENTE
from .models import grupoInvestigacion
from .models import TITULO
from .models import ESPECIALIZACION
from .models import produccionCIENTFICA
from .models import evaluacionyPerfeccionamiento
from .models import CARGO
from .models import RESOLUCION

admin.site.register(DOCENTE)

admin.site.register(CURSO)

admin.site.register(ENTIDAD)
admin.site.register(experienciaLABORAL)

admin.site.register(INSTITUCION)
admin.site.register(experienciaDOCENTE)

admin.site.register(grupoInvestigacion)

admin.site.register(TITULO)
admin.site.register(ESPECIALIZACION)
admin.site.register(produccionCIENTFICA)

admin.site.register(evaluacionyPerfeccionamiento)

admin.site.register(CARGO)

admin.site.register(RESOLUCION)