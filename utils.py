import numpy as np
from typing import Callable

# Creamos la matriz Kronecker A⊗B
def kronecker(A: np.ndarray, B: np.ndarray) -> np.ndarray:
    m, n = A.shape
    p, q = B.shape

    result = np.zeros((m * p, n * q), dtype=complex)

    for i in range(m):
        for j in range(n):
            result[i * p:(i + 1) * p, j * q:(j + 1) * q] = A[i, j] * B

    return result

# Creamos la matriz Hadamard H^n = H⊗H⊗...⊗H (n qubits)
def hadamard_n(n: int) -> np.ndarray:
    H = np.array([[1, 1], [1, -1]], dtype=complex) / np.sqrt(2)
    Hn = H
    for _ in range(n - 1):
        Hn = kronecker(Hn, H)

    return Hn

# Creamos la matriz Oráculo U_f = I - 2|x> para las x tal que f(x)=1. (n qubits, f funcion oracle, )
def create_oracle_matrix(n: int, f: Callable[[str], int]) -> np.ndarray:
    N = 2 ** n
    Uf = np.eye(N, dtype=complex)

    for x in range(N):
        x_bin = format(x, f"0{n}b")
        if f(x_bin) == 1:
            Uf[x, x] = -1

    return Uf

# Creamos la matriz de difusión U_s = 2|s><s| - I, donde |s> es el estado uniforme. (n qubits)
def diffusion_operator(n: int) -> np.ndarray:
    N = 2 ** n
    s = np.ones((N, 1), dtype=complex) / np.sqrt(N)
    return 2 * (s @ s.T) - np.eye(N, dtype=complex)