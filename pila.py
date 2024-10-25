class Pila:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if not self.esta_vacia():
            return self.items.pop()
        else:
            return "La pila está vacía"
    
    def peek(self):
        if not self.esta_vacia():
            return self.items[-1]
        else:
            return "La pila está vacía"
    
    def esta_vacia(self):
        return len(self.items) == 0
    
    def tamano(self):
        return len(self.items)

# Ejemplo de uso de la pila
pila = Pila()
pila.push(893)
pila.push(87)
pila.push(9)
pila.push(67)
pila.push(22)
pila.push(90)
pila.push(233)
pila.push(6)
pila.push(11)
pila.push(34)
print(pila.pop())   
print(pila.pop())
print(pila.peek())
pila.push(198)
pila.push(202)
print("Esta vacia: ", pila.esta_vacia())
print("Tamaño de pila: ", pila.tamano())
print(pila.pop())
print(pila.peek())
pila.push(17)
pila.push(66)
print("Esta vacia: ", pila.esta_vacia())
print(pila.pop())
print(pila.peek())
print("Tamaño de pila: ", pila.tamano())
#FIN
