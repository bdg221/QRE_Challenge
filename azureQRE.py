# Used https://learn.microsoft.com/en-us/azure/quantum/tutorial-resource-estimator-qir and BenchQ azure_estimator.py

import os

from typing import Dict

from azure.quantum import Workspace

from azure.quantum.qiskit import AzureQuantumProvider
from azure.quantum.qiskit.job import AzureQuantumJob
from qiskit import QuantumCircuit


def submit_azure_qre(
    qiskit_circ: QuantumCircuit,
    qubitParams: Dict[str, float] = None,
    errorBudget: Dict[str, float] = None,
):

    workspace = Workspace(
        resource_id=os.getenv("AZURE_RESOURCE_ID"),  # Your resource_id
        location="West US",  # Your workspace location (for example, "westus")
    )

    provider = AzureQuantumProvider(workspace)

    backend = provider.get_backend("microsoft.estimator")

    job = backend.run(qiskit_circ, errorBudget=0.01)

    return job.result()
