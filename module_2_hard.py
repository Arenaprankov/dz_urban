def generate_password(a):
  password = ""
  for b in range(1, a):
    for j in range(b + 1, a + 1):
      if (b + c) % a == 0:
        password += str(b) + str(c)
  return password
a = int(input("Введи число от 3 до 20: "))
if 3 <= a <= 20:
  password = generate_password(n)
  print(f"Пароль для числа {a}: {password}")
else:
  print("Неправильное число! Введи число от 3 до 20.")
