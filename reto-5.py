import unittest
from Geometria_.model.Geometria import Geometria
from Geometria_.view.View import View

class TestGeometria(unittest.TestCase):
    def setUp(self):
        self.element = Geometria(2.00, 3.00, 4.00)

    def testCuadrado(self):
        self.element.set_figuraName(1)
        self.assertEqual(self.element.figuraName, 'Cuadrado')

    def testAreaCuadrado(self):
        self.assertEqual(self.element.switch(1), 4.00)

    def testCirculo(self):
        self.element.set_figuraName(2)
        self.assertEqual(self.element.figuraName, 'Circulo')

    def testAreaCirculo(self):
        self.assertEqual(self.element.switch(2), 12.5664)

    def testTiangulo(self):
        self.element.set_figuraName(3)
        self.assertEqual(self.element.figuraName, 'Tiangulo')

    def testAreaTiangulo(self):
        self.assertEqual(self.element.switch(3), 3.0)

    def testRectangulo(self):
        self.element.set_figuraName(4)
        self.assertEqual(self.element.figuraName, 'Rectangulo')

    def testAreaRectangulo(self):
        self.assertEqual(self.element.switch(4), 6.0)

    def testPentagono(self):
        self.element.set_figuraName(5)
        self.assertEqual(self.element.figuraName, 'Pentagono')

    def testAreaPentagono(self):
        self.assertEqual(self.element.switch(5), 3.0)

    def testRombo(self):
        self.element.set_figuraName(6)
        self.assertEqual(self.element.figuraName, 'Rombo')

    def testAreaRombo(self):
        self.assertEqual(self.element.switch(6), 3.0)

    def testRomboide(self):
        self.element.set_figuraName(7)
        self.assertEqual(self.element.figuraName, 'Romboide')

    def testAreaRomboide(self):
        self.assertEqual(self.element.switch(7), 6.0)

    def testTrapecio(self):
        self.element.set_figuraName(8)
        self.assertEqual(self.element.figuraName, 'Trapecio')

    def testAreaTrapecio(self):
        self.assertEqual(self.element.switch(8), 10.0)


    pass

if __name__ == '__main__':
    unittest.main()