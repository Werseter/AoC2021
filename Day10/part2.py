with open('input.txt') as fp:
    data = [x.strip() for x in fp.readlines()]
scoring_rules = {'(': 1, '[': 2, '{': 3, '<': 4}
closing_brackets = {')': '(', ']': '[', '}': '{', '>': '<'}
opening_brackets = set(closing_brackets.values())
autocomplete_scores = []
for line in data:
    bracket_stack = []
    for bracket in line:
        if bracket in opening_brackets:
            bracket_stack.append(bracket)
        else:
            if bracket_stack.pop() != closing_brackets[bracket]:
                break
    else:
        line_score = 0
        [line_score := line_score * 5 + scoring_rules[bracket] for bracket in bracket_stack[::-1]]
        autocomplete_scores.append(line_score)

print(sorted(autocomplete_scores)[len(autocomplete_scores) // 2])
