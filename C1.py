import sympy as sp

#Edit units and fexpr to fit whatever problem you are working on

def newton_raphson_auto(func, var, x0, tol=1e-5, max_iter=100):
    #Compute derivative 
    f_dx = sp.diff(func, var)
    
    #Convert sp function to numerical
    f = sp.lambdify(var, func, "math")
    df = sp.lambdify(var, f_dx, "math")
    
    x = x0
    steps = [x0]
    
    for i in range(max_iter):
        fx = f(x)
        dfx = df(x)
        
        x_1 = x - fx / dfx
        steps.append(x_1)
        
        if abs(x_1 - x) < tol:
            return x_1, steps
        x = x_1
    raise ValueError("Newton-Raphson method did not converge within max iterations.")

x = sp.symbols('x')
print("\n\tComputation Question 1:\n")
#Input units for your solution
units = "radians"
func = x - (5281.716/5280)*sp.sin(x)
root, steps = newton_raphson_auto(func, x, x0=1.0)
print(f"Root approximation: {root:.8f}", units)

print("\nTheta(Radians)\t\tR(m)\t\t\td(m)")
for i in range(0,len(steps)):
    r = 5280/(2*sp.sin(steps[i]))
    ex = sp.sqrt(r**2 - (5280/2)**2)
    d = r - ex
    print(f"{steps[i]: .8f} \t {r: .8f} \t {d: .8f} ")

print("\n\tQuestion 1.22:\n")
#Input units for your solution
units = "in"
func = x**4 - 16*x**3 + 1.44*x**2 + 1024*x - 4096
root, steps = newton_raphson_auto(func, x, x0=1.0)
print(f"Root approximation: {root:.8f}", units)