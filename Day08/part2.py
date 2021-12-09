order = (2, 3, 4, 7, 5, 6)
with open('input.txt') as fp:
    tmp = (x.partition('|')[0::2] for x in fp.readlines())
    data = [(sorted((frozenset(x) for x in a.strip().split()), key=lambda x: order.index(len(x))),
             [frozenset(x) for x in b.strip().split()]) for a, b in tmp]
total = 0
unambiguous_digit_len_conversion_map = {2: 1, 3: 7, 4: 4, 7: 8}
for raw_input, raw_output in data:
    conversion_map: dict[int, frozenset[str]] = {}
    for number_data in raw_input:
        match number_data_len := len(number_data):
            case 5:
                if number_data >= conversion_map[7]:
                    number = 3
                elif (number_data | conversion_map[1]) >= conversion_map[4]:
                    number = 5
                else:
                    number = 2
            case 6:
                if number_data >= conversion_map[4]:
                    number = 9
                elif number_data >= conversion_map[5]:
                    number = 6
                else:
                    number = 0
            case _:
                number = unambiguous_digit_len_conversion_map[number_data_len]
        conversion_map[number] = number_data
    number_lookup_map = {v: str(k) for k, v in conversion_map.items()}
    total += int(''.join(number_lookup_map[x] for x in raw_output))
print(total)
