from abc import ABC, abstractmethod


class Televisao:

    state = None

    def __init__(self, state) -> None:
        self.mudar_state(state)
        self.volume = 30


    def mudar_state(self, state):

        self.state = state
        self.state.Televisao = self


    def ligar_desligar(self):
        self.state.ligar_desligar()

    def silenciar(self):
        self.state.silenciar()



class State(ABC):


    @property
    def Televisao(self) -> Televisao:
        return self.televisao

    @Televisao.setter
    def Televisao(self, Televisao: Televisao) -> None:
        self.televisao = Televisao

    @abstractmethod
    def ligar_desligar(self) -> None:
        pass

    @abstractmethod
    def silenciar (self) -> None:
        pass


class Desligado(State):
    def ligar_desligar(self) -> None:
        print("A tv desligada vai ligar")
        self.Televisao.mudar_state(Ligado())
    
    def silenciar(self) -> None:
        print("A tv não consegue silenciar enquanto desligada")
    
    def __str__():
        return "a tv está desligada"



class Ligado(State):
    def ligar_desligar(self) -> None:
        print("A tv ligada vai desligar")
        self.Televisao.mudar_state(Desligado())

    def silenciar(self):
        print("a tv vai ficar sem som")
        self.Televisao.volume = 0
        self.Televisao.mudar_state(Silenciado())
    
    def __str__():
        return "a tv está ligada"


class Silenciado(State):
    def ligar_desligar(self) -> None:
        print("A tv ligada vai desligar")
        self.Televisao.mudar_state(Desligado())
    
    def silenciar(self):
        print("a tv vai voltar a ter som")
        self.Televisao.volume = 30
        self.Televisao.mudar_state(Ligado())

        def __str__():
            return "a tv está ligada e sem volume"


if __name__ == "__main__":

    Televisao = Televisao(Desligado())
    Televisao.ligar_desligar()
    Televisao.ligar_desligar()
    Televisao.silenciar()
    Televisao.ligar_desligar()
    Televisao.silenciar()
    Televisao.silenciar()
    Televisao.ligar_desligar()
    
