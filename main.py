import os
from tv import Tv
from consola import Consola
from bicicleta import Bicicleta

class Main:
    def __init__(self):
        self.listasTvs = []
        self.listasConsolas = []
        self.listasScooters = []
        self.listasBicicletas = []
        self.next_id = 1  


    def limpiar(self):
        # Limpiar la consola
        os.system("cls" if os.name == "nt" else "clear")


    def registrar_tv(self):
        self.limpiar()  # Llama a la función para limpiar la consola
        print("Registrar TV")
        # Solicita y valida la marca de la TV
        while True:
            marca = input("Ingrese la marca de la TV: ")
            if marca.strip():  # Verificar que la entrada no esté vacía
                break
            else:
                print("Marca no válida. Intente nuevamente.")
        # Solicita y valida el voltaje de la TV
        while True:
            try:
                voltaje = int(input("Ingrese el voltaje de la TV: "))
                break
            except ValueError:
                print("Voltaje no válido. Ingrese un número entero válido.")
        # Solicita y valida el precio de la TV
        while True:
            try:
                precio = float(input("Ingrese el precio de la TV: "))
                break
            except ValueError:
                print("Precio no válido. Ingrese un número decimal válido.")
        # Solicitar y validar el nivel de eficiencia de la TV
        eficiencia = input("Ingrese el nivel de eficiencia de la Tv: ")
        # Solicita y valida el tamaño de la TV
        while True:
            try:
                tamano = float(input("Ingrese el tamaño de la TV en pulgadas: "))
                break
            except ValueError:
                print("Tamaño no válido. Ingrese un número decimal válido.")
        # Crear una instancia de la clase Tv y agregarla a la lista de Tvs
        tv = Tv(voltaje, precio, eficiencia, marca, tamano)
        tv.id = self.next_id
        self.next_id += 1  # Incrementa el siguiente ID disponible para usar uno distinto
        # Agregar la Tv a la lista de Tvs
        self.listasTvs.append(tv)
        self.limpiar()
        print("TV registrada exitosamente")


    def registrar_consola(self):
        self.limpiar()  # Llama a la función para limpiar la consola
        print("Registrar Consola")
        # Solicita y valida el nombre de la consola
        while True:
            nombre_consola = input("Ingrese el nombre de la consola: ")
            if nombre_consola.strip():  # Verifica que la entrada no esté vacía
                break
            else:
                print("Nombre de consola no válido. Intente nuevamente.")
        # Solicita y valida la versión de la consola
        while True:
            version = input("Ingrese la versión de la consola: ")
            if version.strip():  # Verificar que la entrada no esté vacía
                break
            else:
                print("Versión de consola no válida. Intente nuevamente.")
        # Solicita y valida la marca de la consola
        while True:
            marca = input("Ingrese la marca de la consola: ")
            if marca.strip():  # Verifica que la entrada no esté vacía
                break
            else:
                print("Marca de consola no válida. Intente nuevamente.")
        # Solicita y valida el voltaje de la consola
        while True:
            try:
                voltaje = int(input("Ingrese el voltaje de la consola: "))
                break
            except ValueError:
                print("Voltaje no válido. Ingrese un número entero válido.")
        # Solicita y valida el precio de la consola
        while True:
            try:
                precio = float(input("Ingrese el precio de la consola: "))
                break
            except ValueError:
                print("Precio no válido. Ingrese un número decimal válido.")
        # Solicita y valida el nivel de eficiencia de la consola
        eficiencia = input("Ingrese el nivel de eficiencia de la consola: ")
        # Crear una instancia de la clase Consola
        consola = Consola(voltaje, precio, eficiencia, marca, nombre_consola, version)
        # Asignar un ID único
        consola.id = self.next_id
        self.next_id += 1  # Incrementa el siguiente ID disponible para usar uno distinto
        # Agregar la Consola a la lista de Consolas
        self.listasConsolas.append(consola)
        self.limpiar()
        print("Consola registrada exitosamente")


    def registrar_bicicleta(self):
        self.limpiar()  # Llama a la función para limpiar la consola
        print("Registrar Bicicleta")
        # Solicita y valida el aro de la bicicleta
        while True:
            try:
                aro = float(input("Ingrese el tamaño del aro de la bicicleta: "))
                break
            except ValueError:
                print("Tamaño de aro no válido. Ingrese un número decimal válido.")
        # Solicita y valida el peso de la bicicleta
        while True:
            try:
                peso = float(input("Ingrese el peso de la bicicleta en kg: "))
                break
            except ValueError:
                print("Peso no válido. Ingrese un número decimal válido.")
        # Solicita y valida el precio de la bicicleta
        while True:
            try:
                precio = float(input("Ingrese el precio de la bicicleta: "))
                break
            except ValueError:
                print("Precio no válido. Ingrese un número decimal válido.")
        # Solicita y valida la marca de la bicicleta
        while True:
            marca = input("Ingrese la marca de la bicicleta: ")
            if marca.strip():  # Verifico que la entrada no esté vacía
                break
            else:
                print("Marca de bicicleta no válida. Intente nuevamente.")
        # Crear una instancia de la clase Bicicleta
        bicicleta = Bicicleta(aro, peso, precio, marca)
        bicicleta.id = self.next_id
        self.next_id += 1  # Incrementa el siguiente ID disponible para usar uno distinto
        # Agregue la bicicleta a la lista de bicicletas
        self.listasBicicletas.append(bicicleta)
        self.limpiar()
        print("Bicicleta registrada exitosamente")

    # Implemento el limpiar consola ademas de hacer un for para recuperar cada elemento de la lista ademas de heredar las funciones de mostrar elaboradas en cada instancia
    def mostrar_productos(self):
            self.limpiar()  
            print("Productos Registrados:\n")
            
            print("Tvs:")
            for tv in self.listasTvs:
                print(tv.mostrar_tv())
            
            print("\nConsolas:")
            for consola in self.listasConsolas:
                print(consola.mostrar_consola())
            
            print("\nBicicletas:")
            for bicicleta in self.listasBicicletas:
                print(bicicleta.mostrar_bicicleta())  
            input("\nPresione Enter para volver al menú principal...")

    # Sencillo solo llamo a las funciones mediaante un menu usado por sprints y vaidados con if para verificar las opciones ademas incluye un for para recuperar cada elemento de la lista correspondiente ademas se le llama al id concadenadolo con la llamada de str que es como la funcion para llamar a los str de las instancias
    def menu_cotizar(self):
        while True:
            print("Menú de Cotización:")
            print("1. Cotizar TV")
            print("2. Cotizar Consola")
            print("3. Cotizar Bicicleta")
            print("4. Volver al Menu Principal")
            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                self.limpiar()
                print("Cotizar TV:")
                print("Registros de TV:")
                for tv in self.listasTvs:
                    print(f"ID: {tv.id}")
                    print(str(tv)) 
                    print("------------")
            elif opcion == "2":
                self.limpiar()
                print("Cotizar Consola:")
                print("Registros de Consolas:")
                for consola in self.listasConsolas:
                    print(f"ID: {consola.id}")
                    print(str(consola)) 
                    print("------------")
            elif opcion == "3":
                self.limpiar()
                print("Cotizar Bicicleta:")
                print("Registros de Bicicletas:")
                for bicicleta in self.listasBicicletas:
                    print(f"ID: {bicicleta.id}")
                    print(str(bicicleta)) 
                    print("------------")
            elif opcion == "4":
                self.limpiar()
                break
            else:
                self.limpiar()
                print("Opción no válida. Por favor, elija una opción válida.")

    # Sencillo solo llamo a las funciones mediaante un menu usado por sprints y vaidados con if para verificar las opciones
    def menu(self):
        while True:
            print("Menú:")
            print("1. Registrar TV")
            print("2. Registrar Consola")
            print("3. Registrar Scooter")
            print("4. Registrar Bicicleta")
            print("5. Cotizar producto")
            print("6. Mostrar Productos")
            print("7. Salir")
            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                self.limpiar()  
                self.registrar_tv()
            elif opcion == "2":
                self.limpiar()  
                self.registrar_consola()
            elif opcion == "3":
                # No la hice por temas de tiempo
                pass
            elif opcion == "4":
                self.limpiar()
                self.registrar_bicicleta()
            elif opcion == "5":
                self.limpiar()
                self.menu_cotizar()
            elif opcion == "6":
                self.limpiar()
                self.mostrar_productos()
            elif opcion == "7":
                break
            else:
                self.limpiar()  
                print("Opción no válida. Por favor, elija una opción válida.")


main = Main()
main.menu()