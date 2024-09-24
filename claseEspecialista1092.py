print("EXAMEN Alondra Ramirez Sandoval 1092")
print("clase Especialistas")

class Especialista1092:
    #creacion de atributos en 0
    id_dr=0
    nombre=0
    telefono=0
    correo=0
    especialidad=0
    consultorio=0
    horario=0

#zona de funciones 
    def mostrardatos1092(self):
        print(f"")
    def lista_dr1092(self):
        dr_nombre = ["Sebastian","Jimena","Yuliana","Ricardo","Melissa"]
        print(dr_nombre)
        for dr_n in dr_nombre:
            print(dr_n)
    def tupla_dr1092(self):
        dr_esp = ("Pediatria","Nutriologia","Ginecologia","Cardiologia","General")
        print(dr_esp)
        for dr_e in dr_esp:
            print(dr_e)
    def diccionario_dr1092(self):
        dr_con = {
        "Consultorio 1" : "de 8:00 am - 3:30 pm",
        "Consultorio 2"  : "de 2:00 pm - 7:00 pm",
        "Consultorio 3"  : "de 10:00 am - 4:40 pm",
        "Consultorio 4"  : "de 11:00 am - 6:30 pm",
        "Consultorio 5"  : "de 8:00 am - 4:40 pm"
    }
        for con,hora in dr_con.items():
            print(con, " : " ,hora)

#zona de objetos
especialista=Especialista1092()

#zona para llamar funciones 
especialista.lista_dr1092()
especialista.tupla_dr1092()
especialista.diccionario_dr1092()

#Zona para mostrar datos 
especialista.id_dr= 1092
especialista.nombre="Sebastian"
especialista.telefono= 6561049965
especialista.correo="sebasnutriologo@gmail.com"
especialista.especialidad="Pediatria"
especialista.consultorio="Consultorio 1"
especialista.horario="de 8:00 am - 3:30 pm"
print("------ Datos del Especialista-----")
print(f"ID del especialista: {especialista.id_dr}")
print(f"Le atiende el Doctor: {especialista.nombre}")
print(f"Numero de contacto: {especialista.telefono}")
print(f"Correo electronico: {especialista.correo}")
print(f"Especialista en: {especialista.especialidad}")
print(f"Consultorio: {especialista.consultorio}")
print(f"En un horario: {especialista.horario}")