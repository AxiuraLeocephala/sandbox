# def get_speak_func(text, volume):
#     '''
#     Функции могут захватывать локальное состояние. Такие функции называются
#     «лексическое замыкание» 
#     '''
#     def whisper():
#         return text.lower() + '...'
#     def yell():
#         return text.upper() + '!'
#     if volume > 0.5:
#         return yell
#     else:
#         return whisper

# print(get_speak_func("Hello, World", 0.7)())

# def make_added(n):
#     def add(x):
#         return x + n 
#     return add

# plus_3 = make_added(3)
# plus_5 = make_added(5)

# print(plus_3(4))
# print(plus_5(4))

class Adder:
    '''
    Объекты могут вести себя как функции 
    '''
    def __init__(self, n):
        self.n = n
    def __call__(self, x):
        return self.n + x
    
plus_3 = Adder(3)
plus_3(4)