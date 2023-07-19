#!/usr/bin/env python3
from tipo import TipoVariavel

class SymbolAlreadyDefinedException(Exception):
    "Símbolo já definido no escopo"
    pass


class Symbol:
    def __init__(self, type, value, dimensao):
        self.type = type
        self.value = value
        self.dimensao = dimensao

    def setType(self, type):
        self.type = type

    def setValue(self, value):
        self.value = value

    def setDimensao(self, dimensao):
        self.dimensao = dimensao

    def __repr__(self) -> str:
        if self.type == None:
            return f"Symbol(type={self.type}, register_type={self.type}, value={self.value}, dimensao={self.dimensao})"
        
        return f"Symbol(type={self.type.tipoBasico}, register_type={self.type.tipoRegistro}, value={self.value}, dimensao={self.dimensao})"


class Scope:
    def __init__(self):
        self.stack = []

    def newScope(self):
        self.stack.append({})

    def getScopes(self):
        return self.stack

    def peek(self):
        return self.stack[-1]

    def leaveScope(self):
        self.stack.pop()

    def add(self, key: str, type: TipoVariavel, dimensao: int) -> None:
        current_scope = self.stack[-1]

        if key in current_scope:
            raise SymbolAlreadyDefinedException
        else:
            current_scope[key] = Symbol(type, None, dimensao)

    def set(self, key: str, value) -> None:
        current_scope = self.stack[-1]

        if current_scope[key]:
            raise SymbolAlreadyDefinedException
        else:
            current_scope[key].setValue(value)

    def find(self, key: str) -> Symbol | None:
        for scope in self.stack:
            if key in scope:
                symbol = scope[key]

                if symbol:
                    return symbol
        return None
    
    def findGlobalDecl(self, key: str) -> Symbol | None:
        for scope in self.stack:
            if key in scope:
                if scope[key].type.tipoBasico == "funcao" or scope[key].type.tipoBasico == "procedimento":
                    return scope
        return None
