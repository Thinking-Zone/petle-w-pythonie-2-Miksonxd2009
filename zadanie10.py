# Zadanie:
# Napisz program, który zliczy, ile liczb parzystych znajduje się w zakresie od 1 do 50 (włącznie).
# Program powinien wypisać wynik po zakończeniu pętli.

print("A pod spodem rozwiązanie tego zadanka, napisane w Pythonie :)")

# Rozwiązanie:


licznik_parzystych = 0


for liczba in range(1, 51):
    if liczba % 2 == 0: 
        licznik_parzystych += 1 
