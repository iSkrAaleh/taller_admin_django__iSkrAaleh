from django.db import models

class Museo(models.Model):
    nombre = models.CharField(max_length=150, unique=True, null=False, blank=False)
    ciudad = models.CharField(max_length=100)
    año_fundacion = models.IntegerField()

    def __str__(self):
        return self.nombre
    
    def calcular_costo_exhibiciones(self):
        total = 0
        for guia in self.guias.all():
            for exhibicion in guia.exhibiciones.all():
                total += exhibicion.costo_produccion
        if total > 0:
            return f"${total}"
        return "$0.00"
    
    calcular_costo_exhibiciones.short_description = 'costo total exhibiciones'

    def obtener_mejores_guias(self):
        todos_los_guias = self.guias.all()
        if not todos_los_guias:
            return "sin guías asignados"        
        max_exp = -1
        for guia in todos_los_guias:
            if guia.años_experiencia_guia > max_exp:
                max_exp = guia.años_experiencia_guia
        nombres = []
        for guia in todos_los_guias:
            if guia.años_experiencia_guia == max_exp:
                nombres.append(guia.nombre_completo)
                
        return ", ".join(nombres)
    obtener_mejores_guias.short_description = 'Guias con más experiencia'


class GuiaMuseo(models.Model):
    nombre_completo = models.CharField(max_length=200)
    años_experiencia_guia = models.IntegerField()
    idiomas_hablados = models.CharField(max_length=255) 
    museo = models.ForeignKey(Museo, on_delete=models.CASCADE, related_name='guias')
    def __str__(self):
        return self.nombre_completo


class Exhibicion(models.Model):
    titulo_exhibicion = models.CharField(max_length=200)
    duracion_meses = models.IntegerField()
    costo_produccion = models.DecimalField(max_digits=12, decimal_places=2)
    tematica = models.CharField(max_length=150)
    guia = models.ForeignKey(GuiaMuseo, on_delete=models.CASCADE, related_name='exhibiciones')

    def __str__(self):
        return self.titulo_exhibicion
