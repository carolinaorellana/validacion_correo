from aplicacion.config.mysqlconnection import connectToMySQL #siempre importar la conección con la base de datos
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class Email:
    base_datos= "correos"
    def __init__(self,data):
        self.id = data ['id']
        self.email = data['direccion_correo']
        self.created_at= data ['created_at']
        self.updated_at= data ['updated_at']
    

    #obtener todos los correos
    @classmethod
    def todos_los_correos(cls):
        consulta = "SELECT * FROM correos"
        resultado= connectToMySQL (cls.base_datos).query_db(consulta)
        todos_correos=[]
        for correo in resultado:
            todos_correos.append(cls(correo))
        return todos_correos

    #obntener un solo correo
    @classmethod
    def un_correo(cls, data):
        consulta = "SELECT * FROM correos WHERE id = %(id)s"
        resultado= connectToMySQL (cls.base_datos).query_db(consulta,data)
        return cls(resultado[0])


    #INSERTAR UN CORREO en la base de datos
    @classmethod
    def crear_correo(cls,data):
        consulta = "INSERT INTO correos (direccion_correo) VALUES (%(direccion_correo)s);"
        resultado = connectToMySQL(cls.base_datos).query_db(consulta,data)
        return resultado


    #obntener un solo correo
    @classmethod
    def revisar_correo_existente(cls, data):
        consulta = "SELECT * FROM correos WHERE direccion_correo = %(direccion_correo)s"
        resultado= connectToMySQL (cls.base_datos).query_db(consulta,data)
        return resultado
    
    #Eliminar un correo de la base de datos
    @classmethod
    def eliminar_correo_existente(cls, data):
        consulta = "DELETE FROM correos WHERE correos.id = %(id)s"
        resultado= connectToMySQL (cls.base_datos).query_db(consulta,data)
        return resultado

    @staticmethod
    def validar_correo(correo):
        is_valid = True
        # prueba si un campo coincide con el patrón
        if not EMAIL_REGEX.match(correo['direccion_correo']): 
            flash("Invalid email address!")
            is_valid = False

        if len(Email.revisar_correo_existente(correo))>0:
            flash("Invalid email address ya existe!")
            is_valid = False
        return is_valid

