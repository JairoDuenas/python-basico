print('Programa de evaluación de notas de alumno')

nota_alumno = int(input("Ingrese la nota: "))

def evaluacion(nota):
  valoracion = 'Aprobado'

  if nota < 5:
    valoracion = 'No aprobado'
  return valoracion

print(evaluacion(nota_alumno))
