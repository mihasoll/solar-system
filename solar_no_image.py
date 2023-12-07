from solar_main import *
from solar_input import *

physical_time = 0


def execution2():
    global physical_time
    global file
    recalculate_space_objects_positions(space_objects, time_step)
    physical_time += time_step
    write_statistic(space_objects[0], space_objects[1], physical_time, file)


if __name__ == "__main__":
    in_filename = 'one_satellite.txt'
    space_objects = read_space_objects_data_from_file(in_filename)
    time_step = 10
    file = open('stats2.csv', 'w')
    file.write('t,v,r\n')
    for i in range(10000000):
        execution2()
    file.close()