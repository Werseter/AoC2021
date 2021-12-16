from io import StringIO


def decode_literal_packet(src: StringIO, packet_version: int) -> tuple[int, int]:
    value, continuation_bit = [], '1'
    while continuation_bit != '0':
        continuation_bit, *value_bits = src.read(5)
        value += value_bits
    return packet_version, 6 + len(value) // 4 * 5


def decode_operator_packet(src: StringIO, packet_version: int) -> tuple[int, int]:
    length_type_id = src.read(1)
    expected_packet_length, expected_number_of_subpackets, overhead = None, None, -1
    if length_type_id == '0':
        expected_packet_length, overhead = int(src.read(15), 2), 22
    elif length_type_id == '1':
        expected_number_of_subpackets, overhead = int(src.read(11), 2), 18
    subpacket_version_sum, subpacket_len_sum, subpacket_idx = packet_version, 0, 0
    while (expected_packet_length is not None and subpacket_len_sum < expected_packet_length
           or expected_number_of_subpackets is not None and subpacket_idx < expected_number_of_subpackets):
        subpacket_version, subpacket_len = read_packet(src)
        subpacket_version_sum += subpacket_version
        subpacket_len_sum += subpacket_len
        subpacket_idx += 1
    return subpacket_version_sum, overhead + subpacket_len_sum


def read_packet(src: StringIO) -> tuple[int, int]:
    version, packet_type = int(src.read(3), 2), int(src.read(3), 2)
    return decode_literal_packet(src, version) if packet_type == 4 else decode_operator_packet(src, version)


with open('input.txt') as fp:
    data = bin(int(raw_str := fp.read().strip(), 16))[2:].zfill(len(raw_str) * 4)
    print(read_packet(StringIO(data))[0])
