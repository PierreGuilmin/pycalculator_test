"""This module implements various classes allowing to build an expression tree from an infix
expression.

.. testsetup::

    from pycalculator.expression_tree import *
"""

import operator
import math
import re

from tools import *

class Operator():
    """This class defines an operator and its characteristics (category, associativity, precedence).

    Attributes
    ----------
    symbol: `str`
        String representing the operator (ex: ``'+'``, ``'-'``, ``'max'``, ...).
    function: `function`
        Defines the action of the operator on its arguments.
    category: `{'unary', 'binary', function', None}`
        Defines the operator category.
    associativity: `{'left', 'right', None}`
        Defines the operator associativity.
    precedence: `int` or `None`
        Defines the operator precedence (low value for low precedence and high value for high precedence).

    See Also
    --------
    `Wikipedia 'Operator associativity' article
    <https://en.wikipedia.org/wiki/Operator_associativity>`_

    `Wikipedia 'Order of operations' article <https://en.wikipedia.org/wiki/Order_of_operations>`_
    """

    def __init__(self, symbol, function, category=None, associativity=None, precedence=None):
        """Create an Operator object.

        Parameters
        ----------
        symbol: `str`
            String representing the operator (ex: ``'+'``, ``'-'``, ``'max'``, ...).
        function: `function`
            Defines the action of the operator on its arguments.
        category: `{'unary', 'binary', function', None}`, optional
            Defines the operator category, default = `None`.
        associativity: `{'left', 'right', None}`, optional 
            Defines the operator associativity, default = `None`.
        precedence: `int` or `None`, optional
            Defines the operator precedence (low value for low precedence and high value for high precedence), default \
            = `None`.

        Examples
        --------
        .. doctest::

            >>> # define '+', '*' and 'max' operators
            >>> Operator('+', operator.add, 'binary', 'right', 2)
            <Operator '+': function=<built-in function add>, category='binary', associativity='right', precedence=2>
            >>> Operator('*', operator.mul, 'binary', 'right', 3)
            <Operator '*': function=<built-in function mul>, category='binary', associativity='right', precedence=3>
            >>> Operator('max', max, 'function', precedence=5)
            <Operator 'max': function=<built-in function max>, category='function', associativity=None, precedence=5>

            >>> # define 'my_op' operator
            >>> def my_operator(a, b, c=2, string='waffle'):
            ...     return (a + b + c) / len(string)
            ...
            >>> Operator('my_op', my_operator, 'function', precedence=5) # doctest: +ELLIPSIS
            <Operator 'my_op': function=<function my_operator at 0x...>, category='function', associativity=None, \
precedence=5>
        """
        self.symbol        = symbol
        self.function      = function
        self.category      = category
        self.associativity = associativity
        self.precedence    = precedence

    def __repr__(self):
        """Return a complete description of the operator and its characteristics."""
        return (f'<Operator \'{self.symbol}\': '
                f'function={self.function!r}, '
                f'category={self.category!r}, '
                f'associativity={self.associativity!r}, '
                f'precedence={self.precedence}>')

    def __str__(self):
        """Return a string representing the operator."""
        return self.symbol

    def apply(self, *args, **kwargs):
        """Apply the operator function to given arguments.

        Parameters
        ----------
        *args
            Arguments to give to the operator function.
        **kwargs
            Keyworded arguments to give to the operator function.
        
        Returns
        -------
        return type of ``self.function()``
            Result of the application of the operator function on the given arguments.

        Examples
        --------
        .. doctest::
            
            >>> Operator('-', lambda x: -x).apply(4)       # unary operator
            -4
            >>> Operator('+', operator.add).apply(2, 3)    # binary operator
            5
            >>> Operator('max', max).apply(2, 3, -8.6, 18) # function operator
            18

            >>> def my_operator(a, b, c=2, string='waffle'):
            ...     return (a + b + c) / len(string)
            >>> Operator('my_op', my_operator).apply(1, 2, c=3, string='hello')
            1.2
        """
        return self.function(*args, **kwargs)


class ExpressionTreeNode():
    """This class defines an expression tree node.

    A node is defined by a value and some children, a node value can be:

    - An operator (``Operator`` object), that has a various number of children (the operator function arguments).
    - A value which is an ``int``, a ``str``, or any other type accepted by the parent node operator function. If a node
      holds a value then it is a leaf, it has no children.

    Attributes
    ----------
    value: any: ``Operator`` or argument value for parent ``Operator`` node function or `None`
        Node value, if the node has children ``value`` has to be an ``Operator`` object.
    children: list of ExpressionTreeNode
        Node children, can be empty.
    """

    def __init__(self, value=None, children=[]):
        """Create an ExpressionTreeNode object.

        Parameters
        ----------
        value: any (``Operator`` or argument value for parent ``Operator`` node function)
            Node value, if the node has children ``value`` has to be an ``Operator`` object, default = `None`.
        children: list of ExpressionTreeNode
            Node children, default = `[]`.

        Examples
        --------
        .. doctest::

            >>> # define the operation '2 + 3'
            >>> ExpressionTreeNode(Operator('+', operator.add),
            ...                    children=[ExpressionTreeNode(2), ExpressionTreeNode(3)])
            +
            └── 2
            └── 3
            >>> # define the operation '1 - 5 * 4'
            >>> ExpressionTreeNode(Operator('-', operator.sub),
            ...                    children=[ExpressionTreeNode(1),
            ...                              ExpressionTreeNode(Operator('*', operator.mul),
            ...                                                 children=[ExpressionTreeNode(5),
            ...                                                           ExpressionTreeNode(4)])])
            -
            └── 1
            └── *
                └── 5
                └── 4
        """
        self.value  = value
        self.children = children

    def __repr__(self, depth=0):
        """Return a string representing the node and its child as a tree."""
        if self.is_leaf():
            string_tree = repr(self.value)
        else:
            string_tree = str(self.value)

        indentation = '    ' * depth

        for child in self.children:
            string_tree += f'\n{indentation}└── {child.__repr__(depth + 1)}'

        return string_tree

    def __str__(self):
        """Return a string representing the node and its child as a tree."""
        return repr(self)

    def get_infix(self):
        """Return a string representing the node and its child as a parenthesized infix expression.

        Returns
        -------
        `str`
            Parenthesized infix expression representing the tree.

        Examples
        --------
        .. doctest::

            >>> ExpressionTreeNode(Operator('+', operator.add, category='binary'),
            ...                    children=[ExpressionTreeNode(2), ExpressionTreeNode(3)]).get_infix()
            '(2 + 3)'
            >>> ExpressionTreeNode(Operator('-', operator.sub, category='unary'),
            ...                    children=[ExpressionTreeNode(Operator('len', len, category='function'),
            ...                                                 children=[ExpressionTreeNode('Hello')])]).get_infix()
            "-len('Hello')"
        """    
        if self.is_leaf():
            return repr(self.value)
        elif self.value.category == 'unary':
            return f'{self.value}{self.children[0].get_infix()}'
        elif self.value.category == 'binary':
            return f'({self.children[0].get_infix()} {self.value} {self.children[1].get_infix()})'
        else:
            children_separated_by_commas = ', '.join(map(lambda x: x.get_infix(), self.children))
            return f'{self.value}({children_separated_by_commas})'

    def is_leaf(self):
        """Return a boolean indicating if the node is a leaf or not.

        Returns
        -------
        `bool`
            `True` if the node has no children, `False` otherwise.

        Examples
        --------
        .. doctest::

            >>> basic_tree = ExpressionTreeNode(Operator('+', operator.add),
            ...                                 children=[ExpressionTreeNode(2), ExpressionTreeNode(3)])
            >>> basic_tree.is_leaf()
            False
            >>> basic_tree.children[0].is_leaf()
            True
        """
        return not any(self.children)

    def evaluate(self):
        """Evaluate the node by recursively evaluating its children.

        Returns
        -------
        any
            Value yielded by the evaluation of the expression tree node.

        Examples
        --------
        .. doctest::

            >>> ExpressionTreeNode(Operator('*', operator.mul),
            ...                    children=[ExpressionTreeNode(4), ExpressionTreeNode(7)]).evaluate()
            28
            >>> ExpressionTreeNode(Operator('+', operator.add),
            ...                    children=[ExpressionTreeNode('Hello'), ExpressionTreeNode(' world !')]).evaluate()
            'Hello world !'

            >>> complex_tree = ExpressionTreeNode(Operator('!', math.factorial, category='unary'),
            ...                    [ExpressionTreeNode(Operator('len', len, category='function'),
            ...                         [ExpressionTreeNode(Operator('+', operator.add, category='binary'),
            ...                             [ExpressionTreeNode('abc'),
            ...                              ExpressionTreeNode('de')])])])
            >>> complex_tree
            !
            └── len
                └── +
                    └── 'abc'
                    └── 'de'
            >>> print(complex_tree.get_infix())
            !len(('abc' + 'de'))
            >>> complex_tree.evaluate()
            120
        """
        if self.is_leaf():
            return self.value
        else:
            children_evaluated = [child.evaluate() for child in self.children]
            return self.value.apply(*children_evaluated)


class ExpressionTreeBuilder():
    """This class allows to build an expression tree from an unparenthesized well-formed infix expression.
    
    The algorithm is based on a modified version of the Shunting-yard algorithm from Wikipedia (see See Also section).

    Warnings
    --------
    This class doesn't support functions and unary operators yet.

    Class Attributes
    ----------------
    operator: `dict` with {key = operator symbol: value = corresponding ``Operator`` object}
        This dictionary holds the default operators known by the expression tree builder, contains by default ``+``, \
        ``-``, ``*``, ``/`` and ``^``.
    symbols: `str`
        String of all the symbols that can occur in the expression.
    symbols_reg: `str`
        Regular expression used to split the given infix expression.

    Attributes
    ----------
    expr: `str`
        String representing the infix expression.
    output_queue: queue of ``ExpressionTreeNode``
        Output queue of the Shunting-yard algorithm.
    operator_stack: stack of ``ExpressionTreeNode``
        Operator stack of the Shunting-yard algorithm.
    chuncks: list of `str`
        List of symbols and values in ``expr`` after splitting.
    tree: ``ExpressionTreeNode`` or `None`
        Expression tree corresponding build from an infix expression.

    See Also
    --------
    `Wikipedia 'Shunting-yard algorithm' article <https://en.wikipedia.org/wiki/Shunting-yard_algorithm>`_
    """

    operators = {'^': Operator('^', operator.pow    , 'binary', 'right', 4),
                 '*': Operator('*', operator.mul    , 'binary', 'left' , 3),
                 '/': Operator('/', operator.truediv, 'binary', 'left' , 3), 
                 '+': Operator('+', operator.add    , 'binary', 'left' , 2),
                 '-': Operator('-', operator.sub    , 'binary', 'left' , 2)}

    symbols = ''.join(operators.keys()) + '(),'
    symbols_reg = '|'.join(a+b for a,b in zip(re.escape(symbols)[::2],
                                              re.escape(symbols)[1::2]))

    def __init__(self, expr):
        """Create an ExpressionTreeBuilder object.

        Parameters
        ----------
        expr: `str`
            String representing the infix expression.
        """
        self.expr = expr
        self.output_queue = []
        self.operator_stack = []
        self.chuncks = None
        self.tree = None

    def __repr__(self):
        """Return a complete description of the expression tree builder state."""
        res = f'<Expression \'{self.expr}\': \n'

        # self.output_queue
        res += (f'   - output_queue (n = {len(self.output_queue)}) =\n'
                f'     [\n')
        for node in self.output_queue:
            res += f'        {node.__repr__(depth=2)},\n'
        res += f'     ]\n'

        # self.operator_stack
        res += (f'   - operator_stack (n = {len(self.operator_stack)}) =\n'
                f'     [\n')
        for node in self.operator_stack:
            res += f'        {node.__repr__(depth=2)},\n'
        res += f'     ]\n'

        # self.tree
        if self.tree:
            res += (f'   - tree = {self.tree.__repr__(depth=3)}>')
        else:
            res += (f'   - tree = None>')

        return res

    def __str__(self):
        """Return a complete description of the expression tree builder state."""
        return repr(self)

    def _parse_expression(self):
        """Parse the given expression to split it following `ExpressionTreeBuilder.symbol`.
        
        See Also
        --------
        `re.split() documentation <https://docs.python.org/3/library/re.html#re.split>`_

        Examples
        --------
        .. doctest::
            
            >>> x = ExpressionTreeBuilder('(1-2)*4^5')
            >>> x._parse_expression()
            >>> x.chuncks
            ['(', '1', '-', '2', ')', '*', '4', '^', '5']
        """
        self.chuncks = re.split(f'({ExpressionTreeBuilder.symbols_reg})', self.expr)
        self.chuncks = [x for x in self.chuncks if x != '']

    def _pop_last_operator_to_queue(self):
        """Pop the last operator on the stack to the output queue."""
        last_operator_node = self.operator_stack.pop()
        last_operator_node.children.append(self.output_queue.pop(0))
        self.output_queue.append(last_operator_node)

    def _operator_stack_not_empty(self):
        """Check if the operator stack is empty.

        Returns
        -------
        `bool`
            Return `True` if the operator stack is empty, `False` otherwise.
        """
        return len(self.operator_stack) > 0

    def _last_operator_on_stack(self):
        """Return the last operator on stack.

        Returns
        -------
        ``Operator``
            Last operator on the stack.
        """
        return self.operator_stack[-1].value

    def build(self, verbose=False):
        """Build an expression tree from the given infix expression.
        
        Parameters
        ----------
        verbose: `bool`
            If `True` prints the detailed state of the stacks at each stage of the build.
        """
        self._parse_expression()

        if verbose: print(f'{color("<b>→ Before build:")}\n{self}\n')

        for i, chunck in enumerate(self.chuncks):

            # if chunck is an opening parenthesis
            if chunck == '(':
                self.operator_stack.append(ExpressionTreeNode('('))

            # if chunck is a closing parenthesis
            elif chunck == ')':
                while self._operator_stack_not_empty() and self._last_operator_on_stack() != '(':
                    self._pop_last_operator_to_queue()
                self.operator_stack.pop()

            # if chunck is an operator symbol
            elif chunck in self.operators.keys():
                current_operator = ExpressionTreeBuilder.operators[chunck]

                while self._operator_stack_not_empty() and self._last_operator_on_stack() != '(' and\
                      (\
                          self._last_operator_on_stack().category == 'function'\
                          or\
                          self._last_operator_on_stack().precedence > current_operator.precedence\
                          or\
                          (self._last_operator_on_stack().precedence == current_operator.precedence and\
                           self._last_operator_on_stack().associativity == 'left')
                      ):

                    self._pop_last_operator_to_queue()

                self.operator_stack.append(ExpressionTreeNode(current_operator, [self.output_queue.pop(0)]))

            # if chunck is a value
            else:
                self.output_queue.append(ExpressionTreeNode(eval(chunck)))

            if verbose: print(f'{color("<b>→ Current:")} chunck = {chunck}, index = {i}\n{self}\n')

        # empty the operator stack
        while self._operator_stack_not_empty():
            self._pop_last_operator_to_queue()

            if verbose: print(f'{color("<b>→ Pop last operator to queue:")}\n{self}\n')

        # get the final tree
        self.tree = self.output_queue.pop()

        if verbose: print(f'{color("<b>→ Final result:")}\n{self}')

    def evaluate(self):
        """Build the tree if not built and evaluate it.
        
        Returns
        -------
        any
            Returns the type returned by the last operator called.
        """
        if not self.tree:
            self.build()

        return self.tree.evaluate()


if __name__ == '__main__':
    pass
    # t = ExpressionTreeBuilder('1+2^(10-2*3)')
    # t.build()
    # print("# FINAL")
    # print(t.tree)
    # print(repr(t.tree))
    # print(t.tree.evaluate())

    # x = ExpressionTreeBuilder('(1-2)*4^5') ; x.build(True)
