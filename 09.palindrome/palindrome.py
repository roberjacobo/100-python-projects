def is_palindrome(word: str) -> bool:
    tmp = word.replace(" ", "").lower().casefold()
    return tmp[::-1] == tmp
