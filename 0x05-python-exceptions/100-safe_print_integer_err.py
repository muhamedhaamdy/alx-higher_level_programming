#!/usr/bin/python3
def safe_print_integer_err(value):
    b = True
    try:
        num = int(value)
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError) as err:
        prit("Excption:", err, file=sys.stderr)
        return False
