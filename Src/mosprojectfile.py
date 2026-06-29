import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Label, Style

# Function to display the selected option
def display_choice():
    choice = choice_var.get()
    if choice == "THICK CYLINDER":
        def calculate_stresses():    
        # Lame's equation functions for hoop and radial stresses
            def hoop_stress(r, p_i, p_o, r_i, r_o):
                A = (p_i * r_i**2 - p_o * r_o**2) / (r_o**2 - r_i**2)
                B = ((p_o - p_i) * r_i**2 * r_o**2) / (r_i**2 - r_o**2)
                return A + (B/r**2)

            def radial_stress(r, p_i, p_o, r_i, r_o):
                A = (p_i * r_i**2 - p_o * r_o**2) / (r_o**2 - r_i**2)
                B = ((p_o - p_i) * r_i**2 * r_o**2) / (r_i**2 - r_o**2)
                return A - (B/r**2)

            # Input parameters
            p_i = float(entry_internal_pressure.get())   # internal pressure in N/mm2
            p_o = float(entry_external_pressure.get())    # external pressure in N/mm2
            r_i = float(entry_inner_radius.get())    # internal radius in mm
            r_o = float(entry_outer_radius.get())    # external radius in mm

            # Generate radius values from r_i to r_o
            r_values = np.linspace(r_i, r_o, 100)
            r_mid=(r_i+r_o)/2

            # Calculate hoop and radial stresses for each radius
            hoop_stresses = hoop_stress(r_values, p_i, p_o, r_i, r_o)
            radial_stresses = radial_stress(r_values, p_i, p_o, r_i, r_o)
            hoop_stresses_mid = hoop_stress(r_mid, p_i, p_o, r_i, r_o)
            radial_stresses_mid = radial_stress(r_mid, p_i, p_o, r_i, r_o)

            # Find the extreme values for hoop and radial stresses
            max_hoop = np.max(hoop_stresses)
            min_hoop = np.min(hoop_stresses)
            max_radial = np.max(radial_stresses)
            min_radial = np.min(radial_stresses)
            # Find corresponding radii for extreme values
            max_hoop_r = r_values[np.argmax(hoop_stresses)]
            min_hoop_r = r_values[np.argmin(hoop_stresses)]
            max_radial_r = r_values[np.argmax(radial_stresses)]
            min_radial_r = r_values[np.argmin(radial_stresses)]

            # Plotting the results65yuhj
            plt.figure(figsize=(10, 6))
            # Label the extreme values
            plt.text(max_hoop_r, max_hoop, f' {max_hoop:.2f} MPa', 
                    ha='right', va='top', fontsize=10, color='blue')
            plt.text(min_hoop_r, min_hoop, f' {min_hoop:.2f} MPa', 
                    ha='left', va='bottom', fontsize=10, color='blue')

            plt.text(r_mid, hoop_stresses_mid, f' {hoop_stresses_mid:.2f} MPa', 
                    ha='center', va='top', fontsize=10, color='blue')
            plt.text(r_mid, radial_stresses_mid, f' {radial_stresses_mid:.2f} MPa', 
                    ha='center', va='bottom', fontsize=10, color='red')

            plt.text(max_radial_r, max_radial, f' {max_radial:.2f} MPa', 
                    ha='left', va='top', fontsize=10, color='red')
            plt.text(min_radial_r, min_radial, f' {min_radial:.2f} MPa', 
                    ha='right', va='bottom', fontsize=10, color='red')

            plt.axhline(0, color='black',linewidth=1)  # x-axis
            plt.axvline(0, color='black',linewidth=1)  # y-axis
            plt.axvline(r_i, color='grey',linewidth=2)
            plt.axvline(r_o, color='grey',linewidth=2)

            plt.plot(r_values, hoop_stresses, label='Hoop Stress', color='blue', lw=2)
            plt.plot(r_values, radial_stresses, label='Radial Stress', color='red', lw=2)
            plt.title('Hoop and Radial Stresses in a Thick-Walled Cylinder', fontsize=16)
            plt.xlabel('Radius (mm)', fontsize=14)
            plt.ylabel('Stress (MPa)', fontsize=14)

            plt.legend()
            plt.grid(True)
            plt.show()

        window = tk.Tk()
        window.title("Stress Calculator")
        window.geometry("1000x700")

        # Labels and Entry fields for inputs
        tk.Label(window,font=('Arial', 25), text="Inner Radius (mm):").pack()
        entry_inner_radius = tk.Entry(window,width=25,font=('Arial', 20))
        entry_inner_radius.pack(pady=10)

        tk.Label(window,font=('Arial', 25), text="Outer Radius (mm):").pack()
        entry_outer_radius = tk.Entry(window,width=25,font=('Arial', 20))
        entry_outer_radius.pack(pady=10)

        tk.Label(window,font=('Arial', 25), text="Internal Pressure (MPa):").pack()
        entry_internal_pressure = tk.Entry(window,width=25,font=('Arial', 20))
        entry_internal_pressure.pack(pady=10)

        tk.Label(window,font=('Arial', 25), text="External Pressure (MPa):").pack()
        entry_external_pressure = tk.Entry(window,width=25,font=('Arial', 20))
        entry_external_pressure.pack(pady=10)

        # Button to calculate stresses
        calculate_button = tk.Button(window,bg="light green",font=('Arial', 28), text="Calculate Stresses", command=calculate_stresses)
        calculate_button.pack(pady=30)

        # Label to display the results
        result_label = tk.Label(window, text="", font=("Arial", 12), fg="blue")
        result_label.pack(pady=10)

        # Run the application
        window.mainloop()
    elif choice == "COMPOUND CYLINDER":
        def calculate_stresses():
            p_i = float(entry_internal_pressure.get())  # internal pressure 
            p_c = float(entry_common_pressure.get())
            p_o = float(entry_external_pressure.get())  # external pressure 
            r_i = float(entry_inner_radius.get())    # inner radius
            r_c = float(entry_common_radius.get())
            r_o = float(entry_outer_radius.get())    # outer radius 

            # Define the radial positions (r) where we want to calculate the stresses
            r = np.linspace(r_i, r_o, 1000)
            r_1 = np.linspace(r_i, r_c, 1000)
            r_2 = np.linspace(r_c, r_o, 1000)

            def hoop_stress_i(r,r_1, p_i, p_c, p_o, r_i, r_c, r_o):
                A_1 = (p_c * r_c**2) / (r_i**2 - r_c**2)
                B_1 = ((p_c)*(r_c**2 *r_i**2 )) / (r_i**2 - r_c**2)
                A = (p_i * r_i**2 - p_o * r_o**2) / (r_o**2 - r_i**2)
                B = ((p_o - p_i) * r_i**2 * r_o**2) / (r_i**2 - r_o**2)
                return (A + (B/r_1**2)) + (A_1 + (B_1/r_1**2))

            def radial_stress_i(r,r_1, p_i, p_c, p_o, r_i, r_c, r_o):
                A_1 = (p_c * r_c**2) / (r_i**2 - r_c**2)
                B_1 = ((p_c)*(r_c**2 *r_i**2 )) / (r_i**2 - r_c**2)
                A = (p_i * r_i**2 - p_o * r_o**2) / (r_o**2 - r_i**2)
                B = ((p_o - p_i) * r_i**2 * r_o**2) / (r_i**2 - r_o**2)
                return (A - (B/r_1**2)) + (A_1 - (B_1/r_1**2))

            def hoop_stress_o(r,r_2, p_i, p_c, p_o, r_i, r_c, r_o):
                A_2 = (p_c * r_c**2) / (r_o**2 - r_c**2)
                B_2 = ((p_c)*(r_o**2 *r_c**2 )) / (r_o**2 - r_c**2)
                A = (p_i * r_i**2 - p_o * r_o**2) / (r_o**2 - r_i**2)
                B = ((p_o - p_i) * r_i**2 * r_o**2) / (r_i**2 - r_o**2)
                return (A + (B/r_2**2)) + (A_2 + (B_2/r_2**2))

            def radial_stress_o(r,r_2, p_i, p_c, p_o, r_i, r_c, r_o):
                A_2 = (p_c * r_c**2) / (r_o**2 - r_c**2)
                B_2 = ((p_c)*(r_o**2 *r_c**2 )) / (r_o**2 - r_c**2)
                A = (p_i * r_i**2 - p_o * r_o**2) / (r_o**2 - r_i**2)
                B = ((p_o - p_i) * r_i**2 * r_o**2) / (r_i**2 - r_o**2)
                return (A - (B/r_2**2)) + (A_2 - (B_2/r_2**2))
            # Calculate the hoop and radial stresses using Lame's equations for internal pressure

            hoop_stress_f_i = hoop_stress_i(r,r_1, p_i, p_c, p_o, r_i, r_c, r_o)
            radial_stress_f_i = radial_stress_i(r,r_1, p_i, p_c, p_o, r_i, r_c, r_o)
            hoop_stress_f_o = hoop_stress_o(r,r_2, p_i, p_c, p_o, r_i, r_c, r_o)
            radial_stress_f_o = radial_stress_o(r,r_2, p_i, p_c, p_o, r_i, r_c, r_o)

            # Find the extreme values for hoop and radial stresses
            max_hoop_i = np.max(hoop_stress_f_i)
            min_hoop_i = np.min(hoop_stress_f_i)
            max_radial_i = np.max(radial_stress_f_i)
            min_radial_i = np.min(radial_stress_f_i)
            max_hoop_o = np.max(hoop_stress_f_o)
            min_hoop_o = np.min(hoop_stress_f_o)
            max_radial_o = np.max(radial_stress_f_o)
            min_radial_o = np.min(radial_stress_f_o)
            # Find corresponding radii for extreme values
            max_hoop_r_i = r_1[np.argmax(hoop_stress_f_i)]
            min_hoop_r_i = r_1[np.argmin(hoop_stress_f_i)]
            max_radial_r_i = r_1[np.argmax(radial_stress_f_i)]
            min_radial_r_i = r_1[np.argmin(radial_stress_f_i)]
            max_hoop_r_o = r_2[np.argmax(hoop_stress_f_o)]
            min_hoop_r_o = r_2[np.argmin(hoop_stress_f_o)]
            max_radial_r_o = r_2[np.argmax(radial_stress_f_o)]
            min_radial_r_o = r_2[np.argmin(radial_stress_f_o)]

            # Plotting the results
            plt.figure(figsize=(10, 6))
            # Label the extreme values
            plt.text(max_hoop_r_i, max_hoop_i, f' {max_hoop_i:.2f} MPa', 
                    ha='right', va='top', fontsize=10, color='blue')
            plt.text(min_hoop_r_i, min_hoop_i, f' {min_hoop_i:.2f} MPa', 
                    ha='right', va='bottom', fontsize=10, color='blue')

            plt.text(max_radial_r_i, max_radial_i, f' {max_radial_i:.2f} MPa', 
                    ha='left', va='top', fontsize=10, color='red')
            plt.text(min_radial_r_i, min_radial_i, f' {min_radial_i:.2f} MPa', 
                    ha='right', va='bottom', fontsize=10, color='red')

            plt.text(max_hoop_r_o, max_hoop_o, f' {max_hoop_o:.2f} MPa', 
                    ha='left', va='top', fontsize=10, color='blue')
            plt.text(min_hoop_r_o, min_hoop_o, f' {min_hoop_o:.2f} MPa', 
                    ha='left', va='bottom', fontsize=10, color='blue')

            plt.text(max_radial_r_o, max_radial_o, f' {max_radial_o:.2f} MPa', 
                    ha='left', va='top', fontsize=10, color='red')
            plt.text(min_radial_r_o, min_radial_o, f' {min_radial_o:.2f} MPa', 
                    ha='right', va='bottom', fontsize=10, color='red')

            plt.axhline(0, color='black',linewidth=1)  # x-axis
            plt.axvline(0, color='black',linewidth=1)  # y-axis
            plt.axvline(r_i, color='grey',linewidth=2)
            plt.axvline(r_o, color='grey',linewidth=2)
            plt.axvline(r_c, color='grey',linewidth=2)

            plt.plot(r_1, hoop_stress_f_i, label='Hoop Stress', color='blue', lw=2)
            plt.plot(r_1, radial_stress_f_i, label='Radial Stress', color='red', lw=2)

            plt.plot(r_2, hoop_stress_f_o, color='blue', lw=2)
            plt.plot(r_2, radial_stress_f_o, color='red', lw=2)

            plt.title('Hoop and Radial Stresses in a Compound Cylinder', fontsize=16)
            plt.xlabel('Radius (mm)', fontsize=14)
            plt.ylabel('Stress (MPa)', fontsize=14)

            plt.legend()
            plt.grid(True)
            plt.show()

        window = tk.Tk()
        window.title("Stress Calculator")
        window.geometry("1000x800")

        # Labels and Entry fields for inputs
        tk.Label(window,font=('Arial', 25), text="Inner Radius (mm):").pack()
        entry_inner_radius = tk.Entry(window,width=25,font=('Arial', 20))
        entry_inner_radius.pack(pady=10)

        tk.Label(window,font=('Arial', 25), text="Common Surface Radius (mm):").pack()
        entry_common_radius = tk.Entry(window,width=25,font=('Arial', 20))
        entry_common_radius.pack(pady=10)

        tk.Label(window,font=('Arial', 25), text="Outer Radius (mm):").pack()
        entry_outer_radius = tk.Entry(window,width=25,font=('Arial', 20))
        entry_outer_radius.pack(pady=10)

        tk.Label(window,font=('Arial', 25), text="Internal Pressure (MPa):").pack()
        entry_internal_pressure = tk.Entry(window,width=25,font=('Arial', 20))
        entry_internal_pressure.pack(pady=10)

        tk.Label(window,font=('Arial', 25), text="Common Surface Pressure (MPa):").pack()
        entry_common_pressure = tk.Entry(window,width=25,font=('Arial', 20))
        entry_common_pressure.pack(pady=10)

        tk.Label(window,font=('Arial', 25), text="External Pressure (MPa):").pack()
        entry_external_pressure = tk.Entry(window,width=25,font=('Arial', 20))
        entry_external_pressure.pack(pady=10)

        # Button to calculate stresses
        calculate_button = tk.Button(window,bg="light green",font=('Arial', 28), text="Calculate Stresses", command=calculate_stresses)
        calculate_button.pack(pady=30)

        # Label to display the results
        result_label = tk.Label(window, text="", font=("Arial", 12), fg="blue")
        result_label.pack(pady=10)

        # Run the application
        window.mainloop()
    else:
        messagebox.showerror("Error", "Please select an option")

# Initialize Tkinter window
window = tk.Tk()
window.title("Choose an Option")
window.geometry("1000x600")

# Label for instruction
tk.Label(window, font=('Arial', 25), text="Please select the type of cylinder for stress calculations:").pack(pady=30)

# Variable to store selected option
choice_var = tk.StringVar(value="1")  # No default selection


# Radio buttons for the two options
radio_option1 = tk.Radiobutton(window,activebackground="red",font=('Arial', 30), text="THICK CYLINDER", variable=choice_var, value="THICK CYLINDER")
radio_option1.pack()

radio_option2 = tk.Radiobutton(window,activebackground="red",font=('Arial', 30), text="COMPOUND CYLINDER", variable=choice_var, value="COMPOUND CYLINDER")
radio_option2.pack()

# Button to confirm the choice
select_button = tk.Button(window,bg="light green",font=('Arial', 25), text="Confirm Choice", command=display_choice)
select_button.pack(pady=25)

# Run the application
window.mainloop()