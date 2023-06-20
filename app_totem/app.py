from flask import Flask, render_template, request, url_for, redirect
import database as db
app = Flask(__name__)


@app.route("/")
def inicio():
    return render_template("totem.html")


@app.route("/solicitud-transfer")
def formulario():
    return render_template("crear.html")


@app.route("/crear", methods=["POST"])
def crear():

    v_destino = request.form.get("destino")
    v_cantidad_puertas = request.form.get("cantidad_puertas")
    v_tipo_vehiculo = request.form.get("tipo_vehiculo")

    cursor = db.DATABASE.cursor()
    cursor.execute("INSERT INTO viajes (destino, cantidad_puertas, tipo_vehiculo) VALUES(%s,%s,%s)",
                   (v_destino, v_cantidad_puertas, v_tipo_vehiculo))

    db.DATABASE.commit()

    print("Se creo el registro de manera exitosa ;)")
    return redirect(url_for("inicio"))


if (__name__ == "__main__"):
    app.run(debug=True)
