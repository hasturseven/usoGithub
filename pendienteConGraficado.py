from bokeh.plotting import figure, output_file, show

from CreandoExcepcion import ExceptionEjemplo

print('agragando un par de cambios para')


# def run():
#     output_file('pendienteConGraficos.html')
#     fig = figure()
#     while True:
#         try:
#             print('***   1) para graficar una recta   ***')
#             print('***   2) para salir del programa   ***')

#             opcion=input('ingrasa una opcion')

#             if(opcion=='1'):
#                 punto_final_x = int(input('ingrese hasta que valor x desea graficar'))
#                 punto_inicial_x = int(input('ingrese desde que valor x quiere que inice'))
#                 if punto_final_x<punto_inicial_x:
#                     raise ExceptionEjemplo("debes ingresar un valor final de x mayor que el inicial ")
#                 total = 0
#                 valor_y = float(input('valor cuando x es cero'))
#                 y_valores = []
#                 x_valores = []
#                 pendiente = float(input('ingrese la pendiene'))
                
#                 if(punto_inicial_x < 0):
#                     total = (-1*punto_inicial_x)+punto_final_x
#                     for x in range(total+1):
#                         x_valores.append(punto_inicial_x+x)

#                 else:
#                     total = punto_final_x
#                     for x in range(total+1):
#                         x_valores.append(x+punto_inicial_x)

#                 for y in range(total+1):
#                     y_valores.append(((pendiente*x_valores[y])+valor_y))

#                 fig.line(x_valores, y_valores, line_width=2)

#                 show(fig)
#             elif opcion=='2':
#                 break
#             else:
#                 print('ingrese una opcion valida')
#         except ExceptionEjemplo as e:
#             print(e)
#         except ValueError:
#             print('dees ingresar un numero')


# if __name__ == '__main__':
#     run()
