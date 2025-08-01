import socket
message_to_send = input("Enter the message to send: ")


#Open port to send the message to server
#Open Listener port to receive the response

import argparse

def main():
    parser = argparse.ArgumentParser(description="Start server with host and port")

    # Add --host_ip argument
    parser.add_argument(
        "--host_ip",              # argument name
        required=True,            # must be provided by the user
        help="IP address of the host"  # description shown in help/usage
    )

    # Add --port argument
    parser.add_argument(
        "--port",                 # argument name
        required=True,            # must be provided
        type=int,                 # convert to integer
        help="Port number to use"
    )

    # Parse the arguments from command line
    args = parser.parse_args()

    # Access the arguments
    host_ip = args.host_ip
    port = args.port

    print(f"Starting server on {host_ip}:{port}")

if __name__ == "__main__":
    main()

