import paramiko


class Ssh:
    def __init__(self, host, user_name, password):
        print("Connecting to server.")
        self._host = host
        self._user_name = user_name
        self._password = password
        self._client = self.start()

    def start(self):
        try:
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
            client.connect(self._host, username=self._user_name, password=self._password)
            return client
        except Exception as e:
            raise e

    def send_command(self, command):
        stdin, stdout, stderr = self._client.exec_command(command)
        while not stdout.channel.exit_status_ready():
            return stdout.read().splitlines()

    def close(self):
        self._client.close()
        print('Connection closed!')


