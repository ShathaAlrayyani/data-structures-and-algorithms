from stack_and_queue.stack_and_queue import Stack
import re


def validate_brackets(string):
    reg1 = r'([\{]|[\(]|[\[])'
    reg2 = r'([\}]|[\)]|[\]])'
    matches_o = re.findall(reg1, string)
    matches_c = re.findall(reg2, string)
    node7 = Stack()
    if len(string) == 0 or len(matches_c) != len(matches_o):
        return False
    for val in string:
        if val in matches_o:
            node7.push(val)
        elif val in matches_c:
            s = matches_c.index(val)
            if val == node7.top.value or matches_o[s] == node7.top.value:
                node7.pop()
            else:
                return False
    return node7.is_empty()


if __name__ == "__main__":
    print(validate_brackets('[({}]'))
    print(validate_brackets('{}{Code}[Fellows](())'))
    print(validate_brackets('{(})'))

