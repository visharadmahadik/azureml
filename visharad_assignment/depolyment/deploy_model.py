from azure.ai.ml import MLClient
from azure.identity import DefaultAzureCredential
from azure.ai.ml.entities import ManagedOnlineEndpoint, ManagedOnlineDeployment, Model

ml_client = MLClient(DefaultAzureCredential(), "sub-id", "rg", "workspace")

model = ml_client.models.get(name="train_model", version="1")

endpoint = ManagedOnlineEndpoint(name="iris-endpoint", auth_mode="key")
ml_client.online_endpoints.begin_create_or_update(endpoint)

deployment = ManagedOnlineDeployment(
    name="iris-deploy",
    endpoint_name=endpoint.name,
    model=model,
    instance_type="Standard_DS2_v2",
    instance_count=1
)

ml_client.online_deployments.begin_create_or_update(deployment)
ml_client.online_endpoints.begin_start(endpoint.name)
