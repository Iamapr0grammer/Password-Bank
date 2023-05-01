from cryptography.fernet import Fernet

language = input("Press 1 if You would like to play this app in english | Naciśnij 2 jeśli chcesz przeglądać tą aplikację w języku polskim: ")


# domyślnie język będzie polski, wciskając 1 będzie zmieniony na Angielski
z_pytanie_o_master_password = "Podaj Hasło Administratora: "
z_nazwa_uzytkownika = "Podaj Nazwę Użytkownika: "
z_notatka = "Podaj osobistą notatkę do tego konta: "
z_haslo = "Podaj Hasło do zapamiętania: "
z_co_robi = "Wpisz D by dodać nowe hasło, albo wpisz C aby przeczytać istniejące hasła"
nazwa_uzytkownika = "Nazwa Użytkownika: "
note = "Personalna Notatka: "
password = "Hasło: "
leave = "Wciśnij Q by wyjść"
if language == str(1):
    # English
    # z_ na początku oznacza zapytanie
    z_pytanie_o_master_password = "What is the master password?: "
    z_nazwa_uzytkownika = "Give Your Username: "
    z_notatka = "Give Your personal note about this account: "
    z_haslo = "Give password to remember: "
    z_co_robi = "Press A to add a new password, or press R to read existing passwords"
    nazwa_uzytkownika = "Username: "
    note = "Personal Note: "
    password = "Password: "
    leave = "Press Q to leave"
elif language == str(2):
    # Polski
    pass
else:
    # miejsce na potencjalne inne jeżyki w przyszłości
    pass

master_password = input(z_pytanie_o_master_password)

# def load_key():
#     file = open("key.key", "rb")
#     key = file.read()
#     file.close()
#     return key
# key = load_key() + master_password.encode()

klucz = b'cu5Z1-FNAox7gXzRUxOryaWuQcNlgztQKB83F3FDk1A='
fer = Fernet(klucz)

#print("Klucz: ", klucz)


# def write_key():
#     key = Fernet.generate_key()
#     with open("key.key", "wb") as key_file:
#         key_file.write(key)


#print("Master password is:", master_password)

def view(master_password,nazwa_uzytkownika,persnote,pasw):
    with open("password.txt", "r") as f:
        for line in f.readlines():
            #print(line.rstrip())
            # dodane .rstrip() by nie wyświetlały się niepotrzebne przerwy pomiędzy linijkami

            # rozdzielenie nazwy użytkownika od hasła
            data = line.rstrip()
            user, master, note, password = data.split("|")
            haslo = fer.decrypt(master.encode()).decode()

            # sprawdzenie, czy master password się zgadza
            if haslo == master_password:
                print(nazwa_uzytkownika, user, " | ", persnote, fer.decrypt(note.encode()).decode(),  " | ", pasw, fer.decrypt(password.encode()).decode())


def add(master_password,z_nazwa_uzytkownika,z_haslo,z_notatka):
    name = input(z_nazwa_uzytkownika)
    note = input(z_notatka)
    password = input(z_haslo)

    with open("password.txt", "a") as f:
        f.write(name + "|" + fer.encrypt(master_password.encode()).decode() + "|"+ fer.encrypt(note.encode()).decode() + "|" + fer.encrypt(password.encode()).decode() + "\n")


while True:
    print(leave)
    mode = input(z_co_robi)
    if mode == "q" or mode == "Q":
        break
    if mode == "d" or mode == "D" or mode == "a" or mode == "A":
        add(master_password, z_nazwa_uzytkownika, z_haslo, z_notatka)
    if mode == "c" or mode == "C" or mode == "r" or mode == "R":
        view(master_password, nazwa_uzytkownika, note,password)
    else:
        #print("invalid mode")
        continue