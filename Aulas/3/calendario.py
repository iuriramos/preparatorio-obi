mes, dia = input().split() # você pode separar em duas linhas também...
mes, dia = int(mes), int(dia)

if mes in [1, 3, 5, 7, 8, 10, 12]:
    total_dias = 31
elif mes in [4, 6, 9, 11]:
    total_dias = 30
else: # mes == 2
    total_dias = 28
    
# adiciona espaços em branco no calendário (dia=1 >> 0 espaço, dia=2 >> 1 espaço em branco, ...)
total_dias = total_dias + (dia-1) 

# calcula quantidade de semanas
if total_dias % 7 == 0:
    semanas = total_dias // 7
else: # se possui resto, temos mais uma semana
    semanas = total_dias // 7 + 1

print(semanas)
