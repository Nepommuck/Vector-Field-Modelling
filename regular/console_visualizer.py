def print_field(field):
    print('Read field:')
    for row in field:
        for item in row:
            print(f'{(" " if item is None else item):>6}', end='')
        print()
    print()


def print_dU(dU):
    print('Calculated dU:')
    for row in dU:
        for item in row:
            displ = ' '
            if item is not None:
                displ = f'({round(item[0], 2)}, {round(item[1], 2)})'
            print(f'{(" " if item is None else displ):>13}', end=' | ')
        print()
    print()
