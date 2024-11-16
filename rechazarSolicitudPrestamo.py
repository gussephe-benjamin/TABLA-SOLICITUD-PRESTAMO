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

        if solicitud['estado'] != 'pendiente':
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'La solicitud ya fue revisada'})
            }

        # Actualizar estado en la solicitud
        solicitud_table.update_item(
            Key={'usuario_id': usuario_id, 'solicitud_id': solicitud_id},
            UpdateExpression='SET estado = :estado',
            ExpressionAttributeValues={':estado': 'rechazado'}
        )

        return {
            'statusCode': 200,
            'body': {'message': 'Solicitud rechazada'}
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({
                'error': 'Error interno al rechazar la solicitud',
                'details': str(e)
            })
        }
