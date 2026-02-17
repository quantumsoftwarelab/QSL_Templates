from qiskit import transpile

# class RuntimeEstimator:
#     def __init__(self, backend, num_circuits, circuit, shots = 500, optimisation_level = 1):
#         """
        
#         Args:
#             backend: IBM backend object.
#             num_circuits: Number of circuits to be executed.
#             circuit: Circuit to be executed.
#             shots: The number of shots. Default is 500.
#             optimisation_level: Transpilation optimization level. Default is 1.
        
#         returns:
#             A dictionary containing the estimated runtime, 
#             repetition delay, circuit length, and number of executions.
        
#         """


#         self.backend              = backend
#         self.num_shots            = shots
#         self.num_circuits         = num_circuits
#         self.circuit              = circuit
#         self.job_overhead_per_job = 2.0
#         self.optimisation_level   = optimisation_level

#     def estimate(self) -> dict:
        
#         qcT = transpile(self.circuit, self.backend, optimization_level = self.optimisation_level)
#         rep_delay = self.backend.default_rep_delay
#         circuit_length = qcT.estimate_duration(target=self.backend.target)
#         num_execution = self.num_circuits * self.num_shots
#         estimated_rt = self.job_overhead_per_job + (rep_delay + circuit_length) * num_execution

#         return {
#             "estimated_runtime": estimated_rt,
#             "repetition_delay": rep_delay,
#             "circuit_length": circuit_length,
#             "num_execution": num_execution
#         }




def estimate_runtime(backend, circuit, num_circuits=1, shots=500, optimisation_level=1):
    
    job_overhead_per_job = 2.0
    qcT = transpile(circuit, backend, optimization_level=optimisation_level)
    rep_delay = backend.default_rep_delay
    circuit_length = qcT.estimate_duration(target=backend.target)
    num_execution = num_circuits * shots
    estimated_rt = job_overhead_per_job + (rep_delay + circuit_length) * num_execution
    
    return {
        "estimated_runtime": estimated_rt,
        "repetition_delay": rep_delay,
        "circuit_length": circuit_length,
        "num_execution": num_execution
    }