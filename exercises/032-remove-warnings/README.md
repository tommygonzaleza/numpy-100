# `032` Remove Warnings

When using numpy, you can remove the warnings when you run the code. If you want to remove them, you have to use the function `np.seterr`:

```python
defaults = np.seterr(all="ignore")
```

If you want to take the warnings back, you can do it this way:

```python
_ = np.seterr(**defaults)
```

## Important:

+ You have to use the `seterr` function. You can read more about this function on the following link: https://numpy.org/doc/stable/reference/generated/numpy.seterr.html