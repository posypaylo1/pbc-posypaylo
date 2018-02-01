# pbc-posypaylo
*python boot camp*

## [Day 1](https://gist.github.com/extsoft/bf1b9884cbaccf1eb2efd0330ae542c7)

## Vagrant setup
Deploy VM with Vagrant, configure IP address and name. 
  - `vagrant init ubuntu/trusty64` creates Vargantfile with desired Ubuntu
  - `vagrant up` deploys a VM using VirtualBox
  - `ssh vagrant@192.168.33.10` allows to login (pass is `vagrant`)
  
**New functions:**
- 'fibonacci.py' consist of function which returns desired count of fibonacci numbers
- 'numbers_pairs.py' consist of function which returns unique pairs of numbers which sum is = 10 for a given collection of numbers


## [Day 2](https://gist.github.com/extsoft/6aab6d4a3d143f40029233015508eab1)

**Additional vagrant setup**

Update VM:
```
vagrant destroy
vagrant up --provision
```

**Setup virtual env. Bash script**

To set up virtual environment execute setup_env.sh 

**Unit tests**

- 'unit_tests/test_fib.py' - tests for function "fib" from fibonacci.py (check quantity of numbers,
 output type; float, sting , zero inputs)
- 'unit_tests/test_num_pairs.py' - tests for func "number_pairs" from numbers_pairs.py (check for expected sequence)


## [Day 3](https://gist.github.com/extsoft/f9963e86d9162604fe2d012b0653d7d0)

**Restructurize project**

- Modules fibonacci.py and numbers_pairs.py were moved to main package(my_tested_app)

- Unit tests were parametrized

- For now on "number_pairs" function accepts unlimited numbers 

**Added marks:**

- "pairs" - for test_num_pairs.py (be in your root project folder and execute: pytest -v -m pairs)
- "numbers" - for test_fib.py (pytest -v -m numbers)
          
**Added CLI config for:**

'fibonacci.py' - be in unit_tests package, execute: python fibonacci.py -n "The required amount of sequence items"

'numbers_pairs.py' - be in unit_tests package, execute: python numbers_pairs.py -l "Enter sequence of numbers, use 'space' as divider"

**Added decorator for:**

- Printing out tested inputs in fib function

- Printing out tested inputs in number_pairs function


## [Day 5](https://gist.github.com/extsoft/479fe1c0b2422a991980fee920159724)

**Added fixture:**

- installs Selenium grid on Vagrant box using Python, pytest and paramiko before running tests.
 To check run: pytest -s -v test


## [Day 6](https://gist.github.com/extsoft/0a7861abc8459e180c26106a0e4238f0)

**Added  Ssh class:**

- start() - starts ssh connection using paramiko

- send_command() - executes provided command and returns result

- close() - closes connection

**Added  GridSetup class:**

- is_downloaded() - checks whether downloaded selenium server

- download() - downloads selenium server if server wasn't downloaded

- start_hub() - runs hub

- add_node() - adds node

**Added selenium_precondition fixture:**

- Prepares standalone server for tests(executes methods from GridSetup class)

- Returns connection

- Do precondition (Kills all java processes and closes connection)

**Added test for:**

- Check necessary running java processes on server

- Check errors in log.txt


## [Day 7](https://gist.github.com/extsoft/350299f8342207451073e35103cbe6b7)

**Updated vagrant config:**

- Added installation of firefox + geckodriver on VM
 

**Edited selenium grid configuration:**

-  selenium server reads configuration from sg-node.json


**Added test for:**

- Checks that grid enables expected amount of sessions


## [Day 8](https://gist.github.com/extsoft/0ebe6bfb63e77a6070775abeff53ccd2)

**Added tests:**

- rest test - checks running nodes

- remote ui test