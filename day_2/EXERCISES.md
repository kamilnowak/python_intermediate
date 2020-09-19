# SDA Python Intermediate

## Zadania w czasie zajęć:
### Zadanie 1. (na rzutniku)
Używając namedtuple utwórz klasę Car która przyjmie jako parametry: `make`, `model` i `color`. Użyj nametuple tak aby nowa klasa MyCar korzystała z jej atrybutów i miała dodatkową funkcje `getHexColor`. 

### Zadanie 2.
Napisz funkcję mean(numbers), gdzie numbers to lista liczb dowolnego typu. Funkcja powinna zwrócić średnią arytmetyczną wszystkich elementów listy numbers.

### Zadanie 3.
Utwórz funkcję labeled_entries która:
 - przyjmie jako parametr `entries` listę słowników, np:
   ```
   my_data = [
       {
          "name": "Jan",   
          "Surname": "Kowalski",
       },    
       {
          "name": "Artur",   
          "Surname": "Nowak",
       },  
   ]
   ```
 - funkcja niech przeiteruje po liscie i dla kazdego elementu utworzy Namedtuple 
 - na wyniku funkcji powinna znalezc się lista Namedtuple 


### Zadanie 4.
Skopiuj do `exercises.py` i zmodyfikuj rozwiązanie zadania domowego (klasy Student i School) tak aby korzystać w nich z dekoratora dataclass. 

### Zadanie 5.
Korzystając z dataclass utwórz klasę `Country` która przyjmie jako parametr `name`, `population`, `area`, `coastline`.
Sortując liste krajów, powinno brać pod uwagę populacje. 