def division(a,b):
    try:
        print(a/b)
    except ZeroDivisionError as zerodv:
        print('You can not divide by zero!!')
        print('Error:',zerodv)
    except (TypeError,NameError):
        print('Please check your input!')
    finally:
        print('Finally block executed!')


division(48,4)
division(56,5)
division(157,3)
division(488,10)
division(63,0)