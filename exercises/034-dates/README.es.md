# `034` Dates

Con Numpy puedes obtener fechas. Por ejemplo, Si quieres obtener la fecha de hoy, puedes hacerlo de esta manera:

```python
today = np.datetime64('today')
```

¿Y cómo harías si quieres obtener la fecha de mañana? Esto lo haces de la siguiente manera:

```python
tomorrow = np.datetime64('today') + np.timedelta64(1)
```

## 📝 Instrucciones:

1. Obtén la fecha de ayer e imprímela en la consola.

## 💡 Pista:

+ Tienes que usar la función `datetime64`. Puedes leer más de esta función en el siguiente link: https://numpy.org/doc/stable/reference/arrays.datetime.html