from abc import ABCMeta, abstractmethod


class BaseGrid:
    __metaclass__ = ABCMeta

    @abstractmethod
    def download(self):
        pass

    @abstractmethod
    def start_hub(self):
        pass

    @abstractmethod
    def add_node(self):
        pass


class GridSetup(BaseGrid):
    def __init__(self, ssh_client):
        self._client = ssh_client

    def download(self):
        self._client.send_command('wget -O selenium-server-standalone-3.8.0.jar https://goo.gl/SVuU9X')
        self._client.send_command(
            'wget -O sg-node.json https://gist.github.com/extsoft/aed4cb6e0b1ae3cd1d38cafffdd79310/raw/')

    def start_hub(self):
        print 'Start hub'
        self._client.send_command('rm log.txt')
        self._client.send_command('java -jar selenium-server-standalone-3.8.0.jar -role hub >> log.txt 2>&1 &')

    def add_node(self):
        print 'Add node'
        self._client.send_command(
            'java -jar selenium-server-standalone-3.8.0.jar -role node  -nodeConfig sg-node.json >> log.txt 2>&1 &')

    def get_list_of_files(self):
        return self._client.send_command('ls')
