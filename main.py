
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation
import random
import math
# Fixing random state for reproducibility
##colors
colors = np.array([
    (31, 119, 180), (174, 199, 232), (255, 127, 14), (255, 187, 120),
    (44, 160, 44), (152, 223, 138), (214, 39, 40), (255, 152, 150),
    (148, 103, 189), (197, 176, 213), (140, 86, 75), (196, 156, 148),
    (227, 119, 194), (247, 182, 210), (127, 127, 127), (199, 199, 199),
    (188, 189, 34), (219, 219, 141), (23, 190, 207), (158, 218, 229),

    (31, 119, 180), (174, 199, 232), (255, 127, 14), (255, 187, 120),
    (44, 160, 44), (152, 223, 138), (214, 39, 40), (255, 152, 150),
    (148, 103, 189), (197, 176, 213), (140, 86, 75), (196, 156, 148),
    (227, 119, 194), (247, 182, 210), (127, 127, 127), (199, 199, 199),
    (188, 189, 34), (219, 219, 141), (23, 190, 207), (158, 218, 229),

    (31, 119, 180), (174, 199, 232), (255, 127, 14), (255, 187, 120),
    (44, 160, 44), (152, 223, 138), (214, 39, 40), (255, 152, 150),
    (148, 103, 189), (197, 176, 213), (140, 86, 75), (196, 156, 148),
    (227, 119, 194), (247, 182, 210), (127, 127, 127), (199, 199, 199),
    (188, 189, 34), (219, 219, 141), (23, 190, 207), (158, 218, 229),

    (31, 119, 180), (174, 199, 232), (255, 127, 14), (255, 187, 120),
    (44, 160, 44), (152, 223, 138), (214, 39, 40), (255, 152, 150),
    (148, 103, 189), (197, 176, 213), (140, 86, 75), (196, 156, 148),
    (227, 119, 194), (247, 182, 210), (127, 127, 127), (199, 199, 199),
    (188, 189, 34), (219, 219, 141), (23, 190, 207), (158, 218, 229)

]) / 255.

####Problem Definition####

def func(particle): #rastring
    X=particle.position[0]
    Y=particle.position[1]
    return (X**2 - 10 * np.cos(2 * np.pi * X)) + (Y**2 - 10 * np.cos(2 * np.pi * Y)) + 20


dimensions = 3
lowerBound = -5.12
upperBound = 5.12

####PSO Parameters####

maxNumberOfIterations = 1000
swarmSize = 3
w = 2  #współczynnik bezwładności, określa wpływ prędkości w poprzednim kroku
wdamp = 0.99
c1 = 3  #współczynnik dążenia do najlepszego lokalnego rozwiązania
c2 = 2  # współczynnik dążenia do najlepszego globalnego rozwiązania

maxVelocity = (upperBound -lowerBound) * 0.2
minVelocity = maxVelocity * -1
velocityMultiplier = 1

####Particle####

class Particle:
    def __init__(self):
        self.position = []
        self.velocity = []
        self.personalBest = []
        self.color = colors[random.randint(0,50)]
        for i in range(3):
            self.velocity.append(random.uniform(-1, 1))
            self.position.append(random.uniform(lowerBound,upperBound))
            self.personalBest.append(self.position[i])
        self.position[2] = func(self) # z value
        self.personalBest.append(self.position[2])
        self.cost = func(self)  # measuerment/costvalue
        self.bestCost = self.cost

    def update_velocity(self):
        for i in range(3):
            r1 = random.random()
            r2 = random.random()

            global_comp = c1 * r1 * (self.personalBest[i] - self.position[i])
            social_comp = c2 * r2 * (globalBestPosition[i] - self.position[i])
            self.velocity[i] = (w * self.velocity[i] + global_comp + social_comp)
            if self.velocity[i] > maxVelocity:
                self.velocity[i] = maxVelocity
            if self.velocity[i] < minVelocity:
                self.velocity[i] = minVelocity


    def updatePosition(self):
        for i in range(2):
            self.position[i] = self.position[i] + self.velocity[i] * velocityMultiplier
            if self.position[i] > upperBound:
                self.position[i] = upperBound
            if self.position[i] < lowerBound:
                self.position[i] = lowerBound
        self.position[2] = func(self)


############################################################Rastring
X = np.linspace(-5.12, 5.12, 100)
Y = np.linspace(-5.12, 5.12, 100)
X, Y = np.meshgrid(X, Y)

tridimentionalfunction = (X**2 - 10 * np.cos(2 * np.pi * X)) + \
  (Y**2 - 10 * np.cos(2 * np.pi * Y)) + 20

Z = tridimentionalfunction

##############################################################
def mainPSO():
    global globalBestCost, w, tempParticle,globalBestPosition
    a = 0
    ##Initialization of population
    population = []
    globalBestCost = 9999999999999999999  #this values are overwritten below
    globalBestPosition = [0,0,0] # this values are overwritten below
    bestCostsOfEachIteration = []
    tempParticle = Particle()
    population.append(tempParticle)
    for i in range(3): ##init of first particle in population
        globalBestPosition[i] = tempParticle.position[i]
    globalBestCost = tempParticle.cost

    for i in range(swarmSize-1): ## init of rest of population
        tempParticle = Particle()
        population.append(tempParticle)
        if tempParticle.bestCost < globalBestCost:
            globalBestCost = tempParticle.bestCost
            for j in range(3):
                globalBestPosition[j] = tempParticle.position[j]

    ##end of initialization
    # Attaching 3D axis to the figure
    fig = plt.figure()
    ax = fig.add_subplot(projection="3d")
    for i in range(maxNumberOfIterations):

        for particle in population:
            a = a + 1 if a < 50 else 0
            ax.plot(particle.position[0], particle.position[1], particle.position[2],
             color = particle.color, marker='o')
            particle.update_velocity()
            particle.updatePosition()
            particle.cost = func(particle)
            ax.set_xlim3d([-5.12, 5.12])
            ax.set_ylim3d([-5.12, 5.12])
            ax.set_zlim3d([0, 80])
            if particle.cost < particle.bestCost: #localcost
                particle.bestCost = particle.cost
                if particle.bestCost < globalBestCost: #globalcost
                    globalBestCost = particle.bestCost
                    bestCostsOfEachIteration.append(globalBestCost)
                    for j in range(3):
                        globalBestPosition[j] = tempParticle.position[j] #globalpostition
                for k in range(3):
                    particle.personalBest[k] = particle.position[k] #local position
            print(particle.position[0], particle.position[1], particle.position[2])
            plt.suptitle("Global best cost:")
            plt.title(globalBestCost)
        print(f'GLOBAL BEST:',globalBestCost)
        plt.pause(0.05)
        w = w *wdamp
        ax.clear()
        ax.plot_wireframe(X, Y, Z, alpha=0.1)




