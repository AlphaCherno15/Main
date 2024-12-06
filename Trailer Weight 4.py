import pandas as pd
import tkinter as tk
import math 
import re
from tkinter import ttk

# Load data from CSV test expression and eval
LBfile_path = r"C:\Users\rperon\OneDrive - Trout River Industries\Documents\Documents\CSV LB.csv"
HYCfile_path = r"C:\Users\rperon\OneDrive - Trout River Industries\Documents\Documents\CSV HYC.csv"
RIBfile_path = r"C:\Users\rperon\OneDrive - Trout River Industries\Documents\Documents\RIB SPACING LB.csv"
CSV_LB = pd.read_csv(LBfile_path)
CSV_HYC = pd.read_csv(HYCfile_path)
ribdata = pd.read_csv(RIBfile_path)


root = tk.Tk() 
root.title("Trailer Configuration")
root.geometry("1000x500")
H = 1
L = 1
pad_inf = [5, 5]
Height_confirm_infogrid = [10, 0]  # grid position reference
Length_confirm_infogrid = [11, 0]  # grid position reference
def Trailer_H(any):
    global H
    if any == 59.5:
        H = any 
        label = tk.Label(root, text="Height is set to LV")
        label.grid(row=Height_confirm_infogrid[0], column=Height_confirm_infogrid[1])
    elif any == 72:
        H = any
        label = tk.Label(root, text="Height is set to SC")
        label.grid(row=Height_confirm_infogrid[0], column=Height_confirm_infogrid[1])
    elif any == 82:
        H = any
        label = tk.Label(root, text="Height is set to HC")
        label.grid(row=Height_confirm_infogrid[0], column=Height_confirm_infogrid[1])
    else:
        H = float(custom_h.get())
        label = tk.Label(root, text=f"Height is set to {H}")
        label.grid(row=Height_confirm_infogrid[0], column=Height_confirm_infogrid[1])

def Trailer_L():
    global L
    if float(L_def.get()) <= 52:
        L = float(L_def.get()) * 12
        label = tk.Label(root, text=f"Length is set to {L} Inches")
        label.grid(row=Length_confirm_infogrid[0], column=Length_confirm_infogrid[1])
    elif any == 53:
        L == 52.5 * 12
        label = tk.Label(root, text=f"Length is set to {L} Inches")
        label.grid(row=Length_confirm_infogrid[0], column=Length_confirm_infogrid[1])
    else:
        L = float(L_def.get()) * 12
        label = tk.Label(root, text=f"Length is too Big")
        label.grid(row=Length_confirm_infogrid[0], column=Length_confirm_infogrid[1])

LB_Button = tk.Button(root, text="Live Bottom", command=lambda: Trailer_H(59.5)).grid(row=0, column=0)
HYC_Button = tk.Button(root, text="Hycube", command=lambda: Trailer_H(59.5)).grid(row=0, column=1)



# Hight widgets
H_infogrid = [1, 0] # grid position reference
LV_Button = tk.Button(root, text="LV", command=lambda: Trailer_H(59.5)).grid(row=H_infogrid[0], column=H_infogrid[1])
SC_Button = tk.Button(root, text="SC", command=lambda: Trailer_H(72)).grid(row=H_infogrid[0], column=H_infogrid[1] + 1)
HC_Button = tk.Button(root, text="HC", command=lambda: Trailer_H(82)).grid(row=H_infogrid[0], column=H_infogrid[1] + 2)

H_label = tk.Label(root, text="Enter Height (Inch)")
H_label.grid(row=H_infogrid[0] + 1, column=H_infogrid[1])
custom_h = tk.Entry(root, width=10, borderwidth=2)
custom_h.grid(row=H_infogrid[0] + 1, column=H_infogrid[1] + 1)
Custom_Button = tk.Button(root, text="Set", command=lambda: Trailer_H(1.0)).grid(row=H_infogrid[0] + 1, column=H_infogrid[1] + 2)
# Length widgets
L_infogrid = [3, 0] # grid position reference
L_label = tk.Label(root, text="Enter Length (Feet)")
L_label.grid(row=L_infogrid[0], column=L_infogrid[1])
L_def = tk.Entry(root, width=10, borderwidth=2)
L_def.grid(row=L_infogrid[0], column=L_infogrid[1] + 1)
L_def_Button = tk.Button(root, text="Set", command=Trailer_L).grid(row=3, column=2)
# Dropdown options
O_infogrid = [4, 0] # grid position reference
Skin_options = ["Aluminum", "Stainless Steel"]
Tailgate_options = ["Standard", "Knifegate", "Manual Grain Door", "Air Grain Door", "Produce Door", "Aluminum"]
Tailgate_Actuator_options = ["Air Cylinder", "Hydraulic Cylinder"]
Fron_Sheet_Option = ["Standard", "Front Door"]
fith_wheel_option = ["55, 18", "61, 18", "55, 24", "55, 36", "80, 18"]
Axle_Options = ["F", "L","S", "C","D"]
Axle_Spread_Options = [44, 52, 60, 71.5]

# Dropdown variable
dropdown_skin = tk.StringVar(value="Select Skin Type")
dropdown_Tailgate = tk.StringVar(value="Select TailGate Type")
dropdown_TailgateAc = tk.StringVar(value="Select Actuator Type")
dropdown_FrontSheet = tk.StringVar(value="Select Front sheet Type")

# Dropdown menu
Skin_dropdown = ttk.Combobox(root, textvariable=dropdown_skin, values=Skin_options, state="readonly")
Skin_dropdown.grid(row=O_infogrid[0], column=O_infogrid[1], padx=5, pady=5)
TG_dropdown = ttk.Combobox(root, textvariable=dropdown_Tailgate, values=Tailgate_options, state="readonly")
TG_dropdown.grid(row=O_infogrid[0], column=O_infogrid[1] + 1, padx=5, pady=5)
TGA_dropdown = ttk.Combobox(root, textvariable=dropdown_TailgateAc, values=Tailgate_Actuator_options, state="readonly")
TGA_dropdown.grid(row=O_infogrid[0], column=O_infogrid[1] + 2, padx=5, pady=5)
FS_dropdown = ttk.Combobox(root, textvariable=dropdown_FrontSheet, values=Fron_Sheet_Option, state="readonly")
FS_dropdown.grid(row=O_infogrid[0], column=O_infogrid[1] + 3, padx=8, pady=8)

# Define a variable to store the checkbox state
Side_Ladder = tk.IntVar()  # 0 is unchecked, 1 is checked
Release_Agent_tank = tk.IntVar()
Asphalt_Chute = tk.IntVar()

# Create a checkbox
O2_infogrid = [5, 0] # grid position reference
checkbox_1 = tk.Checkbutton(root, text="Side Ladder", variable=Side_Ladder)
checkbox_1.grid(row=O2_infogrid[0], column=O2_infogrid[1])
checkbox_2 = tk.Checkbutton(root, text="Release Agent Tank", variable=Release_Agent_tank)
checkbox_2.grid(row=O2_infogrid[0], column=O2_infogrid[1] + 1)
checkbox_3 = tk.Checkbutton(root, text="Asphalt Chute", variable=Asphalt_Chute)
checkbox_3.grid(row=O2_infogrid[0], column=O2_infogrid[1] + 2)

fith_Wheel = tk.IntVar(value="Select Pin Set")
Axle_Spread = tk.IntVar(value="Select Value")
Axle_1 = tk.StringVar(value="No Axle")
Axle_2 = tk.StringVar(value="No Axle")
Axle_3 = tk.StringVar(value="No Axle")
Axle_4 = tk.StringVar(value="No Axle")
Axle_5 = tk.StringVar(value="No Axle")
Axle_6 = tk.StringVar(value="No Axle")

# Create a checkbox
A_infogrid = [7, 0] # grid position reference
fith_wheel = ttk.Combobox(root, textvariable=fith_Wheel, values=fith_wheel_option, state="readonly")
fith_wheel.grid(row=A_infogrid[0] - 1, column=A_infogrid[1], padx=pad_inf[0], pady=pad_inf[1])
Ax_Spread = ttk.Combobox(root, textvariable=Axle_Spread, values=Axle_Spread_Options, state="readonly")
Ax_Spread.grid(row=A_infogrid[0] - 1, column=A_infogrid[1] + 1, padx=pad_inf[0], pady=pad_inf[1])
Ax_1 = ttk.Combobox(root, textvariable=Axle_1, values=Axle_Options, state="readonly")
Ax_1.grid(row=A_infogrid[0], column=A_infogrid[1], padx=pad_inf[0], pady=pad_inf[1])
Ax_2 = ttk.Combobox(root, textvariable=Axle_2, values=Axle_Options, state="readonly")
Ax_2.grid(row=A_infogrid[0], column=A_infogrid[1] + 1, padx=pad_inf[0], pady=pad_inf[1])
Ax_3 = ttk.Combobox(root, textvariable=Axle_3, values=Axle_Options, state="readonly")
Ax_3.grid(row=A_infogrid[0], column=A_infogrid[1] + 2,padx=pad_inf[0], pady=pad_inf[1])
Ax_4 = ttk.Combobox(root, textvariable=Axle_4, values=Axle_Options, state="readonly")
Ax_4.grid(row=A_infogrid[0], column=A_infogrid[1] + 3, padx=pad_inf[0], pady=pad_inf[1])
Ax_5 = ttk.Combobox(root, textvariable=Axle_5, values=Axle_Options, state="readonly")
Ax_5.grid(row=A_infogrid[0], column=A_infogrid[1] + 4, padx=pad_inf[0], pady=pad_inf[1])
Ax_6 = ttk.Combobox(root, textvariable=Axle_6, values=Axle_Options, state="readonly")
Ax_6.grid(row=A_infogrid[0], column=A_infogrid[1] + 5, padx=pad_inf[0], pady=pad_inf[1])

data = CSV_LB
def RQ(): # Function to find the highest column index with a non-None value
    Q = ribdata[ribdata["inch"] <= L].iloc[-1] # Find the row corresponding to the given trailer length
    max_column = None # Initialize variable to store the highest column number with a non-None value
    for col in ribdata.columns[1:]:
        if pd.notna(Q[col]): 
            max_column = int(col) # Update with the highest column
    return max_column # Return the highest column found

def bogie_type():# Function to define Bogie Type: LFF71.5
    # List of possible Axle inputs
    axles = [Axle_6.get(), Axle_5.get(), Axle_4.get(), Axle_3.get(), Axle_2.get(), Axle_1.get(), str(Ax_Spread.get())]
    
    # Filter out "No Axle" and convert other values to integers
    axlegroup = "".join(axle for axle in axles if axle != "No Axle")
    return axlegroup

N_axles = lambda: sum(1 for x in bogie_type() if any(char.isalpha() for char in x))
Fix_axles = lambda: sum(1 for x in bogie_type() if x in {"F"})
Lift_axles = lambda: sum(1 for x in bogie_type() if x in {"L"})
Steer_axles = lambda: sum(1 for x in bogie_type() if x in {"S"})
Comp_Lift_axles = lambda: sum(1 for x in bogie_type() if x in {"C"})
Disc_axles = lambda: sum(1 for x in bogie_type() if x in {"D"})   

class Elements:
    def find_target_row(self, data, t_name):
        try:
            matching_rows = data[data.isin([t_name])].stack().index.get_level_values(0).tolist()
            for idx in matching_rows:
                condition = data.iloc[idx, 1]
                if isinstance(condition, str): # If the condition is a string, evaluate it
                    condition = condition.replace('$H', str(H)).replace('$L', str(L))
                    if eval(condition) is True:
                        return idx
            return matching_rows[0] if matching_rows else None
        except IndexError:
            return None
    def Quant(self, data, t_name):
        target_row_index = self.find_target_row(data, t_name)
        if target_row_index is None:
            return 0
        try:
            expression = data.iloc[target_row_index, 5]
            if expression.isnumeric():
                return float(expression) 
            elif isinstance(expression, str):
                expression = expression.replace('$H', str(H)).replace('$L', str(L)).replace('$RQ', str(RQ())).replace('$NS', str(N_axles())).replace('$AS', str(Axle_Spread.get())).replace('$Z', str(Steer_axles())).replace('$X', str(Lift_axles()))
                if "IF" in expression:
                    conditional_pattern = r'IF\((.*?)\)\{(.*?)\}'
                    matches =  re.findall(conditional_pattern, expression)
                    for condition, result in matches:
                        if eval(condition):  # Safely evaluate the condition
                            return float(result)
                    else_match = re.search(r'ELSE\{(.*?)\}', expression)
                    if else_match:
                        return float(else_match.group(1))   
                elif "ROUND" in expression:
                    expression = expression.replace("ROUND","")
                    number = float(eval(expression))
                    roundup = math.ceil(number)
                    return roundup
                else:
                    return float(eval(expression))
        except Exception as e:
            print(f"An error occurred while processing the expression erro linha 254: {expression}\nError: {e}")
            return 0
    def eval1(self, data, t_name,):
        target_row_index = self.find_target_row(data, t_name)
        if target_row_index is None:
            return 0
        Q = self.Quant(data, t_name=t_name)
        try:
            expression = data.iloc[target_row_index, 6]
            quant = data.iloc[target_row_index, 7]
            if expression.isnumeric():
                return float(expression) * float(quant) * Q
            elif isinstance(expression, str):
                try:
                    expression = expression.replace('$H', str(H)).replace('$L', str(L)).replace('$RQ', str(RQ())).replace('$NS', str(N_axles())).replace('$AS', str(Axle_Spread.get())).replace('$Z', str(Steer_axles())).replace('$X', str(Lift_axles()))
                    result = eval(expression)
                    return float(result) * float(quant) * Q
                except Exception as e:
                    print(f"erro linha 225: {e}")
        except Exception as e:
            print(f"erro linha 230: {e}")
            return 0
    def mult_eval(self, data, t_name):
        target_row_index = None
        for idx in range(len(data)):
            if data.iloc[idx, 0] == t_name:  # Adjust index if `t_name` is in another column
                target_row_index = idx
                break
        if target_row_index is None:
            print(f"Target name '{t_name}' not found.")
            return []
        print(f"Starting at row {target_row_index} for target name '{t_name}'.")
        m = 0
        for row_idx in range(target_row_index, len(data)):
            # Stop if a blank row is found in the t_name column
            if pd.isna(data.iloc[row_idx, 0]):  # Adjust index if blank check is in another column
                print(f"Stopping at row {row_idx} due to blank t_name.")
                break
            # Process the row (this is where you can add custom logic)
            row_data = data.iloc[row_idx, 0]
            m1 = self.eval1(data, t_name=row_data)
            m2 = 0 #self.Quant(data, t_name=row_data)
            m += m1
            # Debug output for the processed row
            print(f"Processed row {row_idx}")
            print(row_data)
        return m





calc = Elements() 

def fw():
    corresponding_values = ["2.4.5", "2.4.6", "2.4.7", "2.4.8", "2.4.9"]
    selected_option = fith_wheel.get()
    try:
        index = fith_wheel_option.index(selected_option)
        return corresponding_values[index]
    except ValueError:
        # Handle case when the selected_option is not in the list
        return "2.4.5"
def skinmass():# Function to define skin type and
    if Skin_dropdown.get() == "Aluminum":
        return calc.eval1(data, t_name="1.2.8", c_1=6) * calc.Qsingle(data, t_name="1.2.8", c_1=5) 
    elif Skin_dropdown.get() == "Stainless Steel":
        return calc.eval1(data, t_name="1.2.9", c_1=6) * calc.Qsingle(data, t_name="1.2.9", c_1=5)
    else:
        return 0   
def tgH():# Function to define tailgate height
    if H <= 65:
        return ".3"
    elif 65 < H <= 75:
        return ".2"
    elif H > 75:
        return ".1"
    else:
        return 0
def tgT():# Function to define tailgate type
    corresponding_values = [".1", ".2", ".3", ".4", ".5", ".6"]
    selected_option = TG_dropdown.get()
    try:
        index = Tailgate_options.index(selected_option)
        return corresponding_values[index]
    except ValueError:
        # Handle case when the selected_option is not in the list
        return ".1"

def tga():# Function to define tailgate actuator
    if TGA_dropdown.get() == "Air Cylinder":
        return "1.2.10"
    elif TGA_dropdown.get() == "Hydraulic Cylinder":
        return "1.2.11"
    else:
        return 0
def fsH():# Function to define tailgate height
    if H == 59.5:
        return ".3"
    elif H == 72:
        return ".2"
    elif H == 82:
        return ".1"
    else:
        return ".4"
def fsT():# Function to define frontsheet type
    if FS_dropdown.get() == "Standard":
        return ".2"
    elif FS_dropdown.get() == "Front Door":
        return ".3"
    else:
        return "0"
def varaiables_RS(): #still pricing
    if H in [59.5, 72, 82]:
        return 0
    else:
        return 1

def fenders():
    non_steerGroup = [Axle_2.get(), Axle_3.get(), Axle_4.get(), Axle_5.get(), Axle_6.get()]
    steerGroup = [Axle_2.get(), Axle_3.get(), Axle_4.get(), Axle_5.get(), Axle_6.get()]
    fender_ns = sum(1 for ns in non_steerGroup if ns in {"F", "L", "C", "D"})
    fenders_s = sum(1 for s in steerGroup if s == "S")
    Rear_fender = "4.3.13" if Axle_1.get() == "S" else "4.3.12"
    m1 = fender_ns * calc.eval1(data, t_name="4.3.10")
    m2 = fenders_s * calc.eval1(data, t_name="4.3.11")
    m3 = calc.eval1(data, t_name=Rear_fender)
    return m1 +m2 +m3
def bogie_mass():
    Bogie_weld = data[data.isin([bogie_type()]).any(axis=1)]
    if not Bogie_weld.empty:
        name1 = Bogie_weld.iloc[0, 0]
    else:
        x1 = calc.mult_eval(data, t_name="4.1.1")
        x2 = ((calc.eval1(data, t_name="4.1.12")) +
        (calc.eval1(data, t_name="4.1.13")) +
        (calc.eval1(data, t_name="4.1.19")) + 
        (calc.eval1(data, t_name="4.1.20"))
        )
        x3 = (calc.eval1(data, t_name="4.1.14") * (Steer_axles())) + (calc.eval1(data, t_name="4.1.15") * (Steer_axles())) + (calc.eval1(data, t_name="4.1.21") * (Steer_axles())) 
        x4 = calc.mult_eval(data, t_name="4.1.9") if Fix_axles() > 0 else 0
        x5 = calc.mult_eval(data, t_name="4.1.22") if Steer_axles() > 0 else 0
        x6 = calc.mult_eval(data, t_name="4.1.26") if Steer_axles() > 0 else 0
        x7 = x5 if Steer_axles() > 0 else x4
        name1 = x1 + x2 + x3 + x6 + x7

    mf = calc.eval1(data, t_name="4.3.2") * Fix_axles()
    md = calc.eval1(data, t_name="4.3.2") * Disc_axles()
    mc = calc.mult_eval(data, t_name="4.3.3") * Comp_Lift_axles()
    ml = calc.mult_eval(data, t_name="4.3.5") * Lift_axles()
    ms = calc.mult_eval(data, t_name="4.3.7") * Steer_axles()
    wheel = calc.eval1(data, t_name="4.3.20") * N_axles()
    Bw_mass2 = calc.eval1(data, t_name=name1)
    Bw_mass1 = name1
    Bw_mass = calc.mult_eval(data, t_name="4.3.18") + (Bw_mass2 if Bw_mass2 > 0 else Bw_mass1)
    f = fenders()
    return mf + md + mc + ml + ms + Bw_mass + f + wheel 


def Optionals_mass():
    o1 = Side_Ladder.get() * calc.eval1(data, t_name="1.2.1")
    o2 = Release_Agent_tank.get() * calc.eval1(data, t_name="1.2.2") 
    o3 = Asphalt_Chute.get() * calc.eval1(data, t_name="1.2.4")
    return o1 + o2 + o3

def Fix(type):
    m1 = calc.mult_eval(data, t_name="1.1")
    m2 = calc.mult_eval(data, t_name="1.1.1.1")
    m3 = calc.mult_eval(data, t_name="1.1.1")

    p1 = 1
    p2 = 1
    p3 = 1

    if type == "mass":
        return m1 + m2 + m3
    elif type == "price":
        return p1 + p2 + p3
    else: 
        return 0
def front_sheet(type):
    m1 = calc.mult_eval(data, t_name=f"2.1{fsT()}{fsH()}")
    m2 = calc.mult_eval(data, t_name=f"2.1.1{fsH()}")
    m3 = calc.eval1(data, t_name=f"2.1.1.1{fsH()}") + calc.eval1(data, t_name=f"2.1.1.2{fsH()}")
    m4 = varaiables_RS()
    if type == "mass":
        return m1 + m2 + m3 + m4
    elif type == "price":
        return 1
    else: 
        return 0

def Tailgate(type):
    m1 = calc.mult_eval(data, t_name=f"1.3{tgT()}{tgH()}")
    m2 = calc.mult_eval(data, t_name=tga())
    
    p1 = 1
    p2 = 1
    if type == "mass":
        return m1 + m2
    elif type == "price":
        return p1 + p2
    else: 
        return 0

def Tub(type):
    m1 = calc.eval1(data, t_name=fw())
    m2 = calc.eval1(data, t_name="3.1.1")
    m3 = calc.eval1(data, t_name="3.1.2")
    m4 = calc.eval1(data, t_name=f'3.1.1{fsH()}')
    m5 = calc.mult_eval(data, t_name="3.1.7") 
    m6 = calc.mult_eval(data, t_name="3.2.0")
    m7 = calc.mult_eval(data, t_name="3.2.9")
    m8 = calc.mult_eval(data, t_name="3.2.11")
    m9 = calc.mult_eval(data, t_name="3.2.14")

    p1 = 1
    p2 = 1
    if type == "mass":
        return m1 + m2 + m3 + m4 + m5 + m6 + m7 + m8 + m9
    elif type == "price":
        return p1 + p2
    else: 
        return 0

































def total_mass():
    m = round(Tub("mass")  + Tailgate("mass") +
        front_sheet("mass") + Fix("mass") + Optionals_mass()
        + bogie_mass()   , 2)
    m_label = tk.Label(root, text= f" {m} lbs")
    m_label.grid(row=8, column=2)

mass_label = tk.Label(root, text= "Trailer Wheight:")
mass_label.grid(row=8, column=1)
Mass_Button = tk.Button(root, text="Calculate", command=total_mass).grid(row=8, column=0)

















def test():
    x1 = calc.mult_eval(data, t_name="4.1.1")
    x2 = ((calc.eval1(data, t_name="4.1.12") * (Fix_axles() + Comp_Lift_axles() + Disc_axles() + Lift_axles())) +
        (calc.eval1(data, t_name="4.1.13") * (Fix_axles() + Comp_Lift_axles() + Disc_axles() + Lift_axles())) +
        (calc.eval1(data, t_name="4.1.19") * (Fix_axles() + Comp_Lift_axles() + Disc_axles())) + 
        (calc.eval1(data, t_name="4.1.20") * (Lift_axles()))
        )
    x3 = (calc.eval1(data, t_name="4.1.14") * (Steer_axles())) + (calc.eval1(data, t_name="4.1.15") * (Steer_axles())) + (calc.eval1(data, t_name="4.1.21") * (Steer_axles())) 
    x4 = calc.mult_eval(data, t_name="4.1.9") if Fix_axles() > 0 else 0
    x5 = calc.mult_eval(data, t_name="4.1.22") if Steer_axles() > 0 else 0
    x6 = calc.mult_eval(data, t_name="4.1.26") if Steer_axles() > 0 else 0
    x7 = x5 if Steer_axles() > 0 else x4
    name1 = x7
    print(calc.Quant(data, t_name="4.1.20"))
    print(name1)
# Create a button to check the state
Test_button = tk.Button(root, text="test", command=test)
Test_button.grid(row=Length_confirm_infogrid[0] + 1, column=Length_confirm_infogrid[1], padx= 20, pady= 120)

root.mainloop()