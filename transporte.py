class Transporte:
    def __init__(self):
        self.COSTODESPACHOBASE = 4000.0

    def calcularDespacho(self, peso: float, valor_por_kilogramo: int):
        costo_despacho_base = self.COSTODESPACHOBASE
        costo_adicional_peso = peso * valor_por_kilogramo
        costo_total_despacho = costo_despacho_base + costo_adicional_peso
        return costo_total_despacho