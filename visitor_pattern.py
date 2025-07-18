class Node:
    pass

class UnaryOperator(Node):
    def __init__(self, operand):
        self.operand = operand

class BinaryOperator(Node):
    def __init__(self, left, right):
        self.left = left
        self.right = right

class Add(BinaryOperator):
    pass

class Subtract(BinaryOperator):
    pass

class Multiply(BinaryOperator):
    pass

class Divide(BinaryOperator):
    pass

class Negate(UnaryOperator):
    pass

class Number(Node):
    def __init__(self, value):
        self.value = value


class Visitor:
    def visit(self, node):
        method_name = 'visit_' + node.__class__.__name__
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):
        raise Exception(f'No visit_{node.__class__.__name__} method')
    
class PrintVisitor(Visitor):
    def visit_Number(self, node):
        return str(node.value)

    def visit_Add(self, node):
        return f"({self.visit(node.left)} + {self.visit(node.right)})"

    def visit_Subtract(self, node):
        return f"({self.visit(node.left)} - {self.visit(node.right)})"

    def visit_Multiply(self, node):
        return f"({self.visit(node.left)} * {self.visit(node.right)})"

    def visit_Divide(self, node):
        return f"({self.visit(node.left)} / {self.visit(node.right)})"

    def visit_Negate(self, node):
        return f"-{self.visit(node.operand)}"
    
class EvaluateVisitor(Visitor):
    def visit_Number(self, node):
        return node.value

    def visit_Add(self, node):
        return self.visit(node.left) + self.visit(node.right)

    def visit_Subtract(self, node):
        return self.visit(node.left) - self.visit(node.right)

    def visit_Multiply(self, node):
        return self.visit(node.left) * self.visit(node.right)

    def visit_Divide(self, node):
        return self.visit(node.left) / self.visit(node.right)

    def visit_Negate(self, node):
        return -self.visit(node.operand)
    
# Visitor for generating stack code
class StackCode(Visitor):
    def generate_code(self, node):
        self.instructions = []
        self.visit(node)
        return self.instructions
    
    def visit_Number(self, node):
        self.instructions.append(('PUSH', node.value))

    def binop(self, node, instruction):
        self.visit(node.left)
        self.visit(node.right)
        self.instructions.append((instruction,))

    def visit_Add(self, node):
        self.binop(node, 'ADD')

    def visit_Subtract(self, node):
        self.binop(node, 'SUB') 

    def visit_Multiply(self, node):
        self.binop(node, 'MUL')

    def visit_Divide(self, node):
        self.binop(node, 'DIV')

    def visit_Negate(self, node):
        self.visit(node.operand)
        self.instructions.append('NEG')

    def unaryop(self, node, instruction):
        self.visit(node.operand)
        self.instructions.append((instruction,))

if __name__ == "__main__":

    # Example usage of the visitor pattern
    t1 = Subtract(Number(3), Number(4))
    t2 = Multiply(Number(2), t1)
    t3 = Divide(t2, Number(5))
    t4 = Add(Number(1), t3)

    print(type(t1).__name__)
    print(t1.__class__.__name__)

    # Example of visiting a binary operator
    print_visitor = PrintVisitor()
    evaluate_visitor = EvaluateVisitor()
    print("Expression:", print_visitor.visit(t4))
    print("Result:", evaluate_visitor.visit(t4))

    # Example of visiting a unary operator
    negate_node = Negate(Number(10))
    print("Negated value:", evaluate_visitor.visit(negate_node))
    print("Negated expression:", print_visitor.visit(negate_node))


    # Example of generating stack code
    stack_visitor = StackCode()
    instructions = stack_visitor.generate_code(t4)
    print("Stack code instructions:")
    print(instructions)
