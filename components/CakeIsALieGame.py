import random
rand_num = random.randint(0, 1000)
game_status = True
def cakeisalie():
   print("привет это игра взломай пароль");
cakeisalie()
while game_status:
   a = int( input("взломай пароль: ") )
   if a == rand_num:
      print("хакер!")
      game_status = False
   elif a > rand_num:
      print("попробуй меньше!")  
   else:
      print("попробуй больше!")
