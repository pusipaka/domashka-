#
# #Задание 1 там было слишком много поэтому я не стал комментировать все задание
klich=input("введите кличку питомца:")
vid_pitom=input("введите вид питомца")
vozrast_pitom=int(input('введите его возраст'))
imya_vald=input("введите имя владельца:")
if vozrast_pitom%10==1 and vozrast_pitom%100!=11:
    b="год"
elif vozrast_pitom%10 in [2,3,4] and not(vozrast_pitom%100 in [12,13,14]):
    b="года"
else:b="лет"
pets = {
    f"кличка питомца {klich}":{
    'Вид питомца':vid_pitom,
    'Возраст питомца':f"{vozrast_pitom} {b}",
    'Имя владельца':imya_vald
  }
}
print(pets)
#Задание 2
f=dict()
for i in range(10,-6,-1):
    f={i:i**i}
    print(f)