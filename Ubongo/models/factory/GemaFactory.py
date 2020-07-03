from models.Gema import Gema

class GemaFactory:

    @staticmethod
    def crearGema(x, y, idGema, window):
        gemaCreada = Gema(x, y, idGema, window)
        return gemaCreada