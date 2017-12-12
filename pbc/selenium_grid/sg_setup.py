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


    def is_downloaded(self):
        result = self._client.send_command('test -f "selenium-server-standalone-3.8.0.jar" && echo yes')
        if 'yes' in str(result):
            return True


    def download(self):
        if not self.is_downloaded():
            print 'Download'
            self._client.send_command('wget -O selenium-server-standalone-3.8.0.jar https://goo.gl/SVuU9X')


    def start_hub(self):
        print 'Start hub'
        self._client.send_command('java -jar selenium-server-standalone-3.8.0.jar -role hub >> log.txt 2>&1 &')


    def add_node(self):
        print 'Add node'
        self._client.send_command(
        'java -jar selenium-server-standalone-3.8.0.jar -role node  -hub http://localhost:4444/grid/register >> log.txt 2>&1 &')


