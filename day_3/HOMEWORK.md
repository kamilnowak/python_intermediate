# SDA Python Intermediate

## Zadanie domowe:
### 1. Dodaj testy do klas/funkcji z exercises ;) 
### 2. Dodaj funkcję `is_valid_postal_code`
 która będzie sprawdzać poprawność kodu pocztowego (jedynie polskie kody). Dodaj testy i sprawdź działanie na kilku 
 róźnych kodach pocztowych.
### 3. Napisz klasę abstrakcyjną `BaseCourse` oraz dziedziczącą po niej `Course`.
- klasa `BaseCourse` ma zawierac atrybut `name`, `instructor`, `course_type`.
- klasa `Course` ma po niej dziedziczyć
### 4. Utwórz klasę abstrakcyjną `Person` oraz dziedziczące po niej `Student` i `Instructor` 
- klasa `Person` ma zawierać takie atrybuty jak `name`, `surname`
- klasa `Student` ma zawierać dodatkowo atrybut `courses_assigned` który przechowa wiele obiektów typu `Course`. 
- klasa `Instructor` ma zawierać dodatkowo atrybut `courses_type_which_can_lead` który przechowa wiele obiektów typu `str`.
- klasa `Instuctor` ma zawierać metodę `is_able_to_lead_course_type` 
która jako parametr przyjmie typ kursu i sprawdzi czy znajduje się on w kolekcji `courses_type_which_can_lead` **z wykorzystaniem wyrażenia regularnego**
- tworzenie kursu powinno sprawdzić czy dany instruktor może prowadzić kurs
 wywołując metodę `is_able_to_lead_course_type`, jeśli nie rzuć wyjątek. 
### 5. Rozszerz działanie klas powyżej:
- klasa `Student` powinna umożliwiać przypisanie/odpisanie kursu studentowi dodatkowo przez metode `assign_course`.
- klasa `Instructor` powinna umożlwiać dodanie/usuwanie typu kursu z kolekcji `courses_type_which_can_lead` 


przykładowe wywołanie (punkty 3 & 4):
```
python_instructor = Instructor(..., courses_type_which_can_lead=['python'])
python_course = Course(..., course_type='python', instuctor=python_instructor)
student = Student(..., courses_assigned=[python_course])
```