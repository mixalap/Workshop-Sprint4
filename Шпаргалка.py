1.	Прототипирование.
>>> filter(range(10), lambda x: x == 5)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: 'function' object is not iterable
>>> filter(lambda x: x == 5, range(10))
<filter object at 0x033854F0>
>>> tuple(filter(lambda x: x == 5, range(10)))
(5,)

for num in range(1, 101):
	val = ''
	if num % 3 == 0:
		val += 'Fizz'
	if num % 5 == 0:
		val += 'Buzz'
	if not val:
	val = str(num)
	print(val)
    

# -  REPL (от Read, Eval, Print, Loop – прочитать, вычислить, напечатать, повторить)

for num in range(1, 101):
    print(num)
    
    
for num in range(1, 101):
    if num % 3 == 0:
        print('Fizz')
    else:
        print(num)
    
Упомянуть проблему с отступами
Но код при этом хранится в буфере терминала (И представьтк себе что случится если вдруг закрыть терминал)

Рассказать про ipython
    
# С помощью скрипта
Плюсы того, что весь код в файле

# Использовать pdb

# Jupiter

jupyter nbconvert ––to script Untitled.ipynb


2.	Лайф кодинг по области видимости и замыканиям

# Область видимиости переменной

# 1. Пример

# b = 2

# def func(a):
#     print(a)
#     b = 7
#     print(b)
#     # b = 7

# b = 2
# func(1)
# print(b)

# Замыкние
# 2. Пример

def main_func():
    def inner_func():
        print("Hello my friend")
    inner_func()

# main_func()
a = main_func()
print(a)



from posts.models import Post, User, Group
posts = Post.objects.order_by('-pub_date')

posts_with_group = [p for p in posts if p.group]

posts_with_group[0].group


groups = Group.objects.all()
this_group = groups[0]
this_group.posts.all()

this_group.post_set.all()









