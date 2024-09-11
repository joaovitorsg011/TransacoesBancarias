from typing import List
from Pix import Pix

class Cliente:
    def __init__(self, nome: str, cpf: str, saldo: float):
        self.nome = nome
        self.__cpf = cpf
        self.__saldo = saldo
        self.__extrato: List[Pix] = []  

    def get_saldo(self) -> float:
        return self.__saldo

    def get_extrato(self) -> List[Pix]:
        return self.__extrato

    def get_cpf(self) -> str:
        return f"{self.__cpf[:3]}.xxx.xxx-{self.__cpf[-2:]}" 

    def depositar(self, valor: float):
        self.__saldo += valor

    def retirar(self, valor: float):
        self.__saldo -= valor

    def realizar_pix(self, valor: float, destinatario: 'Cliente'):
        pix = Pix(self, destinatario, valor)
        pix.executar() 

    def registrar_transacao(self, transacao: Pix):
        self.__extrato.append(transacao)
