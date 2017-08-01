import numpy as np
import pymunk
import matplotlib.pyplot as plt


class Pendulum:
    def __init__(self):
        BDIST = 1
        elasticity = 0  # .9999999

        self.space = pymunk.Space()  # Create a Space which contain the simulation
        self.space.gravity = 0, -1  # Set its gravity

        self.base = pymunk.Body(1, 1)
        self.base.position = 0, 0

        shape1 = pymunk.Circle(self.base, 0.1)
        shape1.elasticity = elasticity
        self.space.add(self.base, shape1)
        # put all shapes that should not collide (ie. all shapes here) into the same nonzero shapefilter group
        # why nonzero? if the group is zero they collide...I tried it.
        shape1.filter = pymunk.ShapeFilter(group=1)

        self.middle = pymunk.Body(1, 1)
        self.middle.position = 0, BDIST
        self.middle.velocity = 0.05 * np.random.randn(), 0.05 * np.random.randn()

        shape2 = pymunk.Circle(self.middle, 0.1)
        shape2.elasticity = elasticity
        self.space.add(self.middle, shape2)
        shape2.filter = pymunk.ShapeFilter(group=1)

        self.end = pymunk.Body(1, 1)
        self.end.position = 0, BDIST * 2
        self.end.velocity = 0.05 * np.random.randn(), 0.05 * np.random.randn()

        shape3 = pymunk.Circle(self.end, 0.1)
        shape3.elasticity = elasticity
        self.space.add(self.end, shape3)
        shape3.filter = pymunk.ShapeFilter(group=1)

        pj1 = pymunk.PinJoint(self.base, self.middle, (0, 0), (0, 0))
        pj2 = pymunk.PinJoint(self.middle, self.end, (0, 0), (0, 0))

        sj = pymunk.GrooveJoint(self.space.static_body, self.base, (-5, 0), (5, 0), (0, 0))
        self.space.add(pj1)
        self.space.add(pj2)
        self.space.add(sj)

        # poly = pymunk.Poly.create_box(body) # Create a box shape and attach to body
        # space.add(body, poly)       # Add both body and shape to the simulation

    def step(self, force):
        # pass force (the action) to act on the base's orgin in the x-direction
        self.base.apply_force_at_local_point((force, 0), (0, 0))
        # calculate new state of the pendulum
        self.space.step(0.02)
        return self.state()

    def state(self):
        return np.array([self.base.position[0], self.base.position[1],
                         self.middle.position[0], self.middle.position[1],
                         self.end.position[0], self.end.position[1],
                         self.base.velocity[0], self.base.velocity[1],
                         self.middle.velocity[0], self.middle.velocity[1],
                         self.end.velocity[0], self.end.velocity[1]])

    def plot(self):
        d = self.state()
        plt.plot(d[0], d[1], 'o')
        plt.plot(d[2], d[3], 'o')
        plt.plot(d[4], d[5], 'o')
        plt.plot(d[[0, 2]], d[[1, 3]], 'k')
        plt.plot(d[[2, 4]], d[[3, 5]], 'k')
        plt.axis('equal')
        plt.xlim([-8, 8])
        plt.ylim([-8, 8])
		

