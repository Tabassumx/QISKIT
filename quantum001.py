from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

# 1. Create the Quantum Circuit (2 qubits)
qc = QuantumCircuit(2)
qc.h(0)      # Superposition gate
qc.cx(0, 1)  # Entanglement gate
qc.measure_all()

# 2. Setup the Simulator
sim = AerSimulator()

# 3. Run the simulation and get results
print("Running simulation...")
job = sim.run(qc)
result = job.result()
counts = result.get_counts()

# 4. Show the data
print("\n--- RESULTS ---")
print(f"Quantum Outcomes: {counts}")
print("----------------\n")

# 5. Draw the circuit in the terminal
print("Circuit Diagram:")
print(qc.draw())