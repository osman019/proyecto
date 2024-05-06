import os 
import json
import funciones.globales as gf
import modules.corefiles as cf
import ui.uipacientes as up

def newpaciente():
    title =  """
    ***********************
    *REGISTRO DE PACIENTES*
    ***********************
    """
    gf.borar_pantalla()
    print(title)
    identificacion = input("ingrese numero de identificacion : ")
    nomb_apell = input("ingrese su  nombre y apellidos : ")
    numero_tele = input("ingrese su numero telefonico : ")
    numero_celu = input("ingrese su numero de celular : ")
    fe_nacimiento = input("ingrese su fecha de nacimiento : ")
    edad = input ("ingrese su edad : ")
    genero = input("ingrese su genero : ")


    pacientes = {'identificacion': identificacion,
                 'nombre y apellidos': nomb_apell,
                 'numero telefonico' : numero_tele,
                 'numero de celular' : numero_celu,
                 'fecha de nacimiento': fe_nacimiento,
                 'edad': edad,
                 'genero': genero}
             
    
    cf.AddData('datapacientes',identificacion,pacientes)
    gf.centromedico.get('datapacientes').update({identificacion:pacientes})
    if(bool(input(
        'Desea registrar otro paciente S(Si) o Enter(No)'))):
        newpaciente()
    else:
        up.MenuPacinetes(0)

def SearchData():
    input('ingrese la identificacion del paciente: ')
    data=gf.centromedico.get('datapacientes')
    print(data)
    return data 


def ModifyData():
   datapacientes = SearchData(datapacientes)
   if datapacientes:
      print("Datos actuales del paciente:")
      datapacientes = ['nombre y apellidos','identificacion', 'numero telefonico', 'numero de celular', 'fecha de nacimiento', 'edad','genero']
      for key in datapacientes:
         if bool(input(f"Desea modificar {key}? (Sí/Si o Enter para No): ")):
               new_value = input(f"Ingrese el nuevo valor para {key}: ")
               datapacientes = new_value

      gf.centromedico.get('datapacientes').update({datapacientes:'datapacientes'})
      cf.UpdateFile(gf.centromedico)
      print("Datos del paciente actualizados correctamente.")
   else:
        print("No se encontró ningún paciente con la identificación proporcionada.")