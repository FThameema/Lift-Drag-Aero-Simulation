# Lift and Drag Calculator.
def calculate_lift(rho, velocity, area, cl):
    return 0.5 * rho * velocity**2 * area * cl

def calculate_drag(rho, velocity, area, cd):
    return 0.5 * rho * velocity**2 * area * cd

if _name_ == "_main_":
    rho = 1.225  # Air density (kg/m^3)
    velocity = 50  # Velocity in m/s
    area = 2.0  # Wing area in m^2
    cl = 1.2  # Lift coefficient
    cd = 0.3  # Drag coefficient

    lift = calculate_lift(rho, velocity, area, cl)
    drag = calculate_drag(rho, velocity, area, cd)

    print(f"Lift Force: {lift:.2f} N")
    print(f"Drag Force: {drag:.2f} N")
