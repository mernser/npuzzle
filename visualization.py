import tkinter as tk
import tkinter.font as tk_font


class Visualization:
    def __init__(self, solution, size, args):
        self.solution = solution
        self.size = size
        self.window = tk.Tk()
        self.puzzle = []
        self.step = 0
        self.algorithm = args.search_type
        self.heuristic_type = args.heuristic_type
        self.puzzle_type = args.puzzle_type
        self.input_file = args.filename

        self.configure_window()

        self.info = tk.Label(text="Step N{}\n\nAlgo: {}\n\nPuzzle type:\n{}\n\nUniform "
                                  "Cost Search\n(Dijkstra): {}\n\n"
                                  "Heuristic\n({}): {}\n\n"
                                  "Summary: {}".format(self.step, self.algorithm, self.puzzle_type,
                                                       solution[0].g, self.heuristic_type, solution[0].h,
                                                       solution[0].f), bg='#3E4149',
                             fg="white", font=tk_font.Font(family="Courier", size=16),
                             width=30, height=20)
        self.info.grid(row=0, column=self.size, rowspan=self.size + 1)

        self.window.mainloop()

    def configure_window(self):
        window_width = self.size * 100 + 100
        window_height = self.size * 100

        width_screen = self.window.winfo_screenwidth()
        height_screen = self.window.winfo_screenheight()

        width_offset = (width_screen - window_width) // 2
        height_offset = (height_screen - window_height) // 2

        self.window.geometry('{}x{}+{}+{}'.format(window_width, window_height, width_offset, height_offset))
        self.window.resizable(False, False)
        self.window.title("N-puzzle")

        self.window.columnconfigure([i for i in range(self.size + 1)], weight=1)
        self.window.rowconfigure([i for i in range(self.size + 1)], weight=1)
        self.window.configure(bg='#3E4149')

        for i in range(len(self.solution[0].map)):
            if self.solution[0].map[i] == 0:
                cell = tk.Label(text="", bg="#34A2FE", fg="white", font=tk_font.Font(family="Times New Roman", size=20),
                                width=10, height=10)
            else:
                cell = tk.Label(text=self.solution[0].map[i], bg="black", fg="white",
                                font=tk_font.Font(family="Times New Roman", size=20),width=10, height=10)
            cell.grid(row=i // self.size, column=i % self.size, padx=1, pady=1)
            self.puzzle.append(cell)

        button_increase = tk.Button(master=self.window, text="Next", highlightbackground='#3E4149',
                                    command=lambda: None if self.step + 1 >= len(self.solution) else self.update(1))
        button_increase.grid(row=self.size + 1, column=self.size)

        button_decrease = tk.Button(master=self.window, text="Back", highlightbackground='#3E4149',
                                    command=lambda: None if self.step - 1 < 0 else self.update(-1))
        button_decrease.grid(row=self.size + 1, column=1)

    def update(self, move):
        self.step += move
        self.info.configure(text="Step N{}\n\nAlgo: {}\n\nPuzzle type:\n{}\n\nUniform "
                                 "Cost Search\n(Dijkstra): {}\n\n"
                                 "Heuristic\n({}): {}\n\n"
                                 "Summary: {}".format(self.step, self.algorithm, self.puzzle_type,
                                                      self.solution[self.step].g, self.heuristic_type,
                                                      self.solution[self.step].h, self.solution[self.step].f))

        for i in range(len(self.puzzle)):
            if self.puzzle[i].cget("text") == self.solution[self.step].map[i]:
                continue
            elif self.solution[self.step].map[i] == 0:
                self.puzzle[i].configure(text="", bg="#34A2FE")
            else:
                self.puzzle[i].configure(text=self.solution[self.step].map[i], bg="black")
