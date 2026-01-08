"""

#  @Date: 22-12-2025
#  @LastUpdate: 08-01-2026
#  @brief: Dummy IBM Qiskit Runtime job example to show how to 
#          create a noise model from a real device and run it.

"""

from qiskit import QuantumCircuit
from qiskit.transpiler import generate_preset_pass_manager
from qiskit_aer.noise import NoiseModel
from qiskit_aer.primitives import SamplerV2
from qiskit_ibm_runtime import QiskitRuntimeService
from dotenv import load_dotenv
import os


# Can change into personal env files
load_dotenv(".env")

# Can change into personal credentials
IBM_API_KEY = os.getenv("IBM_API_TOKEN")
IBM_PRN = os.getenv("IBM_PRN_INSTANCE")


# API_TOKEN = "<YOUR_IBM_API_TOKEN"

# INSTANCE = "<YOUR_IBM_INSTANCE_NAME_OR_CRN>"

QiskitRuntimeService.save_account(
    token=IBM_API_KEY, # Use the API_KEY you created and saved from the IBM Quantum Platform Home dashboard
    instance=IBM_PRN, # Optional
    overwrite=True 
)


# Create the service
service = QiskitRuntimeService(channel="ibm_quantum_platform", token=IBM_API_KEY, instance=IBM_PRN)

# Can change any specific backend that you have access to.
# For example "kingston"

available_backends = service.backends(names=["ibm_fez", "ibm_marrakesh", "ibm_torino"])
backend = service.least_busy(available_backends)

print("\n")
print("---------------- Backend ---------------\n")
print(f"Backend: {backend}\n")
print(f"---------------------------------------\n")


target = backend.target

# Get the noise model from the sepcific backend.
noise_model = NoiseModel.from_backend(backend)


print(noise_model)

# Specific circuit
qc = QuantumCircuit(2, 2)
qc.h(0)
qc.cx(0, 1)
qc.measure_all()


# Transpile
# Optimisation levels https://quantum.cloud.ibm.com/docs/en/guides/set-optimization
transpiler = generate_preset_pass_manager(target=target, optimization_level=1)

# Transpiled circuit and then run the citcuit
isa_circ = transpiler.run(qc)



# qiskit_aer SamplerV2 passes backend options to AerSimulator - this is whats under the hood.
# GenericBackend either uses BasicSimulator or AerSimulator so no need for it.

# Sampiling with the specific noise model
sampler = SamplerV2(options=dict(backend_options=dict(noise_model=noise_model)))


# Submitting the job for local simulations
job = sampler.run(pubs=[isa_circ], shots=1024)

# Get the results
result = job.result()


print(result)