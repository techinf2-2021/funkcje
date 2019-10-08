# coding: utf-8
"""
# Filmy

Napisz funkcję `message`, która jako parametr przyjmie słownik o następujących kluczach:

* **name**,
* **role**,
* **movie**.

Następnie niech funkcja przygotuje sformatowany napis: „In _movie_, _name_ is a _role_.”, gdzie w odpowiednie miejsca
podstawi wartości z ww. kluczy. Jeśli któregoś z kluczy nie będzie w słowniku, funkcja ma zwrócić wartość `None`.

##### Przykład 1:

```python
han = {
    "name": "Han Solo",
    "role": "smuggler",
    "movie": "Star Wars"
}

print(message(han))
```

Wynik:
```
In Star Wars, Han Solo is a smuggler.
```

##### Przykład 2:

```python
bilbo = {
    "name": "Bilbo Baggins",
    "role": "burglar"
}

print(message(bilbo))
```

Wynik:
```
None
```
"""

