def sum_all(*numbers: int) -> int:
    result = 0
    for n in numbers:
        result += n
    return result
