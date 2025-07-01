from lift_drag_calculator import calculate_lift, calculate_drag

# Sample inputs
rho = 1.225           # air density in kg/m^3
velocity = 50         # in m/s
area = 10             # wing area in m^2
cl = 0.5              # coefficient of lift
cd = 0.02             # coefficient of drag

# Calculate lift and drag
lift = calculate_lift(rho, velocity, area, cl)
drag = calculate_drag(rho, velocity, area, cd)

# Print the results
print(f"Lift Force = {lift:.2f} N")
print(f"Drag Force = {drag:.2f} N")
