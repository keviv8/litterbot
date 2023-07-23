from network.communication import Communication

comm = Communication('http://45.137.126.83:5000')
data = {
    'litterbot_id': '1',
    'status': 'active',
    # ...
}
response = comm.send_data('data', data)
print(response)