pada = False
licznik_nie = 0


while not pada:
    odpowiedz = input("Czy pada? (tak/nie/nie wiem): ").lower()
    
    if odpowiedz == "tak":
        pada = True
    elif odpowiedz == "nie":
        licznik_nie += 1
    elif odpowiedz == "nie wiem":
        print("To wyjdź na zewnątrz i się dowiedz.")
    else:
        print("Nie rozumiem odpowiedzi. Proszę odpowiedzieć 'tak', 'nie' lub 'nie wiem'.")
        

print(f"Liczba odpowiedzi 'nie': {licznik_nie}")
