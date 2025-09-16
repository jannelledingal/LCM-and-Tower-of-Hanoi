def gcd(a, b):
  
    if b == 0:
        return a
    return gcd(b, a % b)

def lcm(a, b):
    return abs(a * b) // gcd(a, b)


while True:
    x = int(input("Enter a value for x: "))
    y = int(input("Enter a value for y: "))
    if x > 0 and y > 0:
        break
    else:
        print("Please enter positive non-zero integers only.")

print(f"The LCM of {x} and {y} is = {lcm(x, y)}")
