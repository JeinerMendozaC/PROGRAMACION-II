L=[1200,1300,1400,1500,1700,1800,2400,2500,2550,3000,3550,4000,4500,5000] #OPERACION 1 CREACION DE LISTA
SET={"10%","20%","30%","40%"}#OPERACION 2 CREACION DE SET
TUPLA=("COSINA","LAVADORA","REFRIGERADORA","LICUADORA","PLANCHA","TELEVISOR","MICROONDAS","SONIDO","BATIDORA") #OPERACION 3 CREACION DE TUPLA
print("#####  BIENVENIDO A NUESTRA TIENDA DE ELECTRODOMESTICOS #####")
print("###################################################################")
print("A CONTINUACION INGRESARA SU COMPRA, CUANDO FINALIZE SOLO ESCRIBA FIN")
print("###################################################################")
print(" DEPENDIENDO SU COMPRE TENEMOS LOS SIGIENTES DESCUENTOS:",SET)
print("###################################################################")
OP=1
while OP!="FIN":
     OP=input("INGRESE EL UN ELECTRODOMESTICO QUE DESEA COMPRAR:")
     OP=OP.upper() #PARA CONVERTIR EL TEXTO INGRESADO A MAYUSCULAS
     if OP=="FIN":
         print("###################################################################")
         print("###  EL PROGRAMA A FINALIZADO #####")
         print("###  GRACIAS POR SU VISITA RESGRESE PRONTO  ####")
         print("###################################################################")
     else:
        if OP in TUPLA: #OPERACION 4 PERTENENCIA A UNA TUPLA
            print("###################################################################")
            print("ESTA COMPRANDO UN/(A) ",OP)
            PRE = int(input("POR FAVOR INGRESE EL PRECIO:"))
            if PRE in L:#OPERACION 5 PERTENECIA A UNA LISTA
                if PRE > 1400 and PRE < 2400:
                     PRE1 = PRE - (10 / 100) * PRE
                     print("POR LA COMPRA DE SU",OP,"TIENE UN DESCUENTO DEL 10%")
                     print("TOTAL A PAGAR:", PRE1)
                elif PRE > 2300 and PRE < 2900:
                    PRE2 = PRE - (20 / 100) * PRE
                    print("POR LA COMPRA DE SU",OP," TIENE UN DESCUENTO DEL 20%")
                    print("TOTAL A PAGAR:", PRE2)
                elif PRE > 2910 and PRE < 4500:
                    PRE3 = PRE - (30 / 100) * PRE
                    print("POR LA COMPRA DE SU",OP,"TIENE UN DESCUENTO DEL 30%")
                    print("TOTAL A PAGAR:", PRE3)
                elif PRE >= 4500 and PRE < 5100:
                    PRE4 = PRE - (40 / 100) * PRE
                    print("POR LA COMPRA DE SU",OP," TIENE UN DESCUENTO DEL 40%")
                    print("TOTAL A PAGAR:", PRE4)
                else:
                    print("###################################################################")
                    print("NO HAY DESCUENTO")
                    print("###################################################################")
            else:
             print("###################################################################")
             print("ESTE PRECIO NO ESTA REGISTRADO")
             print("###################################################################")
        else:
            print("###################################################################")
            print("LO SENTIMOS EL PRODUCTO QUE INGRESO NO ESTA HABILITADO")
            print("###################################################################")
