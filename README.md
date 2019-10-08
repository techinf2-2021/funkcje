# Oprocentowanie

Niech _p_ będzie rocznym oprocentowaniem konta bankowego. Po _n_ początkowa suma _A_ wzrośnie do:

<p align="center"><i>A</i> (1 + <i>p</i> / 100)<sup><i>n</i></sup></p>

Napisz funkcję `interest` (przyjmującą argumenty _A_, _n_ i _p_), która zwraca kwotę na koncie po kilku latach,
a następnie użyj jej do wyliczenia ile pieniędzy będzie na koncie po trzech latach, jeśli początkowy kapitał wynosił
1000 zł, a oprocentowanie 5%.


# Temperatura

Wzór przeliczający temperaturę w stopniach Fahrenheita na stopnie Celsiusza jest następujący:

<p align="center"><i>C</i> = <sup>5</sup>⁄<sub>9</sub> (<i>F</i> − 32)</p>

Napisz funkcję ``C(F)``, która wylicza temperaturę według tego wzoru. Następnie napisz program, który drukuję tabelę
ze stopniami Fahrenheita: 0, 10, 20, . . . , 100 w pierwszej kolumnie oraz odpowiadającą im temperaturę w stopniach
Celsiusza w drugiej kolumnie.


# Dolary

Napisz funkcję `convert_to_usd`, która przyjmuje parametr `pln`, czyli kwotę w złotówkach. Funkcja ma zwrócić podaną
kwotę w dolarach amerykańskich. Jako przelicznik przyjmij wartość 3,85 PLN = 1 USD.


# Netto

Napisz funkcję `calc_net`, która przyjmie argumenty:

* `brutto`, czyli kwotę brutto ceny zakupu,
* `vat`, czyli wartość podatku VAT w procentach. Możesz założyć, że VAT ma być liczbą zmiennoprzecinkową z zakresu
  0 – 100. Domyślną wartością VAT powinno być 23%.

Funkcja ma zwrócić wartość netto ceny. Jakie obliczenia musisz wykonać?


# Krótkie słowa

Napisz funkcję `get_short_words`, która przyjmie listę wyrazów. Funkcja powinna zwrócić listę słów krótszych od _n_
znaków, gdzie _n_ jest maksymalną ilością liter w wyrazie. Domyślnie _n_ powinno mieć wartość 5.

##### Przykład
```python
wyrazy = "Litwo ojczyzno moja ty jesteś jak zdrowie".split(' ')

print(get_short_words(wyrazy))
print(get_short_words(wyrazy, 3))
```

Wynik:
```
['moja', 'ty', 'jak']
['ty']
```

##### Zadanie dodatkowe
Sprawdź w dokumentacji działanie metody `split` działającej na łańcuch tekstowych i użytej w przykładzie.


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


# Kostki

Napisz funkcję `dice(num)`, która zasymuluje rzuty kostką sześcienną. `num` to parametr, który oznacza ilość kostek.
Funkcja ma zwrócić sumę wyrzuconych oczek.

Następnie napisz funkcję `print_histogram(throws)`, która wykona _N_ rzutów dwiema kostkami i wyrysuje na ekranie
histogram ilości oczek w wyniku (suma może zawierać się w przedziale 2 - 12) dokładnie według wzoru:

```
 2: ##############
 3: #########################
 4: ##############################################
 5: #####################################################################
 6: ##################################################################
 7: ###########################################################################################
 8: ####################################################################
 9: ###################################################
10: ###################################
11: ##################
12: #################
```
