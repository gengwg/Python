class Connection:
    '''
    A simple connection class that uses the State Design Pattern
    to manage its state.
    '''
    # The current state of the connection
    def new_state(self, newstate):
        self.state = newstate

    # Initialize the connection in a closed state
    def __init__(self):
        self.new_state(ClosedConnectionState)

    # Delegate to the state class
    def read(self):
        self.state.read(self)

    def write(self, data):
        self.state.write(self, data)

    def open(self):
        self.state.open(self)

    def close(self):
        self.state.close(self)

# Connection state base class
class ConnectionState:
    @staticmethod
    def read(conn):
        raise NotImplementedError("This method should be overridden in subclasses")
    @staticmethod
    def write(conn, data):
        raise NotImplementedError("This method should be overridden in subclasses")
    @staticmethod
    def open(conn):
        raise NotImplementedError("This method should be overridden in subclasses")
    @staticmethod
    def close(conn):
        raise NotImplementedError("This method should be overridden in subclasses")
    

# Implementation of the different states
class ClosedConnectionState(ConnectionState):
    @staticmethod
    def read(conn):
        print("Cannot read from a closed connection")

    @staticmethod
    def write(conn, data):
        print("Cannot write to a closed connection")

    @staticmethod
    def open(conn):
        print("Opening connection")
        conn.new_state(OpenConnectionState)

    @staticmethod
    def close(conn):
        print("Connection is already closed")

class OpenConnectionState(ConnectionState):
    @staticmethod
    def read(conn):
        print("Reading data from the connection")

    @staticmethod
    def write(conn, data):
        print(f"Writing data to the connection: {data}")

    @staticmethod
    def open(conn):
        print("Connection is already open")

    @staticmethod
    def close(conn):
        print("Closing connection")
        conn.new_state(ClosedConnectionState)

if __name__ == "__main__":
    c = Connection()
    print(c.state) # Should print ClosedConnectionState
    c.read()  # Should print "Cannot read from a closed connection"
    c.write("Hello")  # Should print "Cannot write to a closed connection"
    c.open()  # Should print "Opening connection"
    print(c.state)  # Should print OpenConnectionState
    c.read()  # Should print "Reading data from the connection"
    c.write("Hello")  # Should print "Writing data to the connection: Hello"
    c.read()  # Should print "Reading data from the connection"
    c.close()  # Should print "Closing connection"
    print(c.state)  # Should print ClosedConnectionState