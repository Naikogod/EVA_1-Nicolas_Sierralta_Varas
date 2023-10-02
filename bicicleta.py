from transporte import Transporte

class Bicicleta:
    def __init__(self, aro: float, peso: float, precio: float, marca: str):
        self.__aro = aro
        self.__peso = peso
        self.__precio = precio
        self.__marca = marca
        self.id = None  

    def calcularCostoDespacho(self):
        transporte = Transporte()
        valor_por_kilogramo = 400 
        costo_total_despacho = transporte.calcularDespacho(self.__peso, valor_por_kilogramo)
        return costo_total_despacho


    def mostrar_bicicleta(self):
            return (
            f"Aro: {self.__aro}\n"
            f"Peso: {self.__peso} kg\n"
            f"Precio: ${self.__precio}\n"
            f"Marca: {self.__marca}\n"
            )


    def __str__(self):
        costo_despacho = self.calcularCostoDespacho()
        return (
            f"Aro: {self.__aro}\n"
            f"Peso: {self.__peso} kg\n"
            f"Precio: ${self.__precio}\n"
            f"Marca: {self.__marca}\n"
            f"Costo de Despacho: ${costo_despacho}"
            )