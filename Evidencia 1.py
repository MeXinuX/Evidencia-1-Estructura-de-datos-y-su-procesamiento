import datetime

cliente = {}
id_cliente = 0
salas = {}
id_sala = 0
reservas = {}
id_reserva = 0
turnos = {}
fecha_actual = (datetime.date.today())
fecha = {}


while True:
    opcion_menu = input("""Ingresa una opcion del menú
    ___Menú de opciones____
    1 Reservar una sala
    2 Cambiar nombre de la reservación
    3 Consultar reservaciones
    4 Registrar nuevo cliente
    5 Registrar una sala
    6 Salir
    """)
    if opcion_menu=="1":
        if not salas:
            print("Favor de registrar una sala")
        else:
            while True:
                numero_cliente = input("Ingrese su ID cliente: \n")
                if numero_cliente == "":
                        print("El campo no puede quedar vacio \n")
                        continue
                else:
                    pass

                if numero_cliente not in cliente.keys():
                        print("Favor de registrarse como cliente \n")
                        break
                else:
                    pass
                try:
                    while True:
                        fecha_deseada = input("Ingrese la fecha deseada (dd/mm/aaaa): \n")
                        if fecha_deseada == "":
                                    print("El campo no puede quedar vacío")
                                    continue
                        else:
                            fecha_guardada = datetime.datetime.strptime(fecha_deseada,"%d/%m/%Y").date()

                            limite_fecha = (fecha_guardada - fecha_actual).days
                            if limite_fecha <=2:
                                print("Se necesitan dos dias de anticipacion")
                                continue
                            else:
                                numero_sala = input("Ingrese su ID sala: \n")
                                if numero_sala == "":
                                    print("El campo no puede quedar vacio")
                                    continue
                                if numero_sala not in salas.keys():
                                        print("No hay una sala con ese ID")
                                        break
                                else:
                                    pass

                                while True:
                                    turno = input("""Ingresa un turno
                                    (M) Matutino \n
                                    (V) Vespertino \n
                                    (N) Nocturno \n
                                    """)
                                    turno = turno.title()
                                    if turno == "":
                                        print("No se puede dejar vacio")
                                        continue
                                    elif turno == "M":
                                        turno = "Matutino"
                                        print("\n Eligio el turno matutino")
                                        break
                                    elif turno == "V":
                                        turno = "Vespertino"
                                        print("\n Eligio el turno vespertino")
                                        break
                                    elif turno == "N":
                                        turno = "Nocturno"
                                        print("\n Eligio el turno nocturno")
                                        break
                                    else:
                                        print("No existe opción seleccionada \n")
                                        continue
                        break
                except Exception:
                    print("Debe ingresar una fecha con formato")

                for i in reservas.values():
                    if fecha_deseada in reservas.values():
                        if id_sala in reservas.values():
                            if turno not in reservas.values():
                                print("Ocupado")

                if numero_cliente in cliente.keys():
                    nombre_evento = input("Ingrese el nombre de su evento: \n")
                    id_reserva+= 1
                    reservas[str(id_reserva)] = {'ID cliente':id_cliente,'Fecha':fecha_guardada,'ID sala': id_sala,'ID reserva':id_reserva,'turno':turno}
                    print((f'La reserva {nombre_evento} se le asigno el ID reserva {id_reserva}'))
                    print(reservas)
                break


    elif opcion_menu=="2":
        while True:
            id_reserva = input("Ingresa tu ID de reserva: \n")
            if id_reserva=="":
                print("No se puede dejar vacio")
                continue
            else:
                break
        if id_reserva not in reservas.keys():
            print("No existen reservas con ese ID")
            break
        else:
            nombre_evento = input("Ingrese el nombre deseado: \n")
            reservas[str(id_reserva)][0] = nombre_evento
            print("Se modifico el nombre del evento")
        pass


    elif opcion_menu=="3":
        fecha_consulta = input("Ingresa la fecha a consultar en formato dd/mm/aaaa: \n")
        fecha_forma = datetime.datetime.strptime(fecha_consulta, "%d/%m/%Y").date()
        fecha[str(fecha_forma)] = fecha_consulta
        if fecha_forma == "":
            print("No ingreso ninguna fecha")
        else:
            pass
        for i in fecha.items():
            if fecha_consulta not in fecha.values():
                print("No hay ninguna fecha disponible")
            else:
                print("*" * 65)
                print("" * 7 + f"  REPORTE DE RESERVACIONES PARA EL DÍA {fecha_forma}  " + "" * 7)
                print("*" * 65)
                print(format("SALA:{nombre_sala}" +  "  " * 5 + "CLIENTE:{nombre_cliente}" + "  " * 5 + "EVENTO:{nombre_evento}" +  "  " * 5     +  "TURNO:{turno}"))
                print("*" * 65)
                print("" * 25 + "FIN DEL REPORTE" + "" * 25)
                break
    elif opcion_menu=="4":
        while True:
            cliente_nv = input('Ingrese su nombre: \n')

            if cliente_nv =="":
                print("No se puede dejar vacio \n")
                continue
            else:
                id_cliente+= 1
                cliente[str(id_cliente)]= cliente_nv
                print(f'Al usuario {cliente_nv} se le asigno el ID cliente: {id_cliente}')
                print(cliente)
                break


    elif opcion_menu=="5":
        while True:
            nombre_sala = input("Ingrese el nombre de la sala: \n")
            if nombre_sala =="":
                print("No se puede dejar vacio \n")
                continue
            try:
                cupo_sala = int(input("Ingresa el cupo de la sala: \n"))
            except Exception:
                print("El cupo de la sala tiene que ser numerico \n")
                continue
            if nombre_sala in salas:
                print(f"Ya existe una sala con este nombre {nombre_sala}")
            else:
                id_sala+= 1
                salas[str(id_sala)]= {'nombre sala':nombre_sala,'id sala':id_sala}
                print(f'A la sala {nombre_sala} se le asigno el ID sala: {id_sala}')
                print(salas)
                break

    elif opcion_menu=="6":
        break
    else:
        print("Ingrese una opción \n")