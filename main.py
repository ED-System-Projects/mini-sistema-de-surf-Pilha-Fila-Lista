from surfista import Surfista
from pilha import PilhaEncadeada
from fila import FilaEncadeada


pi = PilhaEncadeada()
fi = FilaEncadeada()

surfista1 = Surfista("Entrei Primeiro - Adriana", 0, 89, 123456)
surfista2 = Surfista("Entrei Ultimo - Diego", 0, 19, 654321)
surfista3 = Surfista("Entrei Primeiro - John", 0, 19, 654321)
surfista4 = Surfista("Entrei Ultimo - Roose", 0, 19, 654321)

pi.inserir(surfista1)
pi.inserir(surfista2)

fi.inserir(surfista3)
fi.inserir(surfista4)

print(pi)
print(fi)
