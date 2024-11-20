import random


pogoda = random.choice(['pada', 'nie pada'])


while input("Czy pada deszcz? (pada/nie pada): ").lower() != pogoda:
    print("Nie zgadłeś, spróbuj jeszcze raz.")
# Używamy .lower(), aby upewnić się, że można wpisać odpowiedź bez względu na wielkość liter (np. "PADA" będzie traktowane tak samo jak "pada")
print("Brawo! Zgadłeś!")
