#!/usr/bin/env python3


class SymbolAlreadyDefinedException(Exception):
    "Símbolo já definido no escopo"
    pass


class Symbol:
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def setType(self, type):
        self.type = type

    def setValue(self, value):
        self.value = value

    def __repr__(self) -> str:
        return f"({self.type}, {self.value})"


class Scope:
    def __init__(self):
        self.stack = []

    def newScope(self):
        self.stack.append({})

    def peek(self):
        return self.stack[-1]

    def leaveScope(self):
        self.stack.pop()

    def add(self, key: str, type: str) -> None:
        current_scope = self.stack[-1]

        if key in current_scope:
            raise SymbolAlreadyDefinedException
        else:
            current_scope[key] = Symbol(type, None)

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
