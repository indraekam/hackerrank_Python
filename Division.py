from typing import Tuple

def divison_cal(a:int, b:int) -> Tuple[int, float] :
    return (a // b, a / b)

def pipeline(a:int, b:int):
    
    if b == 0:
        raise ValueError('B cannot 0')
    
    int_div, float_div = divison_cal(a, b)
    
    print(int_div)
    print(float_div)

if __name__ == '__main__':
    try :
        a = int(input())
        b = int(input())
        
        pipeline(a, b)
    except ValueError as e:
        print(f'Input error {e}')
