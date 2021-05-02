#funcion para conseguir que mes será dentro de determinada cantidad de meses (suma_meses), partiendo de determindado mes (mes_act)

def mes_siguiente(mes_act,suma_meses):
    mes_act=mes_act%12
    rta=(mes_act + suma_meses%12)%12
    if rta==1:
        return "enero"
    if rta==2:
        return "febrero"
    if rta==3:
        return "marzo"
    if rta==4:
        return "abril"
    if rta==5:
        return "mayo"
    if rta==6:
        return "junio"
    if rta==7:
        return "julio"
    if rta==8:
        return "agosto"
    if rta==9:
        return "septiembre"
    if rta==10:
        return "octubre"
    if rta==11:
        return "noviembre"
    if rta==0:
        return "diciembre"

print mes_siguiente(5,16)



