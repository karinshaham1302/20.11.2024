# 1
from operator import index

# a
tup1: tuple[int] = (99,)
print(tup1)

# b
tup2: tuple[int, int, int] = (77, 88, 99)
print(tup2)

# c
num: tuple[int, int, int, int, int] = (13, 22, 1, 41, 36)
print(len(num))

# d
tuple_1: tuple[int, int] = (1, 2)
tuple_2: tuple[int, int] = (3, 4)
print(tuple_1 + tuple_2)

# e
tup_1: tuple[int, int, int, int] = (1, 2, 3, 4)
tup_2: tuple[int, int, int, int] = (3, 4, 5, 6)
print(tuple(x for x in tup_1 if x in tup_2))

# f
tup_3: tuple[int, int, int, int] = (1, 2, 3, 4)
tup_4: tuple[int, int, int, int] = (3, 4, 5, 6)
print(tuple(x for x in tup_3 + tup_4 if (x in tup_3) != (x in tup_4)))

# g
tup3: tuple[int, int, int, int, int, int] = (3, 10, 4, 7, 1, 9)
def num_index(tup3, index):
     if 0 <= index <= len(tup3):
         return tup3[index]
     else:
         return None
print(num_index(tup3, index))

# h
tup4: tuple[int, int, int, int] = (100, 8, 54, 92)
print(tup4[::-1])

# i
tup5: tuple[int, int] = (1, 2)
print(tup5 * 3)

# j
tup6: tuple[int, int, int, int, int, int, int] = (10, 8, 5, 3, 2, 50, 10)
num: int = 10
print(tuple(x for x in tup6 if x != num))

# k
tup7: tuple[int, int, int, int, int, int, int, int] = (10, 8, 5, 5, 2, 50, 10, 30)
result = []
for x in tup7:
    if x not in result:
        result.append(x)
print(tuple(result))

# l
tup8: tuple[int, int, int, int, int, int, int, int] = (10, 8, 5, 5, 3, 2, 5, 10)
number: int = 5
ind_tup = tuple(i for i in range(len(tup8)) if tup8[i] == number)
print(ind_tup)

# m
names = []
scores = []
SENTINAL = -999

while True:
    name: str = input('Enter a name:')
    if name.lower() == 'done':
        break
    names.append(name)
    score: int = int(input('Enter a number:'))
    if score == SENTINAL:
        break
    scores.append(score)

combines_tuple: tuple[tuple[any], tuple[any]] = tuple(zip(names, scores))
print(combines_tuple)


# 2
# Tuple -
# הכוח שלו זה לא רק שאי אפשר לשנות אותו. הכוח שלו זה שמאחורי הקלעים הוא משתמש בלוגיקה
# ואלגוריתמים שגורמים לו לעבוד מאוד מהר ולהקצות זיכרון בדיוק למה שהוא צריך

# List -
# מתאים למקרים שבהם יש צורך בשינויים במהלך העבודה

# כברירת מחדל תמיד עדיף להשתמש ב- Tuple ואם נגיע למצב שנרצה לשנות את הרשימה,
# נהפוך אותה ל- List


# 3
data_tuple = ({'name': 'Alice', 'age': 30, 'city': 'New York'}, 1000, 'secret-code')
data_tuple[0]['age'] = 31
print(data_tuple)
data_tuple[0].clear()
print(data_tuple)

# הקוד לא גורם לשגיאה מכיוון שאייטם 0 מצביע על מבנה נתונים מורכב ולכן
# אפשר לשנות את מבנה הנתונים המורכב הזה ואז השינוי ישתקף גם ב- Tuple
# כי הוא תמיד יצביע על הכתובת של אותו מבנה נתונים
