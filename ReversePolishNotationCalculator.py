import math

error_log = []
def Addition(stack):
    b = stack.pop()
    a = stack.pop()
    stack.append(a + b)

def Subtraction(stack):
    b = stack.pop()
    a = stack.pop()
    stack.append(a - b)

def Multiplication(stack):
    b = stack.pop()
    a = stack.pop()
    stack.append(a * b)

def Division(stack):
    b = stack.pop()
    a = stack.pop()
    try:
        stack.append(a / b)
    except:
        error_log.append('Can not be devided by 0')
        pass

def Power(stack):
    b = stack.pop()
    a = stack.pop()
    stack.append(a ** b)

def SquareRoot(stack):
    b = stack.pop()
    stack.append(math.sqrt(b))

def Sin(stack):
    b = stack.pop()
    stack.append(math.sin(b))

def Cos(stack):
    b = stack.pop()
    stack.append(math.cos(b))

def Tan(stack):
    b = stack.pop()
    stack.append(math.tan(b))

def PushNumberInStack(stack, num):
    stack.append(num)
 
operators = {
    '+': Addition,
    '-': Subtraction,
    '*': Multiplication,
    '/': Division,
    '^': Power,
    'sqrt': SquareRoot,
    'sin': Sin,
    'cos': Cos,
    'tan': Tan,
}
 
def SplitInput(inp = None):
    'Inputs an expression and returns list of tokens'
 
    if inp is None:
        inp = input('expression: ')
    tokens = inp.strip().split()
    return tokens
 
def RPNCalculator(tokens):
    stack = []
    operation_table = ['TOKEN ACTION STACK'.split()]
    for token in tokens:
        if token in operators:
            action = 'Apply operator on remaining number(s)'
            operators[token](stack)
            operation_table.append( (token, action, ' '.join(str(s) for s in stack)) )
        else:
            action = 'Push number in stack'
            PushNumberInStack(stack, float(token))
            operation_table.append( (token, action, ' '.join(str(s) for s in stack)) )
    return operation_table
 
def main():
    for _ in iter(int, 1):
        equation = input('Enter a valid reverse polish notation equation: ')
        print( 'For this reverse polish notation expression: %r\n' % equation )
        answer_table = RPNCalculator(SplitInput(equation))
        max_col_width = [max(len(y) for y in x) for x in zip(*answer_table)]
        row = answer_table[0]
        print( ' '.join('{cell:^{width}}'.format(width=width, cell=cell) for (width, cell) in zip(max_col_width, row)))
        for row in answer_table[1:]:
            print( ' '.join('{cell:<{width}}'.format(width=width, cell=cell) for (width, cell) in zip(max_col_width, row)))

        if error_log:
            print('\n\n*** Error occurred during calculation ***\n')
            for error in error_log:
                print(error)
            print('\n')
        else:
            ans = float(answer_table[-1][2])
            print('\n\nFinal answer after compliting all operations is: %r\n' % ans)
        
        is_another_equ = input('\nDo you waht to enter another equation?(y/n) ')[0].upper()
        if is_another_equ != 'Y':
            break


if __name__ == '__main__':
    main()
