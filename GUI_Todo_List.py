import tkinter as tk


class todo:
    def __init__(self, root):
        self.root = root
        self.root.title("Todo-List")
        self.root.geometry('700x500')

        self.label1 = tk.Label(self.root, text="TO_DO_LIST_TABLE",
                              font='ariel,25', width=10, bd=5, bg='blue', fg='white')
        self.label1.pack(side='top', fill='both')

        self.label2 = tk.Label(self.root, text="FUNCTIONS_ON_TASK",
                               font='ariel,25', width=25, bd=5, bg='green', fg='white')
        self.label2.pack(side='top', fill='both')
        self.label2.place(x=400, y=55)

        self.label3 = tk.Label(self.root, text="LIST_OF_TASKS",
                               font='ariel,25', width=20, bd=5, bg='green', fg='white')
        self.label3.pack(side='top', fill='both')
        self.label3.place(x=70, y=55)

        self.main_text = tk.Listbox(
            self.root, height=15, width=30, bd=5, font='ariel, 12')
        self.main_text.place(x=40, y=120)

        self.text = tk.Text(self.root, bd=5, height=2,
                            width=30, font='ariel, 10')

        self.text.place(x=430, y=120)

        # ADD TASK

        def add():
            content = self.text.get(1.0, tk.END)
            self.main_text.insert(tk.END, content)
            with open('data.txt', 'w') as f:
                f.write(content)
                f.seek(0)
                f.close()
            self.text.delete(1.0, tk.END)


        # DELETE TASK

        def delete():
            delete1 = self.main_text.curselection()
            look = self.main_text.get(delete1)
            with open('data.txt', 'r+') as f:
                new_file = f.readlines()
                f.seek(0)
                for line in new_file:
                    item = str(look)
                    if item not in line:
                        f.write(line)
                f.truncate()
            self.main_text.delete(delete1)

        with open('data.txt', 'r') as f:
            read = f.readlines()
            for i in read:
                ready = i.split()
                self.main_text.insert(tk.END, ready)
            f.close()


        # UPDATE TASK

        def update():
            update1 = self.main_text.curselection()
            sel1 = self.main_text.get(update1)
            self.main_text.insert(tk.END, update1)
            with open('data.txt', 'w') as f:
                f.write(update1)
                f.seek(0)
                f.close()
            self.text.delete(1.0, tk.END)

        self.button1 = tk.Button(self.root, text='ADD TASK', font='ariel,15',
                                width=15, bd=5, bg='blue', fg='white', command=add)
        self.button1.place(x=450, y=200)

        self.button2 = tk.Button(self.root, text='DELETE TASK', font='ariel,15',
                                 width=15, bd=5, bg='blue', fg='white', command=delete)
        self.button2.place(x=450, y=270)

        self.button3 = tk.Button(self.root, text='UPDATE TASK', font='ariel,15',
                                 width=15, bd=5, bg='blue', fg='white', command=update)
        self.button3.place(x=450, y=340)


def main():
    root = tk.Tk()
    ui = todo(root)
    root.mainloop()

if __name__ == "__main__":
    main()
