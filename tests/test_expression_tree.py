import unittest

from pycalculator.expression_tree import *

class TestClassOperator(unittest.TestCase):
    """Unit test for the Operator class."""

    def test_apply(self):
        # basic binary operators
        self.assertEqual(Operator('*', operator.mul).apply(2, 3), 6)
        self.assertEqual(Operator('-', operator.sub).apply(2, 3), -1)

        # basic unary operator
        self.assertEqual(Operator('-', lambda x: -x).apply(2), -2)
        self.assertEqual(Operator('!', math.factorial).apply(5), 120)

        # basic function operator
        self.assertEqual(Operator('max', max).apply(2, 3, 18, -2), 18)
        self.assertEqual(Operator('tri_sum', lambda x, y, z: x + y + z).apply(1, 2, 3), 6)

        # user-defined function operator
        def my_operator(a, b, c=2, string='waffle'):
            return (a + b + c) / len(string)
        self.assertEqual(Operator('my_op', my_operator).apply(1, 2, c=3, string='hello'), 1.2)


class TestClassExpressionTreeNode(unittest.TestCase):
    """Unit test for the ExpressionTreeNode class."""

    def setUp(self):
        self.operators = {'+': Operator('+', operator.add, 'binary'),
                          '-': Operator('-', operator.sub, 'binary'),
                          '!': Operator('!', math.factorial, 'unary'),
                          'max': Operator('max', max, 'function'),
                          'len': Operator('len', len, category='function')}

        # create expression tree corresponding to '2 + 1 - 4'
        self.basic_tree = ExpressionTreeNode(self.operators['+'],
                                             children=[ExpressionTreeNode(2),
                                                       ExpressionTreeNode(self.operators['-'],
                                                                          children=[ExpressionTreeNode(1),
                                                                                    ExpressionTreeNode(4)])])
        # create expression tree corresponding to '2 + max(1, 4, 7)'
        self.with_max_tree = ExpressionTreeNode(self.operators['+'],
                                                children=[ExpressionTreeNode(2),
                                                          ExpressionTreeNode(self.operators['max'],
                                                                             children=[ExpressionTreeNode(1),
                                                                                       ExpressionTreeNode(4),
                                                                                       ExpressionTreeNode(7)])])
        # create expression tree corresponding to "! len('abc' + 'de')"
        self.complex_tree = ExpressionTreeNode(self.operators['!'],
                                children=[ExpressionTreeNode(self.operators['len'],
                                              children=[ExpressionTreeNode(self.operators['+'],
                                                            children=[ExpressionTreeNode('abc'),
                                                                      ExpressionTreeNode('de')])])])

    def test_is_leaf(self):
        self.assertEqual(self.basic_tree.is_leaf(), False)
        self.assertEqual(self.basic_tree.children[0].is_leaf(), True)

    def test_str(self):
        self.assertEqual(str(self.basic_tree)   , '+\n'
                                                  '└── 2\n'
                                                  '└── -\n'
                                                  '    └── 1\n'
                                                  '    └── 4')
        self.assertEqual(str(self.with_max_tree), '+\n'
                                                  '└── 2\n'
                                                  '└── max\n'
                                                  '    └── 1\n'
                                                  '    └── 4\n'
                                                  '    └── 7')
        self.assertEqual(str(self.complex_tree) , '!\n'
                                                  '└── len\n'
                                                  '    └── +\n'
                                                  "        └── 'abc'\n"
                                                  "        └── 'de'")

    def test_get_infix(self):
        self.assertEqual(self.basic_tree.get_infix()   , '(2 + (1 - 4))')
        self.assertEqual(self.with_max_tree.get_infix(), '(2 + max(1, 4, 7))')
        self.assertEqual(self.complex_tree.get_infix() , "!len(('abc' + 'de'))")

    def test_evaluate(self):
        self.assertEqual(self.basic_tree.evaluate()   , -1)
        self.assertEqual(self.with_max_tree.evaluate(), 9)
        self.assertEqual(self.complex_tree.evaluate() , 120)


class TestClassExpressionTreeBuilder(unittest.TestCase):
    """Unit test for the ExpressionTreeBuilder class."""

    def setUp(self):
        self.operators = {'*': Operator('*', operator.mul    , 'binary', 'right', 2),
                          '/': Operator('/', operator.truediv, 'binary', 'left' , 2), 
                          '+': Operator('+', operator.add    , 'binary', 'right', 3),
                          '-': Operator('-', operator.sub    , 'binary', 'left' , 3)}

        self.simple_expr    = ExpressionTreeBuilder('1+2')
        self.complex_expr   = ExpressionTreeBuilder('1-2*5+4/2')
        self.complex_expr_2 = ExpressionTreeBuilder('1+2^(10-2*3)')

    def test_parse_expression(self):
        self.simple_expr._parse_expression()
        self.assertListEqual(self.simple_expr.chuncks, ['1', '+', '2'])

        self.complex_expr._parse_expression()
        self.assertListEqual(self.complex_expr.chuncks, ['1', '-', '2', '*', '5', '+', '4', '/', '2'])

        self.complex_expr_2._parse_expression()
        self.assertListEqual(self.complex_expr_2.chuncks, ['1', '+', '2', '^', '(', '10', '-', '2', '*', '3', ')'])

    def test_build(self):
        self.simple_expr.build()
        self.assertEqual(repr(self.simple_expr.tree), '+\n'
                                                      '└── 1\n'
                                                      '└── 2')

        self.complex_expr.build()
        self.assertEqual(repr(self.complex_expr.tree), '+\n'
                                                       '└── -\n'
                                                       '    └── 1\n'
                                                       '    └── *\n'
                                                       '        └── 2\n'
                                                       '        └── 5\n'
                                                       '└── /\n'
                                                       '    └── 4\n'
                                                       '    └── 2')

        self.complex_expr_2.build()
        self.assertEqual(repr(self.complex_expr_2.tree), '+\n'
                                                         '└── 1\n'
                                                         '└── ^\n'
                                                         '    └── 2\n'
                                                         '    └── -\n'
                                                         '        └── 10\n'
                                                         '        └── *\n'
                                                         '            └── 2\n'
                                                         '            └── 3')

    def test_evaluate(self):
        infix_dict = { 
                         # basic operations
                         '1+2': 3,
                         '1-2': -1,
                         '1+2-5': -2,
                         '1-2+5': 4,
                         '1-2-5': -6,
                         '2*3': 6,
                         '3/4': 0.75,
                         '2*3/3': 2,
                         '2/3*3': 2,
                         '2-3*5': -13,
                         '2*3-5': 1,
                         '2+3-5*2': -5,
                         '2': 2,

                         # parenthesis
                         '(2)': 2,
                         '((2))': 2,
                         '(2+3)': 5,
                         '(2+3)-4': 1,
                         '(2-3)+4': 3,
                         '2-(3-4)': 3,
                         '2*(3-4)': -2,
                         '(2*(3-4))/2+8': 7,
                         '(2*(3-4))/(2+8)': -0.2,
                     }

        for key, value in infix_dict.items():
            self.assertEqual(ExpressionTreeBuilder(key).evaluate(), value)


# Shell command to run the test:
# $ python -m unittest -v tests.test_expression_tree
if __name__ == '__main__':
    unittest.main()
