segs_str = input("Digite o total de segundos para a conversão: ")
total_segs = int(segs_str)

horas = total_segs // 3600
segs_restantes = total_segs % 3600
minutos = segs_restantes // 60
segs_restantes_final = segs_restantes % 60

print(horas, "horas, ", minutos, "minutos e", segs_restantes_final, "segundos")
