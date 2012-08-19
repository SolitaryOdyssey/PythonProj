def QueenPuzzle(priorPos, size):
    for pos in range(size):
        if Compatible(priorPos, pos):
            if len(priorPos) == size-1:
                yield (pos,)
            else:
                results = QueenPuzzle(priorPos+(pos,), size)
                for result in results:
                    yield (pos,) + result

def Compatible(priorPos, pos):
    priorY = 0
    posY = len(priorPos)
    for prior in priorPos:
        if pos == prior or (abs(pos - prior) == posY - priorY):
            return False
        priorY = priorY + 1
    return True

if __name__ == '__main__':
    results = QueenPuzzle((), 4)
    for result in results:
        print(result)        

