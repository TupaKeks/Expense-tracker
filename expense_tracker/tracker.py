import tkinter as tk
import tkinter.ttk as ttk
from tkinter.simpledialog import askstring, askinteger

data = []
index = 1


def add_month(tree, window):
    global index
    try:
        month = askstring("Input", "enter a month", parent=window)
        income = askinteger("Input", "enter your income", parent=window)
        spent = askinteger("Input", "enter how much did you spend", parent=window)
        remain = income - spent
        data.append([month, income, spent, remain])
        current_index = index
        tree.insert("", tk.END, iid=current_index, text=month, values=[income, spent, remain])
        index += 1
    except Exception as e:
        print(e)


def show_expense_details(tree, window):
    selected_item = tree.selection()
    if selected_item:
        item_values = tree.item(selected_item, 'values')
        month = tree.item(selected_item, 'text')

        detail_window = tk.Toplevel(window)
        detail_window.title(f"Details for {month}")
        detail_window.geometry("300x200")

        tk.Label(detail_window, text=f"Month: {month}").pack()
        tk.Label(detail_window, text=f"Income: {item_values[0]}").pack()
        tk.Label(detail_window, text=f"Spending: {item_values[1]}").pack()
        tk.Label(detail_window, text=f"Remain: {item_values[2]}").pack()


def delete_item(tree, data):
    selected_items = tree.selection()
    for item in selected_items:
        month = tree.item(item, 'text')
        for entry in data:
            if entry[0] == month:
                data.remove(entry)
                break
        tree.delete(item)


def main():
    window = tk.Tk()
    window.title("Expense tracker")
    window.geometry("800x400")

    columns = ("income", "spending", "remain")

    frame = tk.Frame(window, relief=tk.RAISED, bd=2)

    add_btn = tk.Button(frame, text="Add month string", command=lambda: add_month(tree, window))
    add_btn.grid(row=0, column=0, sticky="ew", padx=5, pady=5)

    show_details_btn = tk.Button(frame, text="Show details", command=lambda: show_expense_details(tree, window))
    show_details_btn.grid(row=0, column=1, sticky="ew", padx=5, pady=5)

    delete_btn = tk.Button(frame, text="Delete item", command=lambda: delete_item(tree, data))
    delete_btn.grid(row=0, column=2, sticky="ew", padx=5, pady=5)

    frame.grid(row=0, column=0)

    tree = ttk.Treeview(window, columns=columns, height=20)
    tree.grid(row=1, column=0)

    tree.heading("#0", text="Month")
    tree.heading("income", text="Income")
    tree.heading("spending", text="Spending")
    tree.heading("remain", text="Remain")

    window.mainloop()


main()
