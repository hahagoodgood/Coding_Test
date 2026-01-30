tri_list = [-1, -1, -1]  # Initialize with dummy values

while tri_list != [0, 0, 0]:
    # Read and sort three sides (largest becomes the hypotenuse)
    tri_list = sorted(map(int, input().split()))   
    if tri_list == [0, 0, 0]:
        break   
    # Check if it is a right triangle using the Pythagorean theorem.
    a, b, c = tri_list
    if a**2 + b**2 == c**2:
        print("right")
    else:
        print("wrong")