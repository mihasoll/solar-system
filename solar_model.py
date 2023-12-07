def calculate_force(body, space_objects):
    g = 6.67408E-11

    body.Fx = 0
    body.Fy = 0
    for someb in space_objects:
        if someb != body:
            body.Fx += g * someb.m * body.m * (someb.x - body.x) / ((someb.y - body.y) ** 2 + (someb.x - body.x) ** 2) ** (3 / 2)
            body.Fy += g * someb.m * body.m * (someb.y - body.y) / ((someb.y - body.y) ** 2 + (someb.x - body.x) ** 2) ** (3 / 2)



def move_space_object(body, dt):
    #dt = 1000 * dt
    body.x += body.Vx * dt
    body.y += body.Vy * dt
    body.Vx += body.Fx * dt / body.m
    body.Vy += body.Fy * dt / body.m


def recalculate_space_objects_positions(space_objects, dt):
    for someb in space_objects:
        calculate_force(someb, space_objects)
    for someb in space_objects:
        move_space_object(someb, dt)