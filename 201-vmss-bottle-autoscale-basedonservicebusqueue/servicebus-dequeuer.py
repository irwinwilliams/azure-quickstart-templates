from azure.servicebus import ServiceBusService, Message, Queue
bus_read_service = ServiceBusService(
    service_namespace='vmsseight',
    shared_access_key_name='ListenOneTime',
    shared_access_key_value='OhFgmG5Cr/K9aOrE29YL7eXERzmUb3Fpf7J+FoBhiMw=')
msg = bus_read_service.receive_queue_message('vmsseightqueue', peek_lock=False)
print(msg.body)
