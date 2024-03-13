from datetime import date, datetime
from flask import Flask, render_template, request, flash, g
from forms import EmployForm
from config import DevelopmentConfig
from flask_wtf.csrf import CSRFProtect
from models import db , Clientes, Empleados

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
csrf = CSRFProtect(app)
        

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"),404

pizzas=[]
@app.route("/index", methods=["GET", "POST"])
def index():
    global pizzas
    clientes = EmployForm(request.form)
    ta = ""
    ingre = ""
    ing=0
    subtotal = 0
    cantidad = 0
    total = 0 
    day=""
    month=""
    Filtro = Clientes.query.filter(db.func.date(Clientes.fecha) == date.today()).all()
    totalDia = (sum([i.total for i in Filtro]) if Filtro else 0)
    show_filtro=False

    tam = { "Pequeña": 40,"Mediana": 80,"Grande": 120}
    ingredientes = {"jamon": 10,"pinia": 10,"champ": 10}
    
    if clientes.jamon.data:
        ing += ingredientes["jamon"]
        ingre += "Jamon "
    if clientes.pinia.data:
        ing += ingredientes["pinia"]
        ingre += " Piña "
    if clientes.champ.data:
        ing += ingredientes["champ"]
        ingre += " Champiñones"

    ta = clientes.tamanio.data
    
    meses = {
        'NA': 'NA',
        'January': 'Enero',
        'February': 'Febrero',
        'March': 'Marzo',
        'April': 'Abril',
        'May': 'Mayo',
        'June': 'Junio',
        'July': 'Julio',
        'August': 'Agosto',
        'September': 'Septiembre',
        'October': 'Octubre',
        'November': 'Noviembre',
        'December': 'Diciembre'
    }
    dias = {
        'NA': 'NA',
        'Monday': 'Lunes',
        'Tuesday': 'Martes',
        'Wednesday': 'Miercoles',
        'Thursday': 'Jueves',
        'Friday': 'Viernes',
        'Saturday': 'Sabado',
        'Sunday': 'Domingo'
    }
    
    if request.method == "POST":
        
        if request.form['btn'] == "Agregar":
            t= tam[clientes.tamanio.data]
            cantidad = clientes.cantidad.data
            subtotal = (t + ing) * cantidad
            fecha=clientes.fecha.data
            pizzas.append({
                "tamanio": ta,
                "ingredientes": ingre,
                "cantidad": cantidad,
                "subtotal": subtotal
            })
            flash("Se agrego el elemento")

        if request.form['btn'] == "Quitar":
            try:
                pizzas.pop(int(request.form['check'])-1)
                flash("Se elimino el elemento")
            except:
                pass

        if request.form['btn'] == 'Terminar':
            for i in pizzas:
                total += i["subtotal"]
            
            fecha = clientes.fecha.data
            day = fecha.strftime("%A")
            month = fecha.strftime("%B")                
            month = meses[month]
            day = dias[day]
            clientesObj = Clientes(
                nombre=clientes.nombre.data,
                direccion=clientes.direccion.data,
                telefono=clientes.telefono.data,
                total=total,
                fecha=fecha,
                dia=day,
                mes=month,
            )
            db.session.add(clientesObj)
            db.session.commit()
            flash("Pedido guardado")
            pizzas.clear()
            Filtro = Clientes.query.filter(db.func.date(Clientes.fecha) == date.today()).all()
            totalDia = (sum([i.total for i in Filtro]) if Filtro else 0)

            clientes.cantidad.data=None
            clientes.fecha.data=None
            clientes.jamon.data=None
            clientes.pinia.data=None
            clientes.champ.data=None
            clientes.tamanio.data=None
            clientes.nombre.data=None
            clientes.direccion.data=None
            clientes.telefono.data=None
        if request.form['btn'] == 'Filtrar':
            show_filtro=True
            fDia = clientes.day.data
            fMes = clientes.month.data
            fMes = meses[fMes]
            fDia = dias[fDia]
            print(fDia, fMes)
            if fDia == "NA" and fMes == "NA":
                pass
            elif fDia == "NA" and fMes != "NA":
                Filtro = Clientes.query.filter(Clientes.mes == fMes).all()
                totalDia = (sum([i.total for i in Filtro]) if Filtro else 0)
            elif fDia != "NA" and fMes == "NA":
                Filtro = Clientes.query.filter(Clientes.dia == fDia).all()
                totalDia = (sum([i.total for i in Filtro]) if Filtro else 0)
            else:
                Filtro = Clientes.query.filter(Clientes.dia == fDia, Clientes.mes == fMes).all()
                totalDia = (sum([i.total for i in Filtro]) if Filtro else 0)
        
        return render_template("index.html", form=clientes, pizzas=pizzas, Filtro=Filtro, totalDia=totalDia, show_filtro=show_filtro)        
        
    return render_template("index.html", form=clientes, Filtro=Filtro, show_filtro=show_filtro, totalDia=totalDia)


@app.route("/ABC_Completo", methods=["GET","POST"])
def ABC_Completo():
    employ_form= EmployForm(request.form)
    employObj = Empleados.query.all()
    return render_template("ABC_Completo.html", empleado=employ_form, empleados=employObj)
        

if __name__ == "__main__":
    csrf.init_app(app)
    db.init_app(app)

    with app.app_context():
        db.create_all()    
    app.run()
