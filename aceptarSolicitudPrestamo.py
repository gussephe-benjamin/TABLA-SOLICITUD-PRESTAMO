import boto3
import json

dynamodb = boto3.resource('dynamodb')
solicitud_table = dynamodb.Table('TABLA-SOLICITUD-PRESTAMO')
prestamo_table = dynamodb.Table('TABLA-PRESTAMOS')

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

        # Crear registro en la tabla préstamos
        prestamo_table.put_item(Item={
            'usuario_id': usuario_id,
            'prestamo_id': solicitud_id,
            'monto': solicitud['monto'],
            'descripcion': solicitud['descripcion'],
            'estado': 'activo',
            'fecha_creacion': solicitud['fecha_creacion']
        })

        # Actualizar estado en la solicitud
        solicitud_table.update_item(
            Key={'usuario_id': usuario_id, 'solicitud_id': solicitud_id},
            UpdateExpression='SET estado = :estado',
            ExpressionAttributeValues={':estado': 'aprobado'}
        )

        return {
            'statusCode': 200,
            'body': {'message': 'Solicitud aprobada y préstamo creado'}
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({
                'error': 'Error interno al aprobar la solicitud',
                'details': str(e)
            })
        }
