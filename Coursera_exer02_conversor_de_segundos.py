segundost = int(input("Por favor, entre com o número de segundos que deseja converter: "))

dia = segundost // 86400
segundosdia = segundost % 86400
hora = segundosdia // 3600
segundoshora = segundosdia % 3600
minutos = segundoshora // 60
segundosmin = segundoshora % 60
segundos = segundosmin

print(dia,"dias,",hora,"horas",minutos,"minutos e",segundos,"segundos.")