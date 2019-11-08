import math

MAX_COUNT = 100000 * 1000


def get_max_segment(array, previous_max_segment_length=0):
    max_segment = {
        'start': 0,
        'end': 0,
        'length': 0
    }
    index = 0
    while index < len(array):
        if array[index] == 0:
            start = index
            for jindex in range(start, len(array)):
                if array[jindex] == 0:
                    end = jindex
                    index += 1
                else:
                    break
            length = end - start + 1
            if length == previous_max_segment_length:
                segment = {
                    'start': start,
                    'end': end,
                    'length': length
                }
                max_segment = segment
                return max_segment
            if length > max_segment['length']:
                segment = {
                    'start': start,
                    'end': end,
                    'length': length
                }
                max_segment = segment
        index += 1
    return max_segment


def simulation(rocks_count, bugs_count):
    rocks = [0 for x in range(rocks_count)]
    bug = 1
    previous_max_segment_length = get_max_segment(rocks)['length']
    while bug <= bugs_count:
        max_segment = get_max_segment(rocks, previous_max_segment_length)
        previous_max_segment_length = max_segment['length']
        index = int((max_segment['start'] + max_segment['end']) / 2)
        rocks[index] = bug
        bug += 1
    return rocks


def get_left_and_right(rocks, bugs_count):
    last_bug_index = rocks.index(bugs_count)
    i = last_bug_index - 1
    left = 0
    while i >= 0:
        if rocks[i] == 0:
            left += 1
        else:
            break
        i -= 1
    i = last_bug_index + 1
    right = 0
    while i <= len(rocks) - 1:
        if rocks[i] == 0:
            right += 1
        else:
            break
        i += 1
    return left, right


def get_approximately_left_and_right(bugs_count, rocks_count):
    number = int(math.log(bugs_count, 2))
    if bugs_count == 1:
        delimiter = 2
    else:
        delimiter = 2 ** (number + 1)
    left = int(rocks_count / delimiter) - 1
    right = int(rocks_count / delimiter)
    return left, right


def main():
    bugs_count = int(input('Введите количество жуков: '))
    rocks_count = int(input('Введите количество камней: '))
    if bugs_count * rocks_count < MAX_COUNT:
        rocks = simulation(rocks_count, bugs_count)
        left, right = get_left_and_right(rocks, bugs_count)
    else:
        left, right = get_approximately_left_and_right(bugs_count, rocks_count)
    print(f'Количество свободных камней слева: {left} \nКоличество свободных камней справа: {right}')


if __name__ == '__main__':
    main()
