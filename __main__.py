sumUnidades_VentasSteam = 0
cantJuegosSteam = 0

sumUnidades_VentasFisico = 0
cantJuegosFisico = 0

listaPaises = []
listaJuegos = []
MatrizCantVentas = []

print("Bienvenido a Steam")
nombreArchivo = input("Ingrese nombre del archivo: ").upper()
cantArchivosLeido = 0
while nombreArchivo != "CIERRE":
    try:
        arch = open(nombreArchivo, "r")
        cantArchivosLeido += 1
        linea = arch.readline().strip()
        while linea != "":
            partes = linea.split(";")
            pais = partes[0]
            titulo = partes[1]
            cantVendidas = int(partes[2])
            precio = float(partes[3])
            tienda = partes[4]
            linea = arch.readline().strip()
            if tienda == "STEAM":
                cantJuegosSteam+=1
                sumUnidades_VentasSteam+=cantVendidas
            else:
                cantJuegosFisico+=1
                sumUnidades_VentasFisico+=cantVendidas

            if titulo is not listaJuegos:
                listaJuegos.append(titulo)
                aux = []
                for i in range(len(listaPaises)):
                    aux.append(0)
                MatrizCantVentas.append(aux)

            if pais is not listaPaises:
                listaPaises.append(pais)
                for fil in MatrizCantVentas:
                    fil.append(0)

            posCol = listaPaises.index(pais)
            posFil = listaJuegos.index(titulo)

            MatrizCantVentas[posFil][posCol]+=cantVendidas

    except Exception as e:
        print("[!] Error durante la lectura del archivo:", e)

    nombreArchivo = input("Ingrese nombre del archivo: ").upper()


