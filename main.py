import random
import string


def generate_password():
    # Solicita a palavra base para o usuário
    base_word = input("Insira a palavra base da senha: ")

    # Verifica se a palavra base contém letras e números
    while not (any(c.isalpha() for c in base_word) and any(c.isdigit() for c in base_word)):
        print("A palavra base deve conter pelo menos uma letra e um número.")
        base_word = input("Insira a palavra base da senha: ")

    # Adicione caracteres especiais que podem ser usados ​​na senha
    special_chars = '!@#$%^&*()_+-=[]{}|\\;:\'",.<>/?'

    # Embaralhe a palavra base e adicione números e caracteres especiais aleatoriamente
    shuffled_word = ''.join(random.sample(base_word, len(base_word)))
    password = shuffled_word + random.choice(string.digits) + random.choice(special_chars)

    # Adicione caracteres aleatórios adicionais até que a senha atinja o comprimento desejado
    password_length = int(input("Insira o tamanho da senha desejado: "))
    while len(password) < password_length:
        password += random.choice(string.ascii_letters + string.digits + special_chars)

    return password


def generate_multiple_passwords():
    num_passwords = int(input("Insira o número de senhas desejado: "))
    password_list = []
    for i in range(num_passwords):
        password = generate_password()
        while password in password_list:
            password = generate_password()
        password_list.append(password)
    return password_list


def main():
    print("Escolha uma opção:")
    print("1 - Gerar uma senha")
    print("2 - Gerar várias senhas")
    option = input("Opção escolhida: ")
    if option == "1":
        password = generate_password()
        print("Senha gerada:", password)
    elif option == "2":
        password_list = generate_multiple_passwords()
        print("Senhas geradas:")
        for password in password_list:
            print(password)
    else:
        print("Opção inválida")


if __name__ == "__main__":
    main()