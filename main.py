from command_line import parser_command_line
from input import input_number
from sequence import get_sequence


def main() -> str:
    arg_parser = parser_command_line()
    args = arg_parser.parse_args()
    if args.count:
        return get_sequence(args.count)
    return get_sequence(input_number())


if '__main__' == __name__:
    print(main())
