import json
import boto3

def lambda_handler(event, context):
    """AWS Lambda function to invoke SageMaker endpoint."""
    runtime = boto3.client('runtime.sagemaker')
    endpoint_name = "your-endpoint-name"

    # Assuming 'event' is a JSON payload you send to the Lambda function
    response = runtime.invoke_endpoint(EndpointName=endpoint_name,
                                       ContentType='application/json',
                                       Body=json.dumps(event))
    
    result = json.loads(response['Body'].read().decode())
    return result
