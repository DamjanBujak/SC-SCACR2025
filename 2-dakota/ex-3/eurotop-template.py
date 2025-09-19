# EurOtop (steep slopes) mean overtopping discharge
# q / (sqrt(g*Hm0^3)) = 0.09 * exp(-(1.5*Rc/(Hm0*γf*γβ))**1.3)

import math

def overtopping_q(Hm0, Rc, gamma_f=0.5, gamma_beta=1.0, g=9.81):
    """Return mean overtopping discharge q [m^3 s^-1 m^-1]."""
    X = 1.5 * Rc / (Hm0 * gamma_f * gamma_beta)
    return 0.09 * math.sqrt(g * (Hm0**3)) * math.exp(-(X**1.3))

# --- Example ---
Hm0 = {hm0}                  # sig. wave height [m]
Rc = {rc}                    # freeboard [m]
gamma_f = {gamma_f}          # roughness factor
gamma_beta = {gamma_beta}    # obliquity factor
g = 9.81                     # [m s^-2]

q = overtopping_q(Hm0, Rc, gamma_f, gamma_beta, g)

print(q)
