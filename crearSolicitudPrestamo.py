import boto3
import json
import uuid
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
solicitud_table = dynamodb.Table('TABLA-SOLICITUD-PRESTAMO')

def lambda_handler(event, context):
    try:
        # Validar el cuerpo de la solicitud
        data = json.loads(event['body'])

        usuario_id = data['usuario_id']
        monto = data['monto']
        descripcion = data.get('descripcion', 'Solicitud de préstamo')

        # Crear la solicitud
        solicitud_id = str(uuid.uuid4())
        item = {
            'usuario_id': usuario_id,
            'solicitud_id': solicitud_id,
            'monto': monto,
            'descripcion': descripcion,
            'estado': 'pendiente',
            'fecha_creacion': datetime.utcnow().isoformat()
        }

        # Guardar en DynamoDB
        solicitud_table.put_item(Item=item)

        return {
            'statusCode': 200,
            'body': {
                'message': 'Solicitud de préstamo creada exitosamente',
                'solicitud': item
            }
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({
                'error': 'Error interno al crear la solicitud',
                'details': str(e)
            })
        }
