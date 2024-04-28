class Tateti:
  def __init__(self):
    self.turno = True # True -> Jugador X, False -> Jugador 0
    self.seguirJugando = True
    self.tablero = [
      ["1", 2, 3],
      [4, 5, 6],
      [7, 8, 9]
    ]

  def jugar(self):
    while(self.seguirJugando is True):
      self.anunciar("elija alguna posicion: \n")
      self.mostrarTablero()
      self.jugarPieza()
      if (self.hayGanador() is True):
        self.terminarJuego()
        continue
      self.cambiarTurno()
  
  def mostrarTablero(self):
    for i in range(0, len(self.tablero)):
      for j in range(0, len(self.tablero[i])):
        print(self.tablero[i][j], end=" ")
        if (self.tablero.index(self.tablero[j]) != len(self.tablero) - 1):
          print("|", end=" ")
      print("\n_ _ _ _ _\n")


  def jugarPieza(self):
    posicion = int(input())
    
    ficha = "X" if self.turno else "0"
    posicionInicial = 1
    for i in range(0, len(self.tablero)):
      for j in range(0, len(self.tablero[i])):
        if (posicionInicial == posicion):
          self.tablero[i][j] = ficha
        posicionInicial+=1

  def cambiarTurno(self):
    self.turno = not self.turno

  def anunciar(self, mensaje):
    print(mensaje)

  def terminarJuego(self):
    self.anunciar(f"el ganador es {'X' if self.turno is True else 'O'}")
    self.mostrarTablero()
    
    self.anunciar("desea seguir jugando? 1 = si, 2 = no")
    respuesta = int(input())
    self.seguirJugando = respuesta == 1
    
    if (respuesta == 1):
      self.reiniciarPartida()
    else:
      self.anunciar("Gracias por jugar!")
  
  def hayGanador(self):
    #comprobar filas
    if (self.tablero[0][0] == self.tablero[0][1] == self.tablero[0][2]):
      return True
    if (self.tablero[1][0] == self.tablero[1][1] == self.tablero[1][2]):
      return True
    if (self.tablero[2][0] == self.tablero[2][1] == self.tablero[2][2]):
      return True

    # Comprobar columnas
    if (self.tablero[0][0] == self.tablero[1][0] == self.tablero[2][0]):
      return True
    if (self.tablero[0][1] == self.tablero[1][1] == self.tablero[2][1]):
      return True
    if (self.tablero[0][2] == self.tablero[1][2] == self.tablero[2][2]):
      return True

    # Comprobar diagonales
    if (self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2]):
      return True
    if (self.tablero[0][2] == self.tablero[1][1] == self.tablero[2][0]):
      return True
    return False
    
  def reiniciarPartida(self):
    self.tablero = [
      ["1", 2, 3],
      [4, 5, 6],
      [7, 8, 9]
    ]
    self.turno = True
    
tateti = Tateti()
tateti.mostrarTablero()
tateti.jugar()