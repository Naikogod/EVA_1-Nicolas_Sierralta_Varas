class Tecnologia:
    def __init__(self, voltaje: int, precio: float, eficiencia: str, marca: str):
        self.__voltaje = voltaje
        self.__precio = precio
        self.__eficiencia = eficiencia
        self.__marca = marca

    def get_precio(self):
        return self.__precio

    def get_eficiencia(self):
        return self.__eficiencia.upper()


    def calcular_descuento(self):
        eficiencia = self.get_eficiencia()
        descuento = 0
        if eficiencia in ["A", "B"]:
            descuento = 0.5
        elif eficiencia in ["C", "D"]:
            descuento = 0.3
        elif eficiencia in ["E", "F"]:
            descuento = 0.1
        return descuento


    def __str__(self):
        return (
            f"Voltaje: {self.__voltaje}\n"
            f"Precio: {self.__precio}\n"
            f"Eficiencia: {self.__eficiencia.upper()}\n"
            f"Marca: {self.__marca}"
        )
