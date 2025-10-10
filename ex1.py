segundos = int(input("Digite os segundos: "))

horas = segundos // 360
minutos = (segundos % 3600) // 60 
segundosrestantes = segundos % 60

print(horas, "horas," , minutos, "minutos(s) e", segundosrestantes, "segundo(s)")
