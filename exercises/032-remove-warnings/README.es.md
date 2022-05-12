# `032` Remove Warnings

Al usar Numpy, puedes quitar los "warnings" del código. si quieres quitarlos, debes usar la siguiente función `np.seterr`:

```python
defaults = np.seterr(all="ignore")
```

Si quieres volver a poner los "warnings", debes usar el siguiente código:

```python
_ = np.seterr(**defaults)
```

## Importante

+ Tienes que usar la función `seterr`. Puedes leer más de esta función en el siguiente link: https://numpy.org/doc/stable/reference/generated/numpy.seterr.html