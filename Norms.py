import numpy as np

def l1_norm(x):
    """Computes the L1 norm of a vector x"""
    return np.sum(np.abs(x))

def l2_norm(x):
    """Computes the L2 norm (Euclidean norm) of a vector x"""
    return np.sqrt(np.sum(x**2))

def linf_norm(x):
    """Computes the L-infinity norm (maximum norm) of a vector x"""
    return np.max(np.abs(x))

# Example usage
x = np.array([1, 2, 3])
print(f"L1 norm of x: {l1_norm(x)}")
print(f"L2 norm of x: {l2_norm(x)}")
print(f"L-infinity norm of x: {linf_norm(x)}")

'''
This code defines three functions: l1_norm, l2_norm, and linf_norm, which respectively compute the L1 norm, L2 norm (also known as the Euclidean norm), and L-infinity norm (also known as the maximum norm) of a given vector x. To use these functions, you can simply call them with a numpy array as the input.

For example, if you have a vector x that you want to compute the L1 norm of, you can call l1_norm(x). Similarly, you can call l2_norm(x) to compute the L2 norm of x, and linf_norm(x) to compute the L-infinity norm of x.
'''