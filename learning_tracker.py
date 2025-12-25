INFO = ("Version_0.1","Date:25.12.2025","Autor: Grzegorz")
print(INFO)
Lesson_Topic = {"Wyrazenia warunkowe" : "Zalicone",
                "If.elif.else" :  "Poprawka  ",
                "Funkcjie" : "Zalicone",
                "Konersje Typow" : "Poprawka ",
                 "Petla For. White" : "Poprawka",
                 "Listy" : "Zalicone",
                 "Slownik" : "Zalicony ",
                 "Obliczenia Arytmetyczne" : "Zalicone",
                 "Wyrazenia Logiki Bool'a " : "Zalicone"}
print(Lesson_Topic)

Zalicone = []
Poprawka = []     

for temat,status in Lesson_Topic.items():
    if status == "Zalicone": Zalicone.append(temat)
    elif status == "Poprawka" : Poprawka.append(temat)
    
print("Zalicone :" , Zalicone) 
print("Poprawka : " , Poprawka)   

liczba_wszystkich = len(Lesson_Topic)
liczba_zaliconych = len (Zalicone)

procent = (liczba_zaliconych / liczba_wszystkich) * 100
print("Liczba _tematow" , liczba_wszystkich)
print("Zaliczone" , liczba_zaliconych)
print(f"proczent zaliczenia : {procent :.2f} %")
if procent < 30 :
    print("X Kurs nie zalicony" )
else:
    print(" v Kurs Zaliczony")
