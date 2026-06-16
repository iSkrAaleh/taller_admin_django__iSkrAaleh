from django.db import models

class Museo(models.Model):
    nombre = models.CharField(max_length=150, unique=True, null=False, blank=False)
    ciudad = models.CharField(max_length=100)
    año_fundacion = models.IntegerField()

    def __str__(self):
        return self.nombre


class GuiaMuseo(models.Model):
    nombre_completo = models.CharField(max_length=200)
    años_experiencia_guia = models.IntegerField()
    idiomas_hablados = models.CharField(max_length=255) 
    #relacion de un guia trabaja en un museo (muchos guias pertenecen a un museo)    
    museo = models.ForeignKey(Museo, on_delete=models.CASCADE, related_name='guias')

    def __str__(self):
        return self.nombre_completo

class Exhibicion(models.Model):
    titulo_exhibicion = models.CharField(max_length=200)
    duracion_meses = models.IntegerField()
    costo_produccion = models.DecimalField(max_digits=12, decimal_places=2)
    tematica = models.CharField(max_length=150)
    
    # una exhibición es asistida por un guía de museo
    guia = models.ForeignKey(GuiaMuseo, on_delete=models.CASCADE, related_name='exhibiciones')

    def __str__(self):
        return self.titulo_exhibicion
