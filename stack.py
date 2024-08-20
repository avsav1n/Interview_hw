class Stack:
    '''Класс структуры данных - стек

    '''
    def __init__(self, sequence=None):
        self.stack = list(sequence) if sequence else []

    def is_empty(self):
        '''Метод проверки стека на наличие элементов.
        '''
        return self.size() == 0
    
    def size(self):
        '''Метод возврата количества элементов в стеке.
        '''
        return len(self.stack)
    
    def push(self, value):
        '''Метод добавления нового элемента в стек.
        '''
        self.stack.append(value)

    def pop(self):
        '''Метод удаления верхнего элемента стека и его возврата.
        '''
        return None if self.is_empty() else self.stack.pop()
    
    def peek(self):
        '''Метод возврата верхнего элемента стека без удаления.
        '''
        return None if self.is_empty() else self.stack[-1]

    def __repr__(self) -> str:
        return f'Stack: {', '.join(self.stack)}'