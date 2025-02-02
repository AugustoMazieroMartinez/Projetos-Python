def divide(n, d):
    try:
        return n/d
    except ZeroDivisionError:
        return 0
    
print(divide(8, 0))