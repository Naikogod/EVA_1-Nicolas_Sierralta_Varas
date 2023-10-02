from tecnologia import Tecnologia 

class Consola(Tecnologia):
    def __init__(self, voltaje: int, precio: float, eficiencia: str, marca: str, nombreConsola: str, version: str):
        super().__init__(voltaje, precio, eficiencia, marca)
        self.__nombreConsola = nombreConsola
        self.__version = version
        self.id = None  


    def get_nombreConsola(self):
        return self.__nombreConsola


    def get_version(self):
        return self.__version


    def calcular_descuento(self):
        eficiencia = self.get_eficiencia()
        descuento = 0
        if eficiencia in ["A", "B"]:
            descuento = 0.5
        elif eficiencia in ["C", "D"]:
            descuento = 0.3
        elif eficiencia in ["E", "F"]:
            descuento = 0.1
        if "Lite" in self.get_version():
            descuento += 0.05
        return descuento


    def mostrar_consola(self):
        tecnologia_str = super().__str__()  
        return (
            f"{tecnologia_str}\n"
            f"Nombre de la Consola: {self.get_nombreConsola()}\n"
            f"Versión: {self.get_version()}\n"
        )


    def __str__(self):
        tecnologia_str = super().__str__()  
        descuento = self.calcular_descuento()
        precio_descuento = self.get_precio() * (1 - descuento)
        return (
            f"{tecnologia_str}\n"
            f"Nombre de la Consola: {self.get_nombreConsola()}\n"
            f"Versión: {self.get_version()}\n"
            f"Descuento aplicado: {descuento * 100}%\n"
            f"Valor total después del descuento: {precio_descuento} $CLP"
        )
