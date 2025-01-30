def line_one(a:int, b:int) -> int:
    return a+b

def line_two(a:int, b:int) -> int:
    return a-b

def line_three(a:int, b:int) -> int:
    return a*b

def pipeline(a:int, b:int):
    
    if not (1 <= a <= 10**10 and 1 <= b <= 10**10):
        raise ValueError('Number out of range (1 - 10**10)')
    print(line_one(a,b))
    print(line_two(a,b))
    print(line_three(a,b))

if __name__ == '__main__':
    try :        
        a = int(input())
        b = int(input())
        
        pipeline(a,b)
    except ValueError as e:
        print(f'Error Input {e}')
