from models.Juego import Juego
import unittest

class Test_Juego(unittest.TestCase):
        def test_asignarPuzzle(self):
                jugadores = []
                juego = Juego(jugadores,"facil" )
                for i in range(74):
                        juego.mazoPuzzles.append(i)
                self.assertEqual(len(juego.asignarPuzzles("facil")), 9)
                self.assertEqual(len(juego.asignarPuzzles("facil")), 9)
                self.assertEqual(len(juego.asignarPuzzles("facil")), 9)
                self.assertEqual(len(juego.asignarPuzzles("facil")), 9)
                self.assertEqual(len(juego.asignarPuzzles("facil")), 9)


if __name__ == '__main__':
    unittest.main()