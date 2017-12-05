# pbc
*python boot camp*

**Lesson1**

## Vagrant setup
Deploy VM with Vagrant, configure IP address and name. 
  - `vagrant init ubuntu/trusty64` creates Vargantfile with desired Ubuntu
  - `vagrant up` deploys a VM using VirtualBox
  - `ssh vagrant@192.168.33.10` allows to login (pass is `vagrant`)
  
**New functions:**
- 'fibonacci.py' consist of function which returns desired count of fibonacci numbers
- 'numbers_pairs.py' consist of function which returns pairs of numbers which sum is = 10 for a given collection of numbers


##Lesson2
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