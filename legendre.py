#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
plt.style.use( 'publication.sty' )

N = 100
x = np.linspace( -1.0, 1.0, N )

y0 = np.ones( N, np.float64 )
y1 = x
y2 = 0.5 * ( 3 * x**2 - 1 )
y3 = 0.5 * ( 5 * x**3 - 3 * x )
y4 = 0.125 * ( 35 * x**4 - 30 * x**2 + 3 )
y5 = 0.125 * ( 63 * x**5 - 70 * x**3 + 15 * x )

fig, ax = plt.subplots( 1, 1 )
ax.plot( x, y0, label = r'$P_{0}$' )
ax.plot( x, y1, label = r'$P_{1}$' )
ax.plot( x, y2, label = r'$P_{2}$' )
ax.plot( x, y3, label = r'$P_{3}$' )
ax.plot( x, y4, label = r'$P_{4}$' )
ax.plot( x, y5, label = r'$P_{5}$' )

ax.grid()

ax.legend()
ax.set_xlabel( r'$\cos\theta$' )

#plt.show()
plt.savefig( 'legendre.png', dpi = 300 )
