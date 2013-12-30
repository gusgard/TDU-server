import threading
import SocketServer
from vehiculo import Vehiculo

class ThreadedTCPRequestHandler(SocketServer.BaseRequestHandler):

    def handle(self):
        data = self.request.recv(1024)
        cur_thread = threading.current_thread()
        response = "{}: {}".format(cur_thread.name, data)
        #print "Recibi ", self.client_address
        vehiculo = Vehiculo()
        print "Recibi ", data
        #vehiculo.deserializar(data)
        vehiculo.deserializar(data)
        print "Deserializado", vehiculo
        self.request.sendall(response)

#proceso forking.
#class ThreadedTCPServer(SocketServer.ForkingMixIn, SocketServer.TCPServer):
class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    pass


if __name__ == "__main__":
    # Port 0 means to select an arbitrary unused port
    HOST, PORT = "awseb-e-q-AWSEBLoa-U0TZFW27RVH5-1541299131.us-west-2.elb.amazonaws.com", 9997

    server = ThreadedTCPServer((HOST, PORT), ThreadedTCPRequestHandler)
    #ip, port = server.server_address

    # Start a thread with the server -- that thread will then start one
    # more thread for each request
    server_thread = threading.Thread(target=server.serve_forever)
    # Exit the server thread when the main thread terminates
    server_thread.daemon = True
    server_thread.start()
    print "Server loop running in thread:", server_thread.name

    #server.shutdown()

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()
