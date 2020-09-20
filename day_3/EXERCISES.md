# SDA Python Intermediate

## Zadania w czasie zajęć:
### Zadanie 1. (na rzutniku)
Używając modułu abc utwórz klasę `Animal` która będzie zawierać abstrakcyjną metodę `sound`,
Dziedzicząc po klasie Animal utwórz klasy `Cat` i `Dog` i zaimplementuj dla nich metodę `sound`.

### Zadanie 2.
Utwórz klasę `Human` która będzie zawierać metodę `get_name` i zwróci string `Human`.
Utwórz klasę `Coder` która będzie zawierać metodę `get_name` i zwróci string `Coder`.
Utwórz klasę `PythonDev` która będzie dziedziczyć po obu tych klasach.
Wywołaj metodę `get_name` i sprawdź co zwraca. 


### Zadanie 3.
Używając modułu **abc oraz dataclass**:
 - Utwórz klasę `BaseEvent` która będzie posiadać takie atrybuty jak: `created_at`, `created_by`, `name`. 
 - Dodaj do klasy `BaseEvent` abstrakcyjną metodę `log_event`
 - Utwórz klasę `UserEvent` która będzie dziedziczyć po `BaseEvent` i zaimplementuje jego abstrakcyjne metody. 
 - Klasa `UserEvent` powinna dodatkowo zawierać atrybut `email`
 - Metoda `log_event` powinna zalogować (print) informacje z obiektu. 
 - Do klasy BaseEvent dodajmy dwie metody (send_notification, is_important_event)
 - Metoda is_important_event musi być abstrakcyjna
 - Metoda send_notification -> print "email sent" jeśli event jest important
 - W klasie UserEvent nadpisz is_important_event i jeśli nazwa eventu jest "USER_CREATED" albo "USER_DELETED" zwróc True


### Zadanie 4.
Używając modułu `re` utwórz funkcję `get_long_words` która przyjmie argument `text` i za pomocą wyrażenia regularnego
 zwróci wyrazy dłuższe niz 4 znaki. 


### Zadanie 5.
Używając modułu `re` utwórz funkcję `get_abbreviation` która przyjmie argument `text` i za pomocą wyrażenia regularnego
 zwróci skrót dla zadanej frazy. np wywołując z "Software Development Academy" funkcja powinna zwrócić "SDA".


### Zadanie 6.
Używając modułu `re` utwórz funkcję `replace_name` która przyjmie argument `replace_from`, `replace_to` i `text`  i za pomocą wyrażenia regularnego
 zamieni w `text` wartosc z `replace_from` na `replace_to`.
Przykładowo: "Ala ma kota. Ala ma psa." zamień imię na Ania

### zadanie 7
Napisz funkcje `is_valid_number`.
Niech zawiera wyrażenie regularne sprawdzające numer telefonu.
I zwraca True jeśli numer jest poprawny, jeśli nie jest poprawny zwróc False
przyklad:
    504123643     -> True
    5041          -> False
    000000000     -> False

dodatkowe:
 +48504123643     -> True
 (+48)504-123-643 -> True
