from matplotlib import pyplot as pl
import numpy
import math

def calculate_gaussian(input_plot, average, standard_deviation):
    if standard_deviation < 10:
        standard_deviation = 10
    
    gaussian = [math.exp(-(((i)-(average*14/255))**2)/(2*((standard_deviation/25)**2))) for i in range(14)]

    return gaussian


def calculate_sp(input_plot, gaussian, weights, bias):
    sp = [(gaussian[i]*((weights/5)*i))+(bias/5) for i in range(14)]    
    

    return sp


def get_output(gaussians, sp_list):   
    b = list(map(sum, [[gaussians[i][j] for i in range(len(gaussians))] for j in range(len(gaussians[0]))]))
    a = list(map(sum, [[sp_list[i][j] for i in range(len(sp_list))] for j in range(len(sp_list[0]))]))

    
    output_plot = [a[i]/b[i] for i in range(int(len(a)))]

    return output_plot


def get_aptitude(individual):
    #individual = [av1,sd1,p1,q1,av2,sd2,p2,q2,....avn,sdn,pn,qn]
    input_plot = [17.53, 16.94, 8.84, 12.13, 22.01, 12.65, 12.67, 23.98, 14.13, 11.76, 10.33, 0, 0, 0]

    sp_list = []
    gaussians = []
    for i in range(int(len(individual)/4)):
        gaussians.append(calculate_gaussian(input_plot, individual[i*4], individual[(i*4)+1])) 


    #pl.plot(gaussians[0], 'green', gaussians[1], 'blue', gaussians[2], 'red', gaussians[3], 'yellow', gaussians[4], 'black')
    #pl.show()

    for gaussian in gaussians:
        sp_list.append(calculate_sp(input_plot, gaussian, individual[(i*4)+2], individual[(i*4)+3]))

    output_plot = get_output(gaussians, sp_list)
    aptitude = 0
    for i in range(len(input_plot)-3):
        aptitude += abs(input_plot[i] - output_plot[i])
    
    return aptitude, output_plot
