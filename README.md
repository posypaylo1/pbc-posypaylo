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

**Added marks:**

- "pairs" - for test_num_pairs.py (be in your root project folder and execute: pytest -v -m pairs)
- "numbers" - for test_fib.py (pytest -v -m numbers)
          
**Added CLI config for:**

'fibonacci.py' - be in unit_tests package, execute: python fibonacci.py -n "The required amount of sequence items"

'numbers_pairs.py' - be in unit_tests package, execute: python numbers_pairs.py -l "amount of items in list"

**Added decorator for:**

- Printing out tested inputs in fib function

- Printing out tested inputs in number_pairs function