from wtforms import DateField, Form, SelectField
from wtforms import validators
from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, IntegerField, FloatField, BooleanField, RadioField
from wtforms import EmailField
# Aqui agregaremos los campos que sean obligatorios y el email
from wtforms.validators import DataRequired, Email, Length

class EmployForm(Form):
    id = IntegerField('', [validators.number_range(min=1, max=20, message="Valor no valido")])
    nombre=StringField("Nombre Completo", [validators.DataRequired(message="El nombre es requerido"), validators.length(min=4,max=40, message="Ingresa un nombre de entre 4 a 20 letras")])
    direccion=StringField("Dirección", [validators.DataRequired(message="La dirección es requerida"), validators.length(min=10,max=100, message="Ingresa una dirección valida")])
    telefono=StringField("Telefono", [validators.DataRequired(message="El campo es requerido"), validators.length(min=10,max=10, message="El telefono debe tener 10 digitos")])
    tamanio = RadioField('Tamaño', choices=[('Pequeña', 'Pequeña $40'), ('Mediana', 'Mediana $80'), ('Grande', 'Grande $120')], default=False)
    # email=EmailField("Email", [validators.DataRequired(message=("El campo es requerido")), validators.Email('Ingrese un correo valido') ])
    # sueldo=FloatField("Sueldo", [validators.DataRequired(message="El campo es requerido")])
    # Checkbox para ingredientes
    jamon = BooleanField("Jamon $10", default=False)
    pinia = BooleanField("Piña $10", default=False)
    champ = BooleanField("Champiñones $10", default=False)
    cantidad = IntegerField("Cantidad de pizzas", [validators.DataRequired(message="El campo es requerido"), validators.number_range(min=1, max=1000, message="Valor no valido")])
    day = SelectField('', choices=[('NA','N/A'), ('Monday', 'Lunes'), ('Tuesday', 'Martes'), ('Wednesday', 'Miercoles'), ('Thursday', 'Jueves'), ('Friday', 'Viernes'), ('Saturday', 'Sabado'), ('Sunday', 'Domingo')])
    month = SelectField('', choices=[('NA','N/A'), ('January', 'Enero'), ('February', 'Febrero'), ('March', 'Marzo'), ('April', 'Abril'), ('May', 'Mayo'), ('June', 'Junio'), ('July', 'Julio'), ('August', 'Agosto'), ('September', 'Septiembre'), ('October', 'Octubre'), ('November', 'Noviembre'), ('December', 'Diciembre')])
    fecha = DateField('Fecha pedido', format='%Y-%m-%d', validators=[DataRequired(message="El campo es requerido")])



