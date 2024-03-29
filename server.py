# Universidad Politécnica de Chiapas
# Desarrollo de Sistemas Inteligentes 9 - A
from flask import Flask # Dependencia del servidor
from utils.juego import Juego
import json

app = Flask(__name__)

juego = Juego()
jugador1 = None
jugador2 = None

@app.route('/')
def welcome():
    return "Bienvenido al juego del gato"

@app.route('/setplayer1')
def setplayer1():
    global jugador1
    puedoTomarElTurno, caracterP1 = juego.setPlayer1()
    if puedoTomarElTurno:
        jugador1 = caracterP1
        print(jugador1)
        return {
            "status": "Success",
            "mensaje": "Eres el jugador 1, te toca la X"
        }
    else:
        return {
            "status": "Error",
            "mensaje": "No puedes tomar este turno"
        }

@app.route('/setplayer2')
def setplayer2():
    global jugador2
    puedoTomarElTurno, caracterP2 = juego.setPlayer2()
    if puedoTomarElTurno:
        jugador2 = caracterP2
        print(jugador2)
        return {
            "status": "Success",
            "mensaje": "Eres el jugador 2, te toca la O"
        }
    else:
        return {
            "status": "Error",
            "mensaje": "No puedes tomar este turno"
        }

@app.route('/tablero')
def getTablero():
    print(juego.getBoard())
    return json.dumps({"tablero": juego.getBoard()})
    # return {
    #     "tablero": juego.getBoard().toList()
    # }

@app.route('/tirar/<x>/<y>')
def tirar(x, y):
    _x = int(x)
    _y = int(y)
    print(_x)
    print(_y)
    tiroAceptado,mensaje = juego.tirar(_x, _y)
    print(f'\n\nTiro aceptado = {tiroAceptado}')
    print(f'Mensaje = {mensaje}\n')

    if tiroAceptado:
        yaGano = juego.determinarGanador(jugador1)
        print(f'Gano? = {yaGano}\n')
        juego.cambiarTurno()
        return {
            "status": tiroAceptado,
            "mensaje": mensaje,
            "yaGano": yaGano
        }
    else:
        return {
            "status": "Error",
            "mensaje": "No puedes tirar aqui",
            "yaGano": False
        }

@app.route('/puedoTirar/<ficha>')
def puedoTirar(ficha):
    puede = juego.yaMeToca(ficha)
    return {
        "puede": puede
    }