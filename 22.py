fractal = [3]
fractal.append(fractal)
fractal.append(2)
print(fractal)

def fractal_print(frac):
    print(frac[:])
    
fractal_print(fractal)