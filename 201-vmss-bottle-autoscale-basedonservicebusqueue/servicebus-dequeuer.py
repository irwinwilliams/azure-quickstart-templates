from azure.servicebus import ServiceBusService, Message, Queue
bus_read_service = ServiceBusService(
    service_namespace='<enter sb namespace>',
    shared_access_key_name='<enter name of sb shared access key>',
    shared_access_key_value='<enter value for sb shared access key>')
msg = bus_read_service.receive_queue_message('<enter name of sb queue>', peek_lock=False)
print(msg.body)
