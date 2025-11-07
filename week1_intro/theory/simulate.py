from apm import *  # load APMonitor.com toolkit
z = apm_solve('ferrari',7) # solve

# plot results
import matplotlib.pyplot as plt
plt.figure()

plt.subplot(211)
plt.plot(z['time'],z['p'],'r-')
plt.legend(['Pedal'])
plt.ylabel('Position (%)')

plt.subplot(212)
plt.plot(z['time'],z['v'],'b.-')
plt.legend(['Velocity'])
plt.ylabel('Velocity (m/s)')
plt.xlabel('Time (sec)')
plt.show()
