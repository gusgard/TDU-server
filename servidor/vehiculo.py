__author__ = 'yoda'


class Vehiculo():

    #def __init__(self):
        #self.id_vehiculo = id_vehiculo
        #self.var1 = var1
        #self.var2 = var2
        #self.var3 = var3

    def __unicode__(self):
        return '%s, %s, %s, %s' % (self.id_vehiculo, self.var1, self.var2, self.var3)

    def __str__(self):
        return '%s, %s, %s, %s' % (self.id_vehiculo, self.var1, self.var2, self.var3)

    def serializar(self):
        return '%s;%s;%s;%s' % (self.id_vehiculo, self.var1, self.var2, self.var3)

    def deserializar(self, vehiculo_serializado):
        lista_atributos = vehiculo_serializado.split(';')
        self.id_vehiculo = lista_atributos[0]
        self.var1 = lista_atributos[1]
        self.var2 = lista_atributos[2]
        self.var3 = lista_atributos[3]








