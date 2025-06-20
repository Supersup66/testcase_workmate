a = '5'
b = '5.6'


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
    
print(is_number(a))
print(is_number(b))