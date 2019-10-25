LS=[]
LP=[]
TUPLA=("LUNES","MARTES","MIERCOLES","JUEVES","VIERNES")
SET={"SABADO","DOMINGO"}
OPC=1
while (OPC<5):
    print("##########################")
    print("#  INFORME DE TRABAJO  #")
    print("##########################")
    print("# 1. AGREGAR DIAS DE TRABAJO  #")
    print("# 2. AGREGAR HORAS         #")
    print("# 3. VERIFICACION DE SUELDO  #")
    print("# 4. LISTAR              #")
    print("# 5. SALIR               #")
    print("##########################")
    OPC=int(input("Ingrese una opcion:"))
    if OPC==1:
        print("##########################")
        NMD=int(input("CUANTOS DIAS TRABAJO DE LUNES-VIERNES:"))
        for i in range(NMD):
            DIA=input("INGRESE UN DIA DE LA SEMANA:")
            DIA=DIA.upper()
            if DIA in TUPLA:
                LS.append(DIA)
            else:
                print("INGRESE LOS DATOS CORRECTAMENTE")
        T=input("TRABAJO SABADO Y/O DOMINGO (SI/NO):")
        T=T.upper()
        if T=="SI":
            NUM=int(input("TRABAJO UNO O LOS DOS DIAS:"))
            if NUM<=len(SET) and NUM>0:
                for i in range(1,NUM+1):
                    DI=input("INGRESE EL DIA:")
                    DI=DI.upper()
                    if DI in SET:
                        LS.append(DI)
                    else:
                        print("INGRESE DATOS CORRECTOS")
            else:
                print("FUERA DE RANGO")
        elif T=="NO":
            print("########################################")
        else:
            print("NO ES CORRECTO")
        input("presione enter")
    if OPC==2:
         S=0
         for i in LS:
             SDS=int(input("HORAS DE TRABAJO POR DIA(segun los dias q trabajo):"))
             if SDS<9 and SDS>0:
                 S=S+SDS
                 LP.append(SDS)
             else:
                 print("ESTA PERMITIDO TRABAJAR 8 HORAS DIARIAS")
         input("presione enter")
    if OPC==3:
        SU=int(input("CUANTO GANA POR HORA:"))
        A=S*SU
        print("presione enter")
    if OPC==4:
        print("####################################")
        print("INFORME TOTAL")
        print("DURANTE LA SEMANA USTED TRABAJO LOS SIGUIENTES DIAS:",LS)
        print("USTED TRABAJO",S,"HORAS DURANTE LA SEMANA Y ESTA ES LA LISTA DE HORAS:",LP)
        print("SU SUELDO ES DE:",A)
        print("####################################")
        print("presione enter")





