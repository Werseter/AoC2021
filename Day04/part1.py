from dataclasses import dataclass


@dataclass
class BingoNumber:
    number: int
    marked: bool = False


@dataclass
class BingoBoard:
    rows: list[list[BingoNumber]]

    def mark_number(self, number_to_mark: int) -> None:
        for row in self.rows:
            for bingo_number in row:
                if bingo_number.number == number_to_mark:
                    bingo_number.marked = True

    @property
    def is_winning(self) -> bool:
        return (any(all(x.marked for x in col) for col in self.rows) or
                any(all(x.marked for x in row) for row in zip(*self.rows)))

    @property
    def sum_of_unmarked(self) -> int:
        return sum(x.number for row in self.rows for x in row if not x.marked)


with open('input.txt') as fp:
    numbers_drawn = [int(x) for x in fp.readline().strip().split(',')]
    tmp = fp.read().strip().split('\n\n')
    boards = [BingoBoard([[BingoNumber(int(z)) for z in y.split()] for y in x.split('\n')]) for x in tmp]

for number in numbers_drawn:
    for board in boards:
        board.mark_number(number)
        if board.is_winning:
            print(board.sum_of_unmarked * number)
            exit(0)
