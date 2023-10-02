from tecnologia import Tecnologia

class Tv(Tecnologia):
    def __init__(self, voltaje: int, precio: float, eficiencia: str, marca: str, tamano: float):
        super().__init__(voltaje, precio, eficiencia, marca)
        self.__tamano = tamano
        self.id = None  


    def get_tamano(self):
        return self.__tamano


    def set_tamano(self, tamano):
        self.__tamano = tamano

    def mostrar_tv(self):
        tecnologia_str = super().__str__()  
        return (
            f"{tecnologia_str}\n"
            f"Tamaño: {self.get_tamano()} pulgadas\n"
        )

    def __str__(self):
        tecnologia_str = super().__str__()  
        descuento = self.calcular_descuento()
        precio_descuento = self.get_precio() * (1 - descuento)
        return (
            f"{tecnologia_str}\n"
            f"Tamaño: {self.get_tamano()} pulgadas\n"
            f"Descuento aplicado: {descuento * 100}%\n"
            f"Valor total después del descuento: {precio_descuento} $CLP"
        )