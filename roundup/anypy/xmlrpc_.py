try:
    # Python 3+.
    from xmlrpc import client, server
    server.SimpleXMLRPCDispatcher
except (ImportError, AttributeError):
    # Python 2.
    import xmlrpclib as client
    import SimpleXMLRPCServer as server
