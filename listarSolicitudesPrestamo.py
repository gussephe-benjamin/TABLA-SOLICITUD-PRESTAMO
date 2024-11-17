import boto3
import json
from decimal import Decimal

# Conexión con DynamoDB
dynamodb = boto3.resource('dynamodb')
solicitud_table = dynamodb.Table('TABLA-SOLICITUD-PRESTAMO')

# Función auxiliar para convertir Decimal a tipos JSON serializables
def decimal_to_serializable(obj):
    if isinstance(obj, Decimal):
        return float(obj) if obj % 1 != 0 else int(obj)
    elif isinstance(obj, list):
        return [decimal_to_serializable(item) for item in obj]
    elif isinstance(obj, dict):
        return {key: decimal_to_serializable(value) for key, value in obj.items()}
    return obj

def lambda_handler(event, context):

    data = json.loads(event['body'])
    cuenta = data['usuario_id']
    
    try:

        response = solicitud_table.query(
            KeyConditionExpression=Key('usuario_id').eq(cuenta)
        )
        
        # Obtener todas las solicitudes
        items = decimal_to_serializable(response.get('Items', []))

        return {
            'statusCode': 200,
            'body': items  # Asegurarse de que sea JSON serializable
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({
                'error': 'Error al listar las solicitudes de préstamo',
                'details': str(e)
            })
        }
