trassa = int(input("Какой ваш рост в см? "))
if trassa >= 170:
    print("черная")
elif trassa >= 155 and trassa < 170:
    print("красная")
elif trassa >= 140 and trassa < 155:
    print("зеленая")
elif trassa >= 80 and trassa < 140:
    print("синяя")
else:
    print("Рост не соответствует допустимому значению")