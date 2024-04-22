from command_line import parser_command_line
from input import input_number
from sequence import get_sequence


if '__main__' == __name__:
    arg_parser = parser_command_line()
    args = arg_parser.parse_args()
    if args.count:
        sequence = get_sequence(args.count)
    else:
        sequence = get_sequence(input_number())
    print(sequence)
