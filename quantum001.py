from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator


qc = QuantumCircuit(2)
qc.h(0)     
qc.cx(0, 1)  
qc.measure_all()


sim = AerSimulator()


print("Running simulation...")
job = sim.run(qc)
result = job.result()
counts = result.get_counts()


print("\n--- RESULTS ---")
print(f"Quantum Outcomes: {counts}")
print("----------------\n")


print("Circuit Diagram:")
print(qc.draw())
