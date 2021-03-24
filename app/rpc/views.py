from modernrpc.core import rpc_method


@rpc_method
def add(a, b):
    return a + b


@rpc_method
def upper(msg):
    return msg.upper()


@rpc_method
def reverse(msg):
    return msg[::-1]
    

@rpc_method
def swap(data):
    return {value:key for key, value in data.items()}
