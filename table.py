import tkinter as tk


class Table:
    def __init__(self, num_of_rows:int, num_of_cols:int, master, min_width=50,min_height=50,padx=50,pady=50):
        self.master=master
        self.grid_cells=[]
        self.table=tk.Frame(master=self.master)
        self.table.pack(padx=padx, pady=pady)
        for i in range(num_of_rows):
            self.grid_cells.append([])

            for j in range(num_of_cols):
                text=str(i)+","+str(j)
                self.grid_cells[i].append(tk.Entry(master=self.table))
                self.grid_cells[i][j].grid(row=i,column=j)
                self.grid_cells[i][j].insert(0,text)
                self.grid_cells[i][j]['state'] = 'disabled'
                if i==0:
                    self.table.columnconfigure(j, minsize=min_width)

            self.table.rowconfigure(i, minsize=min_height)


