with open('input.txt') as fp:
    data = (x.strip() for x in fp.readlines())
scoring_rules = {')': 3, ']': 57, '}': 1197, '>': 25137}
closing_brackets = {')': '(', ']': '[', '}': '{', '>': '<'}
opening_brackets = set(closing_brackets.values())
total_error_score = 0
for line in data:
    bracket_stack = []
    for bracket in line:
        if bracket in opening_brackets:
            bracket_stack.append(bracket)
        else:
            if bracket_stack.pop() != closing_brackets[bracket]:
                total_error_score += scoring_rules[bracket]
                break
print(total_error_score)
