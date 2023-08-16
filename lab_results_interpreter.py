# Full Blood Count

name = input("Enter patient name: ")
age = int(input("Enter patient age: "))

lab_type = "Full Blood Count"

fbc_parameter_names = {
    "WBC": "White Blood Cell Count",
    "RBC": "Red Blood Cell Count",
    "Hb": "Haemoglobin",
    "Hct": "Haematocrit",
    "MCV": "Mean Corpuscular Volume",
    "MCH": "Mean Corpuscular Haemoglobin",
    "MCHC": "Mean Corpuscular Haemoglobin Concentration",
    "RDW": "Red Cell Distribution Width",
    "Plt": "Platelet Count",
    "MPV": "Mean Platelet Volume",
    "PCT": "Plateletcrit",
    "PDW": "Platelet Distribution Width",
    "P-LCR": "Platelet Large Cell Ratio",
}

fbc_parameter_references = {
    "WBC": [4.0, 11.0],
    "RBC": [4.5, 6.5],
    "Hb": [130, 180],
    "Hct": [0.4, 0.54],
    "MCV": [80, 100],
    "MCH": [27.0, 32.0],
    "MCHC": [300, 350],
    "RDW": [11.5, 14.5],
    "Plt": [150, 400],
    "MPV": [7.5, 11.5],
    "PCT": [0.15, 0.35],
    "PDW": [15.0, 17.0],
    "P-LCR": [13.0, 43.0],
}

fbc_values = {}

for parameter in fbc_parameter_names:
    fbc_values[parameter] = float(input(f"Enter {fbc_parameter_names[parameter]}: "))

fbc_status = {}

for parameter in fbc_parameter_names:
    if fbc_values[parameter] < fbc_parameter_references[parameter][0]:
        fbc_status[parameter] = "LOW"
    elif fbc_values[parameter] > fbc_parameter_references[parameter][1]:
        fbc_status[parameter] = "HIGH"
    else:
        fbc_status[parameter] = "NORMAL"

print(f"\n{lab_type} for {name} ({age} years old)")
print("-" * 65)
print("Parameter\tValue\tReference Range\t\tStatus")

for parameter in fbc_parameter_names:
    print(
        f"{parameter}\t\t{fbc_values[parameter]}\t{fbc_parameter_references[parameter][0]} - {fbc_parameter_references[parameter][1]}\t\t{fbc_status[parameter]}"
    )
