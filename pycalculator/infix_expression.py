from tools import *

class Step:
    def __init__(self, err, error_message, check_message):
        self.err = err
        self.error_message = error_message
        self.check_message = check_message

    def print(self, expr, adjusting_len):
        if any(self.err):
            print_c(f'<r>  ✘ {self.error_message: <{adjusting_len}}:</> {expr}')
            print_c(' ' * (adjusting_len + 6) +
                    ''.join(['<r>^</>' if e else ' ' for e in self.err]))
        else:
            print_c(f'<g>  ✓ {self.check_message}!</>')


class Diagnosis:
    def __init__(self):
        self.steps = []

    def add_step(self, err, error_message, check_message):
        self.steps.append(Step(err, error_message, check_message))

    def print(self, expr):
        adjusting_len = max(map(lambda x: len(x.error_message), self.steps))
        for s in self.steps:
            s.print(expr, adjusting_len)


class Expression:

    valid_char = '0123456789()+- '

    def __init__(self, expr):
        self.expr = expr
        self.err  = [False for _ in self.expr]
        self.diagnosis = Diagnosis()
        # self.result = NA


    def print_diagnosis(self):
        self.diagnosis.print(self.expr)


    def reset_err(self):
        self.err  = [False for _ in self.expr]


    def found_error(self):
        if any(self.err):
            return True
        else:
            return False


    def check_characters(self):
        #self.reset_err()
        self.err = [True if not c in self.valid_char
                         else False
                         for c in self.expr]

        self.diagnosis.add_step(self.err, 'unknown characters', 'checked characters')

        return self.found_error()


    def check_parenthesing(self):
        # could be implemented with count variable only
        self.reset_err()
        opened_index = []

        for i, c in enumerate(self.expr):
            if c == '(':
                opened_index.append(i)
            elif c == ')':
                if len(opened_index) == 0:
                    self.err[i] = True
                else:
                    opened_index.pop(0)

        for i in opened_index:
            self.err[i] = True

        self.diagnosis.add_step(self.err, 'wrong parenthesing', 'checked parenthesing')

        return self.found_error()


    def remove_spaces(self):
        self.expr = self.expr.replace(' ', '')


    def check_syntax(self):
        last_was_sym = False
        self.reset_err()

        for i, c in enumerate(self.expr):
            if c in self.symbols:
                if last_was_sym:
                    self.err[i - 1] = True
                    self.err[i] = True
                
                last_was_sym = True
            elif c == ' ':
                pass
            else:
                last_was_sym = False

        if self.expr[-1] in self.symbols:
            self.err[-1] = True

        self.diagnosis.add_step(self.err, 'wrong syntax', 'checked syntax')

        return self.found_error()


    def evaluate(self):        
        self.result = 3
        print_c(f'<b><+>  ● Result:</> {self.result}')
        return 3


        # print(self.symbols_reg)
        # print(re.split(self.symbols_reg, self.expr))

if __name__ == '__main__':
    for expr in [')1 + 2 # ?/ 45 ++ 7',
                 '1 + 2 + 45 -- 8',
                 '- 1 + 2 + 45 -- 8 +',
                 '1 + 2 + 45 - 8',
                 '(1 + 2 + 45 - 8)',
                 '(1 + 2 + 45 - 8))',
                 '())(1 + 2 + 45 - 8)(()(']:
        print('→ ' + expr)
        e = Expression(expr)
        e.check_characters()
        e.check_parenthesing()
        e.check_syntax()
        e.print_diagnosis()
        e.evaluate()
        print()


# x = input('→ ')
# e = Expression(x)
# e.check_characters()

# live suggestion
# colors
# handle empty
# handle \n
# proposed correction
# better name
# check existing 'parse equation in Python'
# enable multi-parenthesing with [] and {}
# Infix to Expression Tree
