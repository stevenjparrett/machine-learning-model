import sagemaker
from sagemaker.tensorflow import TensorFlowModel

def deploy_model(model_artifacts_path, execution_role):
    """Deploys the model to AWS SageMaker."""
    sagemaker_session = sagemaker.Session()
    model = TensorFlowModel(model_data=model_artifacts_path,
                            role=execution_role,
                            framework_version='2.3.0',
                            sagemaker_session=sagemaker_session)
    predictor = model.deploy(initial_instance_count=1, instance_type='ml.m5.large')
    return predictor
