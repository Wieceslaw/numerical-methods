def read_float(message: str, min_val: float = -1000.0, max_val: float = 1000.0, max_length: int = 18) -> float:
    message = message.strip()
    while True:
        print(message, end=f" [{min_val} ... {max_val}]: ")
        try:
            line = input().strip().replace(",", ".")
            assert len(line) <= max_length, f"Number is too long, enter number with length less than or equal" \
                                            f" {max_length - 1}"
            num = float(line)
            assert num >= min_val, f"Number should be greater than or equal {min_val}"
            assert num <= max_val, f"Number should be less than or equal {max_val}"
            return num
        except ValueError:
            print("Wrong float number format, enter again")
        except AssertionError as e:
            print(e)


def read_int(message: str, min_val: int = -1000, max_val: int = 1000, max_length: int = 16) -> int:
    message = message.strip()
    while True:
        print(message, end=f" [{min_val} ... {max_val}]: ")
        try:
            line = input().strip().replace(",", ".")
            assert len(line) <= max_length, f"Number is too long, enter number with length less than or equal" \
                                            f" {max_length - 1}"
            num = int(line)
            assert num >= min_val, f"Number should be greater than or equal {min_val}"
            assert num <= max_val, f"Number should be less than or equal {max_val}"
            return num
        except ValueError:
            print("Wrong integer number format, enter again")
        except AssertionError as e:
            print(e)


def read_string(message: str, variants: list[str]):
    message = message.strip()
    variants_set = set([s.lower() for s in variants])
    while True:
        print(message, end=f" [{', '.join(variants)}]: ")
        try:
            line = input().strip().lower()
            assert line in variants_set, f"An unsuitable string has been entered, use one of: " \
                                         f"[{', '.join(variants)}]"
            return line
        except AssertionError as e:
            print(e)
