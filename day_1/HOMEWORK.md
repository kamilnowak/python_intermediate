# SDA Python Intermediate

## Zadanie domowe:
### 1. Dodać type hintsy do wszystkch istniejących funkcji
### 2. Przygotuj klase "Student", która:
 - będzie przyjmować przy inicjalizacji dane takie jak imie, nazwisko, wiek
 - będzie zawierać metody:
    - add_grades(funkcja powinna obsługiwać dowolną liczbę ocen i zapisywać je do studenta, możliwy zakres ocen to 1-6)
    - remove_grade (jako param przyjmij numer indexu w liście grades)
 - pamiętaj aby:
    - dodać testy
    - dodać type hintsy
    - obsłużyc wyjątki (np próba usunięcia elementu o indexie spoza listy, albo dodanie oceny spoza zakresu)

 - **podpowiedzi**:
    - jeśli w funkcji chcesz odwołać się do atrybutu klasy można to zrobić za pomocą `self.nazwa_atrybutu`
    - zakres ocen sprawdzamy już w momencie dodawania oceny do studenta
    - ocena/oceny które chece dodać powinny byc przekazywana jako argument funkcji
    - do operacji na liście (np. dodawnie, usuwanie ocen) warto wykorzystać metody `append`, `extend`, `pop`

### 3. Przygotuj klase "School", która:
 - będzie przyjmować przy inicjalizacji dane takie jak nazwa uczelni, adres
 - będzie zawierac metody:
    - add_student (przyjmie pojedynczy obiekt studenta)
    - add_students (przyjmie wiele obiektów typu student)
    - remove_student
 - pamiętaj aby:
    - dodać testy
    - dodać type hintsy
    - obsłużyc wyjątki (np próba dodania jako student obiektu innego typu powinna skutkowac rzuceniem wyjątku)
