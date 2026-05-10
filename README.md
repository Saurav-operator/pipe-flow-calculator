# 🔧 Pipe Flow Calculator

Programme written in Python for analysing fluid flow in pipes, during Year 1 Mechanical Engineering at University of East London.

The tool uses the fundamental theory of fluid mechanics such as Reynolds number, Blasius equation and Darcy-Weisbach formula to determine important flow properties for any pipe configuration.

---

## 📊 Example Output

The graph shown is a plot of head loss against velocity for water in a pipe.The following is a graph that plots head loss against velocity for water flowing in a pipe.

---

## ⚙️ What It Calculates

| Output | Formula Used |
|---|---|
| Volumetric Flow Rate (Q) | Q = v × A |
| Reynolds Number (Re) | Re = ρvD / μ |
Flow Regime: Laminar / Transitional / Turbulent |
Friction Factor (f) = 64/Re (Laminar) or Blasius equation (Turbulent) |
Head Loss (hf) | Darcy-Weisbach equation |

---

## 🧪 Fluids Supported

- Water (20°C) — density: 1000 kg/m³, viscosity: 0.001 Pa·s
- Air (20°C) — density: 1.204 kg/m³, viscosity: 0.0000181 Pa·s

---

## 🚀 How to Run

**Requirements:**
- Python 3.x
- matplotlib
- numpy

**Install dependencies:**
```
pip install matplotlib numpy
```

**Run the script:**
```
python pipe_flow.py
```

You will be asked to type:
- Temperature of the fluid (Low, medium, or high)
- Pipe diameter (mm)
- Fluid velocity (m/s)
- Pipe length (m)

---

## 📁 Output Files

All runs are automatically saved:
A resulting file, in the format `.txt`, containing all the calculated values.
- A .png graph of head loss vs velocity in which your input is circled in red.

---

## 📐 Example Calculation

**Inputs:**
- Fluid: Water
- Diameter: 75 mm
- Velocity: 2.5 m/s
- Length: 250 m

**Results:**
```
Fluid              : Water
Pipe Diameter      : 75.0 mm
Pipe Length        : 250.0 m
Velocity           : 2.5 m/s
Flow Rate (Q)      : 0.011045 m³/s  (11.0447 L/s)
Reynolds Number    : 187500
Flow Regime        : Turbulent
Friction Factor    : 0.01519
Head Loss          : 16.1249 m
```

---

## 🎓 Academic Context

This project was developed independently whilst studying BEng Mechanical Engineering at the University of East London in Year 1 and was based upon theory learnt in the module titled Fluid Mechanics (EG4020) and this included the following:

- Bernoulli's principle
The Reynolds number is used to classify the flow regime.Flow regime classification is done by using Reynolds number.
These are the approximations given by the Moody chart using the Blasius equation.
A Darcy-Weisbach head loss equation.Darcy-Weisbach head loss equation.

---

## 👤 Author

Saurav is a Mechanical Engineer from the University of East London and has a degree in BEng Mechanical Engineering.  
[GitHub](https://github.com/Saurav-operator)