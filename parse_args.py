import argparse

def parser_init(parser):
    parser.add_argument('-heuristic',
                        action="store", dest="heuristic_type",
                        help='\33[32mchoose heuristic type\33[0m',
                        default="manhattan", choices=["manhattan", "hamming", "corners", "patterns", "last_move"])
    parser.add_argument('-search',
                        action="store", dest="search_type",
                        help='\33[32mchoose search type\33[0m',
                        default="a_star", choices=["a_star", "greedy", "uniform_cost"])
    parser.add_argument('-puzzle', action="store", dest="puzzle_type",
                        help='\33[32mchoose terminal state type\33[0m',
                        default="snail", choices=["snail", "classic", "reverse_classic"])
    parser.add_argument('-info', action="store", dest="info",
                        help='\33[32mchoose verbosity type\33[0m',
                        default="off", choices=["off", "text", "plot"])
    parser.add_argument('-filename', action="store",
                        dest="filename", required=True,
                        help='\33[32menter valid filename with puzzle\33[0m')
    parser.add_argument('-visualize', action="store_true",
                        dest="is_visualize",
                        help='\33[32menable visualization\33[0m')
    parser.add_argument('-h', '--help', action='help', default=argparse.SUPPRESS,
                        help='\33[32mshow this help message and exit\33[0m')
    return parser.parse_args()
