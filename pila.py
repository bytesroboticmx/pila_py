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
pila.push(10)
pila.push(7)
pila.push(8)
pila.push(3)
print(pila.pop())   
print(pila.pop())
print(pila.peek())
print("Esta vacia: ", pila.esta_vacia())
print("Tamaño de pila: ", pila.tamano())
print(pila.pop())
print(pila.peek())
print("Esta vacia: ", pila.esta_vacia())
print("Tamaño de pila: ", pila.tamano())
print(pila.peek())
#FIN
