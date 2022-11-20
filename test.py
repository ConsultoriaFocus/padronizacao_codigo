class Pilha:
    def __init__(self, v = []):
        self.__v:list = v
    def __setattr__(self, __name, __value):
        if __name == "_Pilha__v":
            if not isinstance(__value, list):
                raise Exception("valor invalido")
        object.__setattr__(self, __name, __value)
    def __str__(self):
        return str(self.__v)
    def __getitem__(self, i):
        return self.__v[i]
    def add(self, val):
        self.__v.append(val)
    def pop(self):
        self.__v.pop()


