import csv

list_voprosov = []
list_otvetov1 = []
list_otvetov2 = []
list_otvetov3 = []
score = []
nom_vop = 1
verno = 0
otsenka =''

with open ('quiz.csv', newline='') as quiz:
  read = csv.reader(quiz, delimiter=';')
  for row in read :
    vopros = row[0]
    otvet1 = row[1]
    otvet2 = row[2]
    otvet3 = row[3]
    prav_otv = row[4]
    
    list_voprosov.append(vopros)
    list_otvetov1.append(otvet1)
    list_otvetov2.append(otvet2)
    list_otvetov3.append(otvet3)

while nom_vop < 20:
  print('Вопрос №' + str(nom_vop) + ':' + list_voprosov[nom_vop])
  print('a) ' + list_otvetov1[nom_vop])
  print('b) '+ list_otvetov2[nom_vop])
  print('c) '+ list_otvetov3[nom_vop])
  polzovatel = input("Выберите вариант ответа(a,b,c): ")
  
  if polzovatel == 'a': 
    a = list_otvetov1[nom_vop]
    if a == prav_otv[nom_vop]:
      print( "+5 баллов. Наверное это хорошо!")
      score.append(5)
      verno += 1
    else:
      print( "Ответ неверный! Странно но у вас почти получилось!.")

  elif polzovatel == 'b':
    b = list_otvetov2[nom_vop]
    if b == prav_otv[nom_vop]:
      print( "+5 баллов. Не так уж и много!")
      score.append(5)
      verno += 1
    else:
      print("Ответ неверный! Вероятность угодать была 33.3333%!!!.")

  elif polzovatel == 'c':
    c = list_otvetov3[nom_vop]
    if c == prav_otv[nom_vop]:
      print("+5 баллов. Ну это только пока!")
      score.append(5)
      verno += 1
    else:
      print("Ответ неверный! Ой это кто ошибся!.")

  else:
    print("Такого варианта ответа не существует!")
  nom_vop += 1

obwee = sum(score)

print("Тест окончен вот ваш результат " + str(obwee))
print("Количество правильных ответов: " + str(prav_otv)+ " из "+ str(len(list_voprosov) - 1))

if obwee == 100:
  print("Ваша оценка: A")
elif obwee >= 95:
  print("Ваша оценка: A-")
elif obwee >= 90:
  print("Ваша оценка: B+")
elif obwee >= 87:
  print("Ваша оценка: B")
elif obwee >= 85:
  print("Ваша оценка: B-")
elif obwee >= 80:
  print("Ваша оценка: C+")
elif obwee >= 77:
  print("Ваша оценка: C")
elif obwee >= 75:
  print("Ваша оценка: C-")
elif obwee >= 70:
  print("Ваша оценка: D+")
elif obwee >= 67:
  print("Ваша оценка: D")
elif obwee >= 65:
  print("Ваша оценка: D-")
else:
  print("Ваша оценка: F")


    

  