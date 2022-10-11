
class Login:

    def logIn():
        intentos = 3
        for i in range(0,3):
            try:
                pswdIn = int(input(f"""Ingresa PIN tienes {intentos} intentos """))
            except ValueError:
                print("Recuerda que el PIN es numerico")
                intentos = intentos-1
                continue
            if pswdIn == 1235:
                return True
            else:
                intentos = intentos -1

