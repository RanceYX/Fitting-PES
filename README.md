# -
V1.0:
This code is used to get Van der Waals potential coefficients (C6)

Workflow:
1. Read the numerical potential energy surface(PES) from a csv file.
2. Expand PES with Legendre polynomial(V_l(R)) with doing an integral(Simpson's rule)
3. Fitting each V_l to get C6 by function 'polyfit' from numpy
4. Extrapolate PES at long distance with C6 coefficients to reconstruct the PES
5. Write the new PES into a csv file.

