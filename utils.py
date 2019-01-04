
def row_to_str(row):
    outstr = ''
    for elem in row:
        if elem == 1:
            outstr += 'O'
        else:
            outstr += ' '
    return outstr