import os 
import json
import funciones.globales as gf
import modules.corefiles as cf
import ui.uimedicos as uim

def newmedico():
    title =  """
    *********************
    *REGISTRO DE MEDICOS*
    *********************
    """
    gf.borar_pantalla()
    print(title)
    identificacion = input("ingrese numero de identificacion : ")
    nomb_apell = input("ingrese su  nombre y apellido : ")
    corre_ele = input("ingrese su correo eletronico : ")
    num_consul = input("ingrese numero de consultorio : ")
    hora_atencion = input("ingrese el horario del medico : ")
    medicos = {'identificacion': identificacion,
               'nombre y apellido': nomb_apell,
               'numero de consultorio':num_consul,
               'horario de atencion': hora_atencion,
               'correo eletronico': corre_ele,}
    
    cf.AddData('data',identificacion,medicos)
    gf.centromedico.get('data').update({identificacion:medicos})
    if(bool(input('Desea registrar otro medico S(Si) o Enter(No)'))):
        newmedico()
    else:
        uim.menumedicos(0)

def  SearchData():
    criterio = input('ingrese el Nro identificacion del medico')
    data=gf.centromedico.get('data').get(criterio)
    return data 
def MofifyData():
    datamedico = SearchData()
    idetificacion,nomb_apell,corre_ele,num_consul = datamedico.values()
    for key in datamedico.keys():
        if (key != 'identificacion' and key != 'notas'):
            if(bool(input(f'desea modificar el {key} s(si) o Enter no'))):
               datamedico[key] = input (f'ingrese el nuevo valor para {key} :')
    gf.centromedico.get('data').update({idetificacion:datamedico})
    cf.UpdateFile(gf.centromedico)
    uim.Menumedicos(0)           


