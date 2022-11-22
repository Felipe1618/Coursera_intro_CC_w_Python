segundos_str = input("Informe o número de segundos: ")
total_segs = int(segundos_str)

horas = total_segs // 3600  # horas recebe a parte inteira da divisão
segs_restantes = total_segs % 3600 # segs_restantes recebe resto  da divisão
minutos = segs_restantes // 60
segs_restantes_final = segs_restantes % 60

print(horas, "horas", minutos, "minutos e", segs_restantes_final, "segundos")
