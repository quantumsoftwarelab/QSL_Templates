from qiskit_ibm_runtime import QiskitRuntimeService, Session, SamplerV2
from qiskit.circuit import QuantumCircuit

from qiskit import QuantumCircuit
from qiskit.transpiler import generate_preset_pass_manager
from dotenv import load_dotenv
import os


# Can change into personal env files
load_dotenv(".env")

# Can change into personal credentials
IBM_API_KEY = os.getenv("IBM_API_TOKEN")
IBM_PRN = os.getenv("IBM_PRN_INSTANCE")


# 1. Initialize service
service = QiskitRuntimeService(
    token=IBM_API_KEY,
    instance=IBM_PRN
)

# 2. Get backend
backend_list = ["ibm_fez", "ibm_marrakesh", "ibm_torino"]
available_backends = service.backends(names=backend_list)
backend = service.least_busy(available_backends, simulator=False, operational=True)

# Your allocated backend
print(f"Using backend: {backend.name}")

# 3. Create circuit
qc = QuantumCircuit(2)
qc.cx(0, 1)
qc.cx(1, 0)
qc.cx(0, 1)
qc.measure_all()


# 4. TRANSPILE with preset_pass_manager (as you requested)
transpiler = generate_preset_pass_manager(backend=backend, optimization_level=3)
transpiled_circuit = transpiler.run(qc)

print(f"Original depth: {qc.depth()}")
print(f"Transpiled depth: {transpiled_circuit.depth()}")


# This could be the better option to handle your sessions.
# with Session(backend=backend) as session:
#     sampler = SamplerV2(session=session)
#     job = sampler.run(pubs=[qc], shots=1024)
#     print(job.result())


# print(result)
sampler = SamplerV2(mode=backend)
job = sampler.run(pubs=[transpiled_circuit], shots=1024)
result = job.result()

