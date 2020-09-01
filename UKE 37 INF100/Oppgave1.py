a = input("Tall 1")

b = input("Tall 2")

egen_max = (int(a) + int(b) + abs(int(a)-int(b)))//2

egen_min = (int(a) + int(b) - abs(int(a)-int(b)))//2

print("egen_max = " + str(egen_max))
maximum = max(int(a),int(b))
print("max = " + str(maximum))

print("egen_min = " + str(egen_min))


minimum = min(int(a),int(b))
print("min = " + str(minimum))