# `034` Dates

On numpy you can get dates. For example, if you want to get today's date, you would do it this way:

```python
today = np.datetime64('today')
```

What if you want to get tomorrow's date? You can do it this way:

```python
tomorrow = np.datetime64('today') + np.timedelta64(1)
```

## 📝 Instructions:

1. Get yesterday's date and print it in the console.

## 💡 Hint:

+ You have to use the `datetime64` function. You can read more about this function on the following link: https://numpy.org/doc/stable/reference/arrays.datetime.html