# Algoritmo de Grover

## Descripción
Este módulo implementa el algoritmo de Grover, un algoritmo cuántico que proporciona una aceleración cuadrática para búsquedas en conjuntos de datos no estructurados. El algoritmo puede encontrar soluciones a problemas de búsqueda con una probabilidad alta en O(√N) operaciones, comparado con los O(N) pasos requeridos por algoritmos clásicos.
El algoritmo implementado soporta múltiples estados marcados y tiene modo de prueba como modo para búsquedas personalizadas (función oráculo)

## Requisitos
- Python 3.x
- NumPy

## Uso

### Modo interactivo
```bash
python grover.py
```
El programa solicitará una cadena binaria objetivo y ejecutará el algoritmo para encontrarla. De modo que se generá la función
```python
    def f(x: str) -> int:
        return 1 if x == target else 0
```

### Modo de prueba
```bash
python grover.py test
```
Ejecuta una serie de casos predefinidos para verificar el funcionamiento del algoritmo.

## Detalles de implementación
El algoritmo sigue estos pasos:
1. Inicializa el estado cuántico a |0⟩⊗ⁿ
2. Aplica la transformada de Hadamard para crear superposición
3. Calcula el número óptimo de iteraciones de Grover
4. En cada iteración:
   - Aplica el oráculo (Uf) que marca los estados solución
   - Aplica el operador de difusión (Us) que amplifica las amplitudes
5. Mide el estado resultante, obteniendo la solución con alta probabilidad

## Ejemplo
```python
# Definir una función oráculo que marque el estado "101"
def f(x):
    return 1 if x == "101" else 0

# Ejecutar el algoritmo con 3 qubits
resultado = grover_algorithm(n=3, f=f)
```

## Referencias
- [Quantum Computing Stack Exchange](https://quantumcomputing.stackexchange.com/questions/1939/in-grovers-algorithm-why-does-the-optimal-number-of-iterations-involve-a-floor)
- [Groover's Algorithm](https://en.wikipedia.org/wiki/Grover%27s_algorithm)