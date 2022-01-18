from stack import Stack


def infix_to_postfix(infix_expr):
    prec = {'*': 3, '/': 3, '+': 2, '-': 2, '(': 1}

    op_stack = Stack()  # Stos operatorow
    postfix = []  # Wyjscie

    for token in infix_expr.split():
        if token.isalnum():
            postfix.append(token)
        elif token == "(":
            op_stack.push(token)
        elif token == ")":
            while op_stack.peek() != '(':
                postfix.append(op_stack.pop())

            op_stack.pop()  # Zrzucenie '(' ze stosu
        else:
            while not op_stack.is_empty() and prec[op_stack.peek()] >= prec[token]:
                postfix.append(op_stack.pop())
            op_stack.push(token)

    while not op_stack.is_empty():
        postfix.append(op_stack.pop())

    return " ".join(postfix)


if __name__ == '__main__':
    print(infix_to_postfix("A + A + A + A + A + A + A + A "))
    print(infix_to_postfix("AA * AB * ( ACD + AOV )"))
    print(infix_to_postfix("( 5 - 6 ) * 4 - ( 5 - 2 * 2 )"))
    print(infix_to_postfix("( 7 + 8 ) / ( 3 + 2 )"))
