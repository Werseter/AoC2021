from io import StringIO
from math import prod
from operator import eq, gt, lt


def decode_literal_packet(src: StringIO) -> tuple[int, int]:
    value, continuation_bit = [], '1'
    while continuation_bit != '0':
        continuation_bit, *value_bits = src.read(5)
        value += value_bits
    return int(''.join(value), 2), 6 + len(value) // 4 * 5


def decode_operator_packet(src: StringIO, packet_type: int) -> tuple[int, int]:
    operator_map = {0: sum, 1: prod, 2: min, 3: max, 5: lambda x: gt(*x), 6: lambda x: lt(*x), 7: lambda x: eq(*x)}
    length_type_id, expected_packet_length, expected_number_of_subpackets, overhead = src.read(1), None, None, -1
    if length_type_id == '0':
        expected_packet_length, overhead = int(src.read(15), 2), 22
    elif length_type_id == '1':
        expected_number_of_subpackets, overhead = int(src.read(11), 2), 18
    value, subpacket_len_sum, subpacket_idx = [], 0, 0
    while (expected_packet_length is not None and subpacket_len_sum < expected_packet_length
           or expected_number_of_subpackets is not None and subpacket_idx < expected_number_of_subpackets):
        subpacket_value, subpacket_len = read_packet(src)
        value.append(subpacket_value)
        subpacket_len_sum += subpacket_len
        subpacket_idx += 1
    return int(operator_map[packet_type](value)), overhead + subpacket_len_sum


def read_packet(src: StringIO) -> tuple[int, int]:
    _, packet_type = int(src.read(3), 2), int(src.read(3), 2)
    return decode_literal_packet(src) if packet_type == 4 else decode_operator_packet(src, packet_type)


with open('input.txt') as fp:
    data = bin(int(raw_str := fp.read().strip(), 16))[2:].zfill(len(raw_str) * 4)
    print(read_packet(StringIO(data))[0])
