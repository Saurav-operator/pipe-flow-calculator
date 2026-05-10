#pipe flow calculator
#Author: me
#Description: Intereactive pipe flow analyser with user inputs
import math 
import matplotlib.pyplot as plt 
import numpy as np
# --fluid sections--
print("===pipe flow calculator===")
print("Select fluid:")
print("1-Water (20 degree)")
print("2-Air (20 degree)")
fluid_choice =input("Enter 1 or2:")
if fluid_choice == "1":
    fluid_name = "Water"
    density = 1000
    viscosity = 0.001
else:
    fluid_name = "Air"
    density = 1.204
    viscosity = 0.0000181
#--user inputs--
diameter= float(input("Enter the pipe diameter(mm):"))/1000  #convert to meters
velocity=float(input("Enter the fluid velocity(m/s):"))
length=float(input("Enter pipe length(m):"))
#--calculations--
#reynolds number
Re=(density*velocity*diameter)/viscosity
#-------flow regime-------
if Re<2300:
    regime="Laminar"
elif Re<4000:
    regime="Transitional"
else:
    regime="Turbulent"
    # Volumetric Flow Rate
area = math.pi * (diameter ** 2) / 4
Q = velocity * area
Q_litres = Q * 1000
    #friction factor (Blasius approximation - valid for turbulent flow)
if Re < 2300:
    f = 64 / Re                        # Laminar exact formula
else:
    f = 0.316 * (Re ** -0.25)         # Blasius equation
# Head Loss (Darcy-Wiesbach)
g=9.81
head_loss = f*(length/diameter)*(velocity**2)/(2*g)  # meters
#Output
print("\n=====Results====")
print(f"fluid    :{fluid_name}")
print(f"pipe diameter    :{diameter*1000:.1f}mm")
print(f"pipe lenghth    :{length} m")
print(f"velocity    :{velocity} m/s")
print(f"flow rate (Q)    :{Q:.6f} m^3/s ({Q_litres:.4f} L/s)")
print(f"Reynolds number:{Re:.0f}")
print(f"flow regime    :{regime}")
print(f"friction factor    :{f:.5f}")
print(f"head loss    :{head_loss:.4f} m")
print("=========")
# --- Save Results to File ---
filename = f"pipe_flow_results_{fluid_name}_{int(diameter*1000)}mm.txt"

with open(filename, "w") as file:
    file.write("=== Pipe Flow Calculator Results ===\n")
    file.write(f"Fluid              : {fluid_name}\n")
    file.write(f"Pipe Diameter      : {diameter*1000:.1f} mm\n")
    file.write(f"Pipe Length        : {length} m\n")
    file.write(f"Velocity           : {velocity} m/s\n")
    file.write(f"Flow Rate (Q)      : {Q:.6f} m³/s  ({Q_litres:.4f} L/s)\n")
    file.write(f"Reynolds Number    : {Re:.0f}\n")
    file.write(f"Flow Regime        : {regime}\n")
    file.write(f"Friction Factor    : {f:.5f}\n")
    file.write(f"Head Loss          : {head_loss:.4f} m\n")

print(f"\nResults saved to: {filename}")
# --- Generate Graph Data ---
velocities = np.linspace(0.1, 5, 100)    # 100 velocity values from 0.1 to 5 m/s
head_losses = []

for v in velocities:
    Re_v = (density * v * diameter) / viscosity
    if Re_v < 2300:
        f_v = 64 / Re_v
    else:
        f_v = 0.316 * (Re_v ** -0.25)
    hl = f_v * (length / diameter) * (v ** 2) / (2 * 9.81)
    head_losses.append(hl)

# --- Plot ---
plt.figure(figsize=(9, 5))
plt.plot(velocities, head_losses, color='steelblue', linewidth=2)
plt.scatter([velocity], [head_loss], color='red', zorder=5, label=f'Your input: v={velocity} m/s')
plt.title(f'Head Loss vs Velocity — {fluid_name} pipe ({diameter*1000:.0f}mm, {length}m long)')
plt.xlabel('Velocity (m/s)')
plt.ylabel('Head Loss (m)')
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.tight_layout()
plt.savefig(f'pipe_flow_graph_{fluid_name}_{int(diameter*1000)}mm.png')
plt.show()
print(f"Graph saved as: pipe_flow_graph_{fluid_name}_{int(diameter*1000)}mm.png")
input("Press Enter to close...")