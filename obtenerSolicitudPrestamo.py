import boto3
import json

dynamodb = boto3.resource('dynamodb')
solicitud_table = dynamodb.Table('TABLA-SOLICITUD-PRESTAMO')

def lambda_handler(event, context):
    try:
        data = json.loads(event['body'])
        usuario_id = data['usuario_id']
        solicitud_id = data['solicitud_id']

        # Obtener la solicitud
        solicitud = solicitud_table.get_item(Key={'usuario_id': usuario_id, 'solicitud_id': solicitud_id}).get('Item')

        if not solicitud:
            return {
                'statusCode': 404,
                'body': json.dumps({'error': 'Solicitud no encontrada'})
            }

        return {
            'statusCode': 200,
            'body': solicitud
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({
                'error': 'Error interno al obtener la solicitud',
                'details': str(e)
            })
        }
