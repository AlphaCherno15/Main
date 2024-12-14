import tkinter as tk

root = tk.Tk()
root.title("Prime Calculator")
root.geometry("600x200")
grid_reference = [1, 0]

def calc():
    prime_list = ["", "", "", "", ""]
    number = 0
    target = int(target_num.get())
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, num):
            if num % i == 0:
                # print(num % i)
                return False
        else:
            # print(num)
            return True

    while target > 0:
        prime = is_prime(number)
        if prime is True:
            prime_list.append(number)
            prime_list.remove(prime_list[0])
        number += 1
        target -= 1
    max_prime = max(prime_list)
    result_label = tk.Label(root, text=f'The max Prime number in {target_num.get()} numbers is {max_prime}')
    result_label.grid(row=3, column=0)
    list_label = tk.Label(root, text=f'The last 5 prime number found where {prime_list}')
    list_label.grid(row=4, column=0)

target_label = tk.Label(root, text="What is your Target for max Prime?:")
target_label.grid(row=grid_reference[0], column=grid_reference[1])
target_num = tk.Entry(root, width=10, borderwidth=2)
target_num.grid(row=grid_reference[0], column=grid_reference[1] + 1)

calc_button = tk.Button(root, text="Find", command=calc)
calc_button.grid(row=grid_reference[0] + 1, column=grid_reference[1])
root.mainloop()
