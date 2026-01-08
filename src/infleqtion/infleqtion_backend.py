"""
# 
#  @Author: Your Name
#  @Date: 08-01-2026
#  @LastUpdate: 08-01-2026
#  @brief: Example module for the infleqtion squale QPU 
#          Documentation can be found here: https://superstaq.readthedocs.io/en/latest/optimizations/sqale/sqale_compile_qss.html
# 
"""
from typing import Any
import qiskit_superstaq as qss
from qiskit import QuantumCircuit


def infleqtion_backend(circuit: QuantumCircuit) -> Any:
        

    num_shots = <NUM_SHOTS>
    description = "dummy run on the squale qpu"
    
    # It is a better idea to use the API key from .env file
    provider = qss.SuperstaqProvider(api_key = "", api_version="v0.3.0")


    sqale_backend = provider.get_backend("sqale_nqcc_qpu")
    
    # Get User Stats (Details like your account details and credits)
    get_user_stats = provider.get_user_info()

    sqale_compile = sqale_backend.compile(circuit)
    sqale_run = sqale_backend.run(circuit , num_shots, description)
    
    counts = sqale_run.result().get_counts()

        
    return counts