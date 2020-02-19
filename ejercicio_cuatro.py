# ejercicio_cuatro
# ¿Tu número es mayor que el mío?

import random

def may_number(nu):
      ns = random.randrange(1000)
      if(nu>ns):
            print(f"Mi número era {ns}. El tuyo es mayor.")
      else:
            print(f"Mi número era {ns}. El mío es mayor.")            


number = int(input("Ingresa un número. Te diré si es mayor que el mío. "))
may_number(number)
