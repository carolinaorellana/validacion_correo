from aplicacion import app
from aplicacion.models.modelo import Email
from flask import render_template, request, redirect

@app.route('/')
def inicio():
    return render_template('registro.html')

@app.route('/registrar',  methods=['POST'])
def registrar():
    if not Email.validar_correo(request.form):
        # redirigimos a la plantilla con el formulario
        return redirect('/')
    print(request.form, "ESTO ES LO QUE CONTIENE EL FORMULARIO")
    data ={
        "direccion_correo": request.form['direccion_correo']
    }
    ultimo_id=Email.crear_correo(data)
    return redirect (f"/registro_exitoso/{ultimo_id}")

@app.route('/registro_exitoso/<int:id>')
def mostrar(id):
    todos_los_correos=Email.todos_los_correos()
    data ={
        "id":id
    }
    ultimo_correo=Email.un_correo(data)
    return render_template('mostrar.html', todos_los_correos=todos_los_correos, ultimo_correo=ultimo_correo)

@app.route ("/eliminar/<int:id>")
def eliminar_correo( id):
    data={
        "id":id
    }
    Email.eliminar_correo_existente(data)
    
    return redirect ('/')
