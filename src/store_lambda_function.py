import json
import boto3
import uuid
from botocore.exceptions import ClientError

def lambda_handler(event, context):
    # Initialize the S3 client
    s3 = boto3.client('s3')
    bucket_name = 'ssapp-secrets'  # Adjust this as needed

    try:
        # Parse the JSON body from the event
        if 'body' not in event or not event['body']:
            raise ValueError("Missing or empty 'body' in the request")
        
        body = json.loads(event['body'])

        # Check if 'data' key is in the body for operations
        if 'data' not in body:
            raise KeyError("Missing key 'data' in the JSON payload")

        operation = body.get('operation', 'store')  # Default to 'store' if not specified

        if operation == 'store':
            # Generate a unique key for this secret
            secret_key = str(uuid.uuid4())
            secret_data = json.dumps(body['data'])  # Ensure the data is in JSON format

            # Store the secret in the S3 bucket
            s3.put_object(Bucket=bucket_name, Key=secret_key, Body=secret_data)

            # Optionally generate a pre-signed URL for accessing the secret
            presigned_url = s3.generate_presigned_url('get_object',
                                                      Params={'Bucket': bucket_name, 'Key': secret_key},
                                                      ExpiresIn=3600)  # Link expires in 1 hour

            return {
                'statusCode': 200,
                'headers': {"Access-Control-Allow-Origin":"*"},
                'body': json.dumps({'url': presigned_url})
            }

        elif operation == 'retrieve':
            object_key = body.get('key')
            if not object_key:
                raise KeyError("Missing key 'key' required for retrieve operation")

            # Fetch the object from S3
            response = s3.get_object(Bucket=bucket_name, Key=object_key)
            secret_data = response['Body'].read().decode('utf-8')

            return {
                'statusCode': 200,
                'body': json.dumps({'data': secret_data}),
                'headers': {'Content-Type': 'application/json'}
            }

    except ValueError as e:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': str(e)})
        }
    except KeyError as e:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': f"Missing key in request: {str(e)}"})
        }
    except json.JSONDecodeError:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'Invalid JSON format'})
        }
    except ClientError as e:
        # Handle specific AWS client errors
        error_code = e.response['Error']['Code']
        return {
            'statusCode': 500,
            'body': json.dumps({'error': f"S3 Error: {error_code}"})
        }
    except Exception as e:
        # Handle other unexpected errors
        return {
            'statusCode': 500,
            'body': json.dumps({'error': f"Internal Server Error: {str(e)}"})
        }

