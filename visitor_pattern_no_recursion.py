import types

class Node:
    """Base class for all nodes in the expression tree."""
    pass

class Visitor:
    """A base class for visitors that can traverse a tree of nodes."""
    def visit(self, node):
        """handles iterative traversal using a stack"""
        stack = [ node]
        last_result = None
        while stack:
            try:
                last = stack[-1]
                if isinstance(last, types.GeneratorType):
                    stack.append(last.send(last_result))
                    last_result = None # This line is critical. Fixed the yield bug
                    # This line solves the generator value propagation issue by resetting the result after sending it to the coroutine.
                elif isinstance(last, Node):
                    stack.append(self._visit(stack.pop()))
                else:
                    last_result = stack.pop()
            except StopIteration:
                stack.pop()
        return last_result
                    
    def _visit(self, node):
        """dynamically dispatch to methods"""
        method_name = 'visit_' + type(node).__name__
        method = getattr(self, method_name, None)
        if method is None:
            method = self.generic_visit
        return method(node)
    
    def generic_visit(self, node):
        raise NotImplementedError(f"No visit_{type(node).__name__} method defined")
    
class UnaryOperator(Node):
    def __init__(self, operand):
        self.operand = operand 

class BinaryOperator(Node):
    def __init__(self, left, right):
        self.left = left
        self.right = right

class Number(Node):
    def __init__(self, value):
        self.value = value

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

# A sample visit that evaluates the expression
class EvaluateVisitor(Visitor):
    """A visitor that evaluates expressions."""
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
    
class EvaluateVisitorGenerator(Visitor):
    """A visitor that uses generators to evaluate expressions."""
    def visit_Number(self, node):
        yield node.value  # Or just `return` if not using generators
    
    def visit_Add(self, node):
        left = yield node.left
        right = yield node.right
        yield left + right  # Final result
        
    def visit_Subtract(self, node):
        left = yield node.left
        right = yield node.right
        yield left - right
    
    def visit_Multiply(self, node):
        left = yield node.left
        right = yield node.right
        yield left * right
    
    def visit_Divide(self, node):
        left = yield node.left
        right = yield node.right
        yield left / right
        
    def visit_Negate(self, node):
        operand = yield node.operand
        yield -operand

if __name__ == "__main__":
    # Example usage of the visitor pattern
    t1 = Subtract(Number(3), Number(4))
    t2 = Multiply(Number(2), t1)
    t3 = Divide(t2, Number(5))
    t4 = Add(Number(1), t3)

    evaluate_visitor = EvaluateVisitor()
    print("Evaluation:", evaluate_visitor.visit(t4))


    a = Number(0)
    for n in range(1, 100000):
        a = Add(a, Number(n))

    try:
        print("Sum of first 100000 numbers:", evaluate_visitor.visit(a))
    except RecursionError as e:
        print(e)
        print("RecursionError: The expression is too complex to evaluate with the current recursion limit.")
    print("Recursion limit:", __import__('sys').getrecursionlimit())


    evaluate_visitor_gen = EvaluateVisitorGenerator()
    print("Evaluation with generator:", evaluate_visitor_gen.visit(a))
