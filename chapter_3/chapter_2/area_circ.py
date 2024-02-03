import math
def compute_radius(radius):
    return math.pi*radius**2

if __name__ == "__main__":
    radius = input("enter radius: ")
    print(compute_radius(int(radius)))
