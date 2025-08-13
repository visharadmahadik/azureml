from azure.ai.ml import MLClient, load_job
from azure.identity import DefaultAzureCredential
from azure.ai.ml.entities import RecurrenceTrigger, JobSchedule

try:
    # Connect to Azure ML workspace
    ml_client = MLClient(
        DefaultAzureCredential(),
        subscription_id="",
        resource_group_name="",
        workspace_name=""
    )

    # Load pipeline job definition from YAML file
    create_job = load_job("deploy.yml")

    # Define daily recurrence trigger
    trigger = RecurrenceTrigger(
        frequency="Day",
        interval=1,
        start_time="2025-08-07T00:00:00",
        time_zone="UTC"
    )

    # Define the schedule
    job_schedule = JobSchedule(
        name="daily-retraining-job",
        trigger=trigger,
        create_job=create_job
    )

    # Create the schedule
    print("Starting scheduling job...")
    ml_client.schedules.begin_create_or_update(job_schedule)
    print("Schedule created successfully.")

except Exception as e:
    print(f"Error occurred: {e}")
