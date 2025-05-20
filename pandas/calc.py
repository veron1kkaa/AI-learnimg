def calculator(a,b, operation='add', *args,**kwargs):
    operations ={
        "add": lambda x,y:x+y,
        'subtract': lambda x,y: x-y,
        'multiply': lambda x,y: x*y,
        'divide': lambda x,y:x/y if y !=0 else float('inf')
    }

    if operation not in operations:
        raise(f'Невідома операція: {operation}')

    result = operations[operation](a,b)

    for num in args:
        result = operations[operation](result, num)

    if kwargs.get('round_result'):
        result = round(result)

    if kwargs.get('log_result'):
        print(f"Результат {result}")

    return result



print(calculator(6,8))
print(calculator(6,8, 'subtract'))
print(calculator(6,8, 'multiply', round_result=True))
print(calculator(6,8, 'divide',  log_result=True))
