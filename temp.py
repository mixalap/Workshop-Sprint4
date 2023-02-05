def make_decorator(start_counter):
    def decorator(func):
        series = []
        count = start_counter

        def wrapper(*args, **kwargs):
            nonlocal count
            result = func(*args, **kwargs)
            series.append(result)
            print(f"Это {count} запуск функции {func.__name__}")
            print("series = {}".format(series))
            count += 1
            #return result
        return wrapper
    return decorator

@make_decorator(10)
def func1(a, b):
    c = a + b
    return c

# @make_decorator(10)
# def func2(a, b):
#     c = a + b
#     return c

# func2 = func1
# func1 = make_decorator(10)(func1)
# func2 = make_decorator(10)(func1)


func1(1, 1)
func1(2, b=1)
func1(a=2, b=2)

# print("Запускаем func2")

# func2(1, 1)
# func2(2, b=1)
# func2(a=2, b=2)

# print(func1)
# print(func2)
