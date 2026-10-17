from flask import Flask, render_template, request

app = Flask(__name__)

preguntas = [
    "¿Separas la basura para reciclar?",
    "¿Cierras la llave mientras te cepillas los dientes?",
    "¿Apagas las luces cuando no las necesitas?",
    "¿Usas bicicleta o transporte publico cuando puedes?",
    "¿Evitas utilizar bolsas y plasticos innecesarios?"
]


@app.route("/", methods=["GET", "POST"])
def inicio():
    resultado = None
    puntaje = 0
    recomendaciones = []

    if request.method == "POST":
        respuestas = []

        for i in range(len(preguntas)):
            respuesta = request.form.get("pregunta" + str(i))

            if respuesta not in ["2", "1", "0"]:
                return "Por favor, responde todas las preguntas."

            respuestas.append(int(respuesta))

        puntaje = sum(respuestas)

        if puntaje >= 8:
            resultado = "BAJO"
            recomendaciones = [
                "Sigue reciclando y separando los residuos.",
                "Continua ahorrando agua y energia.",
                "Invita a tu familia a cuidar el planeta."
            ]

        elif puntaje >= 4:
            resultado = "MEDIO"
            recomendaciones = [
                "Intenta reciclar todos los dias.",
                "Apaga las luces que no estes utilizando.",
                "Reduce el uso de bolsas plasticas."
            ]

        else:
            resultado = "ALTO"
            recomendaciones = [
                "Empieza a separar la basura para reciclar.",
                "Cierra la llave cuando no necesites agua.",
                "Apaga los aparatos y las luces que no uses.",
                "Camina o usa bicicleta en trayectos cortos."
            ]

    return render_template(
        "index.html",
        preguntas=preguntas,
        resultado=resultado,
        puntaje=puntaje,
        recomendaciones=recomendaciones
    )


if __name__ == "__main__":
    app.run(debug=True)
