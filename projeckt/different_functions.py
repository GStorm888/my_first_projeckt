
def get_distance(a, b):
    if a[0]-b[0] < 0: different_x = (a[0]-b[0]) * -1
    else: different_x = (a[0]-b[0])
    if a[1]-b[1] < 0: different_y = (a[1]-b[1]) * -1
    else: different_y = (a[0]-b[0])
    return ((different_x**2)+(different_y**2))**(0.5)
