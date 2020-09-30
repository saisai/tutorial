import os

import tqdm

from socketserver import BaseRequestHandler, TCPServer

class EchoHandler(BaseRequestHandler):

    # receivve 4096 bytes each time
    BUFFER_SIZE = 4096

    SEPARATOR = "<SEPARATOR>"

    def handle(self):
        print("Gog connection from", self.client_address)
        #while True:
            
        received = self.request.recv(self.BUFFER_SIZE).decode()
        
        #if not received:
            #break
        filename, filesize = received.split(self.SEPARATOR)

        # remove absolute path if there is
        filename = os.path.basename(filename)

        # covert to integer
        filesize = int(filesize)

        # start receiving the file from the socket
        # and writing to the file stream
        progress = tqdm.tqdm(range(filesize), f"Receing {filename}", unit="B", unit_scale=True, unit_divisor=1024)

        with open(filename, "wb") as f:
            for _ in progress:
                # read 1024 bytes from the socket (receive)
                bytes_read = self.request.recv(self.BUFFER_SIZE)
                if not bytes_read:
                    # nothing is received
                    # file transmitting is done
                    break
                # write to the file the bytes we just received
                f.write(bytes_read)
                # update the progress bar
                progress.update(len(bytes_read))
                
        # close the client socket
        self.request.close()
        # close the server socket
        #s.close()
        
        #print(len(msg))
        #if not msg:
            #break
        #self.request.send(str(received)s)

if __name__ == "__main__":
    serv = TCPServer(("0.0.0.0", 20000), EchoHandler)
    print("Echo server running on port 20000")
    serv.serve_forever()
