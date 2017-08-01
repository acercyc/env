import numpy as np
import matplotlib.pyplot as plt
from env_ForceField import env_ForceField

# ---------------------------------------------------------------------------- #
#                              create environment                              #
# ---------------------------------------------------------------------------- #
env = env_ForceField.ForceField()

# ---------------------------------------------------------------------------- #
#                      Define positions and force of stars                     #
# ---------------------------------------------------------------------------- #
# env.attractors = npa([[70, 70, -200],
#                       [60, 60, -300],
#                       [75, 58, -300],
#                       [20, 25, 1000]])

# ---------------------------------------------------------------------------- #
#                             Define initial state                             #
# ---------------------------------------------------------------------------- #
# env.state = npa([50, 70, 0, 0])


state_history = []
plt.ion()
f = plt.figure(figsize=(5, 5))
for iStep in range(1000):
    # --------------------------  get the current state -------------------------- #
    state_history.append(env.state)

    # ----------------------------------- plot ----------------------------------- #
    plt.cla()

    # plot visited places with colored visiting time
    env.plot_coverage_freq(np.vstack(state_history)[:, 0:2], nBin=(21, 21))

    # plot agent position and stars
    env.plot()

    # compute coverage rate from history
    s = 'Coverage Rate = {:.2%}'.format(env.cal_coverageRate(np.vstack(state_history)[:, 0:2]))
    plt.text(0.05, 0.95, s)

    plt.title(iStep)
    f.canvas.draw()
    plt.pause(0.01)

    # ------------------------------ perform action ------------------------------ #
    action = np.random.uniform(-1, 1, 2)
    env.step(action)
