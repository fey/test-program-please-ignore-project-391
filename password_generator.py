LOWERCASE = "abcdefghijklmnopqrstuvwxyz"
UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DIGITS = "0123456789"
SPECIAL = "!@#$%^&*"


def next_random(seed: int) -> int:
    return (16807 * seed) % 2147483647


def generate_password(
    length: int,
    seed: int,
    use_uppercase: bool = True,
    use_digits: bool = True,
    use_special: bool = False,
) -> str:
    alphabet = LOWERCASE
    if use_uppercase:
        alphabet += UPPERCASE
    if use_digits:
        alphabet += DIGITS
    if use_special:
        alphabet += SPECIAL

    current = seed
    result = ""
    for _ in range(length):
        current = next_random(current)
        result += alphabet[current % len(alphabet)]
    return result


def has_lowercase(password: str) -> bool:
    for char in password:
        if "a" <= char <= "z":
            return True
    return False


def has_uppercase(password: str) -> bool:
    for char in password:
        if "A" <= char <= "Z":
            return True
    return False


def has_digit(password: str) -> bool:
    for char in password:
        if "0" <= char <= "9":
            return True
    return False


def has_special(password: str) -> bool:
    for char in password:
        if char in SPECIAL:
            return True
    return False


def is_long_enough(password: str, min_length: int = 8) -> bool:
    return len(password) >= min_length


def strength_score(password: str) -> int:
    score = 0
    if is_long_enough(password):
        score += 1
    if has_lowercase(password):
        score += 1
    if has_uppercase(password):
        score += 1
    if has_digit(password):
        score += 1
    if has_special(password):
        score += 1
    return score


def check_password(password: str) -> str:
    score = strength_score(password)
    match score:
        case 0 | 1 | 2:
            verdict = "Слабый"
        case 3:
            verdict = "Средний"
        case 4:
            verdict = "Надёжный"
        case _:
            verdict = "Очень надёжный"
    return f"{verdict} пароль (оценка {score} из 5)"
