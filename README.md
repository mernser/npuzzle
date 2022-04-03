# npuzzle
Puzzle solver (python) A* algorithm

Позволяет решать пятнашки по методам алгоритма А звезда, поиск в ширину, жадный поиск, с использованием разнообразных эвристик
Определяет решаемость пятнашки (инвариант - четность перестановок)

пример использования:
python3 main.py -filename ./maps/size3_3


Для usage python3 main.py -h
usage: main.py [-heuristic {manhattan,hamming,corners,patterns,last_move}]
               [-search {a_star,greedy,uniform_cost}]
               [-puzzle {snail,classic,reverse_classic}]
               [-info {off,text,plot}] -filename FILENAME [-visualize] [-h]

WELCOME TO PUZZLE SOLVER

optional arguments:
  -heuristic {manhattan,hamming,corners,patterns,last_move}
                        choose heuristic type
  -search {a_star,greedy,uniform_cost}
                        choose search type
  -puzzle {snail,classic,reverse_classic}
                        choose terminal state type
  -info {off,text,plot}
                        choose verbosity type
  -filename FILENAME    enter valid filename with puzzle
  -visualize            enable visualization
  -h, --help            show this help message and exit
