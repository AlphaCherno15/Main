import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import math


def calculate_force(angle, weight, length):
    """
    Calculate the required piston force to open a tailgate.
    :param angle: Opening angle of the tailgate in degrees.
    :param weight: Weight of the tailgate in kilograms.
    :param length: Length of the piston in meters.
    :return: Required force in Newtons.
    """
    g = 9.81  # Gravitational acceleration in m/s²
    force = (weight * g * length) / (2 * math.sin(math.radians(angle)))
    return force


def plot_force():
    """
    Plot the required piston force against different tailgate angles.
    """
    weight = float(weight_entry.get())
    length = float(length_entry.get())

    angles = range(5, 90, 2)  # Angles from 10 to 85 degrees
    forces = [calculate_force(angle, weight, length) for angle in angles]

    # Plotting
    plt.figure(figsize=(8, 6))
    plt.plot(angles, forces, marker='o', label='Piston Force')
    plt.title('Piston Force vs Tailgate Angle')
    plt.xlabel('Angle (degrees)')
    plt.ylabel('Force (Newtons)')
    plt.grid(True)
    plt.legend()
    plt.show()


def display_result():
    """
    Display the required piston force for the given parameters.
    """
    try:
        angle = float(angle_entry.get())
        weight = float(weight_entry.get())
        length = float(length_entry.get())
        force = calculate_force(angle, weight, length)
        result_label.config(text=f"Required Force: {force:.2f} N")
    except ValueError:
        result_label.config(text="Error: Please enter valid numbers.")


# Create the main window
root = tk.Tk()
root.title("Piston Force Calculator")

# Input fields
angle_label = tk.Label(root, text="Tailgate Angle (degrees):")
angle_label.grid(row=0, column=0, padx=10, pady=5)
angle_entry = tk.Entry(root)
angle_entry.grid(row=0, column=1, padx=10, pady=5)

weight_label = tk.Label(root, text="Tailgate Weight (kg):")
weight_label.grid(row=1, column=0, padx=10, pady=5)
weight_entry = tk.Entry(root)
weight_entry.grid(row=1, column=1, padx=10, pady=5)

length_label = tk.Label(root, text="Piston Length (m):")
length_label.grid(row=2, column=0, padx=10, pady=5)
length_entry = tk.Entry(root)
length_entry.grid(row=2, column=1, padx=10, pady=5)

# Buttons
calculate_button = tk.Button(root, text="Calculate Force", command=display_result)
calculate_button.grid(row=3, column=0, columnspan=2, pady=10)

plot_button = tk.Button(root, text="Plot Force vs Angle", command=plot_force)
plot_button.grid(row=4, column=0, columnspan=2, pady=10)

# Result label
result_label = tk.Label(root, text="", font=("Helvetica", 12))
result_label.grid(row=5, column=0, columnspan=2, pady=10)

# Run the main loop
root.mainloop()
