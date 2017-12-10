import paramiko
import pytest
from time import sleep

@pytest.fixture(scope="session", autouse=True)
def setup_selenium():
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    client.connect('192.168.33.10', username='vagrant', password='vagrant')
    print("starting selenium setup")
    # download
    client.exec_command('wget -O selenium-server-standalone-3.8.0.jar https://goo.gl/SVuU9X')
    sleep(10)
    # run hub
    client.exec_command('java -jar selenium-server-standalone-3.8.0.jar -role hub >> log.txt 2>&1 &')
    # run node
    client.exec_command(
    'java -jar selenium-server-standalone-3.8.0.jar -role node -hub http://localhost:4444/grid/register >> log.txt 2>&1 &')
    print("selenium is deployed")
    stdin, stdout, stderr = client.exec_command('pgrep java')
    sleep(2)
    processes = []
    for row in stdout:
        print('... ' + row.strip('\n'))
        processes.append(row)
    print('running processes: {}'.format(processes))
    yield processes
    # clean up
    client.exec_command('killall java')  # kill processes
    client.close()
    print('Connection closed!')





# lectures = 'https://gist.github.com/extsoft/ea63fd7fc47db8110a333d4939f53f02#commom'
#
# docs = 'https://docs.google.com/spreadsheets/d/1U-Qgh5lAmrp7nqsWZirypvw_h90qPVla4V0sJRPBW-I/edit#gid=0'
#
# run_numbers_from_app = 'python app.py -a number -l 5 6 7 8 9 4'
# run_fib_from_app = 'python app.py -a fib -n 5'
