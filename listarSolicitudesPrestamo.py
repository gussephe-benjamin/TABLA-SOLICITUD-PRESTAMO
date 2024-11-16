import boto3
import json

dynamodb = boto3.resource('dynamodb')
solicitud_table = dynamodb.Table('TABLA-SOLICITUD-PRESTAMO')

def lambda_handler(event, context):
    try:
        # Obtener todas las solicitudes
        response = solicitud_table.scan()

        return {
            'statusCode': 200,
            'body': response.get('Items', [])   
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({
                'error': 'Error al listar las solicitudes de préstamo',
                'details': str(e)
            })
        }
