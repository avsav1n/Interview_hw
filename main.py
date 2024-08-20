from stack import Stack

def check_braces_sequence(sequence):
    braces_closed = {
        '}': '{',
        ']': '[',
        ')': '('
    }
    stack = Stack()
    for element in sequence:
        if element not in '()[]{}':
            continue
        if element in '([{':
            stack.push(element)
        else:
            if braces_closed[element] != stack.pop():
                return 'Несбалансированно'
    return 'Сбалансированно' if stack.is_empty() else 'Несбалансированно'
