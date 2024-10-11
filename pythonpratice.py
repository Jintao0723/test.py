import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the heart shape using a parametric equation
t = np.linspace(0, 2 * np.pi, 1000)
x = 16 * np.sin(t)**3
y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)

# Create figure and axis
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xlim([-20, 20])
ax.set_ylim([-20, 20])

# Plot the heart shape
heart, = ax.plot([], [], color='red', lw=2)

# Update function for animation (heartbeat effect)
def update(frame):
    scale = 1 + 0.05 * np.sin(frame * 0.3)  # Control the beat with a sine wave
    heart.set_data(scale * x, scale * y)  # Adjust the size of the heart
    return heart,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=np.linspace(0, 2 * np.pi, 60), interval=50, blit=True)

# Show the animation
plt.show()
