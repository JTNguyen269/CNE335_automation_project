# This is the template code for the CNE335 Final Project
# John Nguyen
# CNE 335 Winter

from Server import Server


def print_program_info():
    print("Server Automator v0.1 by John Nguyen")


if __name__ == '__main__':
    print_program_info()
    my_server = Server("54.149.41.254", r"C:\Users\johnn\OneDrive\Desktop\Jtnguyen_Key.pem")
    if my_server.ping():
        my_server.run_a_command("sudo apt update && sudo apt -y upgrade")
