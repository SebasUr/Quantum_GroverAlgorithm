import numpy as np
import sys
from typing import Callable
from utils import hadamard_n, create_oracle_matrix, diffusion_operator

# Ejecución del algoritmo de Grover
def grover_algorithm(n: int, f: Callable[[str], int]) -> str:

    N = 2 ** n

    # Contamos cuántos marcados hay, en caso de que haya más de 1 marcado. 
    marked_count = 0
    for i in range(N):
        binary = format(i, f"0{n}b")
        if f(binary) == 1:  
            marked_count += 1

    # Calculamos hadamard_n(n), la matriz oráculo y la matriz de difusión dado los qubits y la función 
    Hn = hadamard_n(n) 
    Uf = create_oracle_matrix(n, f)
    Us = diffusion_operator(n)

    # Inicializamos el estado |0>⊗n
    psi = np.zeros((N, 1), dtype=complex)
    psi[0, 0] = 1

    # Aplicamos Hadamard⊗n a |0>⊗n
    psi = Hn @ psi

    # Número óptimo de iteraciones 
    # https://quantumcomputing.stackexchange.com/questions/1939/in-grovers-algorithm-why-does-the-optimal-number-of-iterations-involve-a-floor
    k = int(np.floor(np.pi / 4 * np.sqrt(N / marked_count)))
        
    print(f"Running Grover for n={n} (N={N}) with k={k} iterations")
    for i in range(1, k + 1):
        psi = Us @ (Uf @ psi)
        probs = np.abs(psi.flatten())**2
        print(f"Iteration {i}: Probabilities = {np.round(probs, 3)}")

    # Escogemos el que tenga mayor probabilidad
    final_probs = np.abs(psi.flatten())**2
    idx = np.argmax(final_probs)
    result = format(idx, f"0{n}b")
    print(f"\nMost probable result: |{result}> with probability {final_probs[idx]:.4f}")
    return result

def run_tests():
    test_cases = [
        ("11", 2),
        ("101", 3),
        ({"101", "010"}, 3),
        ("1010", 4),
        ({"1010", "0101"}, 4),
        ("11111", 5),
        ("000000", 6),
        ({"000000", "111111", "101010"}, 6)
    ]

    for i, (target, n) in enumerate(test_cases, start=1):
        if isinstance(target, str):
            f = lambda x, t=target: 1 if x == t else 0
            marks = [target]
        else:
            f = lambda x, ts=target: 1 if x in ts else 0
            marks = list(target)
        print(f"\n--- Case {i}: {n} qubits - Marked state(s): {marks} ---")
        grover_algorithm(n=n, f=f)

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        run_tests()
    else:
        print("Ejecutando el algoritmo de Grover con una cadena binaria objetivo personalizada. Utilizar test como argumento para pruebas predefinidas.")
        target = input("Ingrese la cadena binaria objetivo para su función oráculo (ej. 1010): ")
        n = len(target)
        def f(x: str) -> int:
            return 1 if x == target else 0
        print(f"\n--- Custom search: {n} qubits - target '{target}' ---")
        grover_algorithm(n=n, f=f)
