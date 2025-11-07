### Sequential method with SciPy.integrate.odeint
import numpy as np
from scipy.integrate import odeint

def skydive(z,t):
    # constants
    g = 9.81 # m/s^2, gravitational constant
    m = 80   # kg, mass of skydiver and pack
    if t<61:
        c = 0.2  # N-s^2/m^2, drag coefficient, chute closed
    else:
        c = 10.0 # N-s^2/m^2, drag coefficient, chute open

    # states (z)
    x = z[0]  # meters, horizontal position 
    y = z[1]  # meters, vertical position / elevation
    vx = z[2] # m/s, skydiver horizontal velocity = airplane velocity
    vy = z[3] # m/s, skydiver vertical velocity

    # derived values
    v = np.sqrt(vx**2+vy**2) # m/s, magnitude of velocity
    Fx = -c * vx**2
    Fy = -m*g + c*vy**2

    # calculate derivatives
    dxdt = vx
    dydt = vy
    dvxdt = Fx / m
    dvydt = Fy / m
    dzdt = [dxdt,dydt,dvxdt,dvydt]    

    return dzdt

# initial conditions
z0 = [0,5000,50,0]
# time points
t = np.linspace(0,90,91)
# solve
z1 = odeint(skydive,z0,t)

# parse results
x = z1[:,0]
y = z1[:,1]
vx = z1[:,2]
vy = z1[:,3]
v = np.sqrt(vx**2+vy**2)

### Plot results
import matplotlib.pyplot as plt

plt.figure()
plt.subplot(2,1,1)
plt.plot(t,x,'r-',lw=2)
plt.plot(t,y,'b-',lw=2)
plt.ylabel('Position (m)')
plt.legend(['x','y'])

plt.subplot(2,1,2)
plt.plot(t,vx,'r-',lw=2)
plt.plot(t,vy,'b-',lw=2)
plt.plot(t,v,'k-',lw=2)
plt.xlabel('Time (sec)')
plt.ylabel('Velocity (m/s)')
plt.legend(['V_x','V_y','V'])

plt.show()
