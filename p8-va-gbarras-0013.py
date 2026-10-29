import numpy as np
import matplotlib.pyplot as plt
# Meredith Aguirre NC = 0013 Fecha 29/10/2026

diasX = ["Lun", "Mar", "Mie", "Jue", "Vie"]
califa_va_y = [5, 6, 3, 8, 10]

plt.bar(diasX, califa_va_y)
plt.title("Califas en VA de Meredith Aguirre NC = 0013")
plt.xlabel("Días de la semana habil")
plt.ylabel("Calificaciones en VA")
plt.grid()
plt.show()