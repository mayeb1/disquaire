#################------------README------------#################


STEP 1:
we need python version 3.10 or above

For Linux
sudo apt install build-essential
sudo apt-get install python3-dev

STEP 2:

Before to start the program, you have to setup all packages in requirements.txt

You can use the program whithout wxPython, however there will not be graphics interface

STEP 3:

main.py file lunch the program:

you can add argument like (-a,--p,-d,-g, -m)

-a allow you to add in the console movies

-d when you want to debug

--p path to the text file for order

-g graphics mode

-m this is an addictionnal mode, all the saga cost 15 euros (not only Back to the Future)

Example:

python3.10 main.py -a : lunch programm in the console and add movie in the console

python3.10 main.py -a -p path_to_file: lunch programm in the console, add movie to the list of movie already added from text file

python3.10 main.py -g : lunch graphic programm, you can drag and drom text files  (work only in Windows) and add movie in text field

You can't do:

python3.10 main.py -g -a -p path_to_file: because you have to choose the graphics or console mode, (-a and -p) are for console mode

If you want to try drag and drop order file, you can find text file named test.txt in unit_test


---------------------------Unit Test--------------------------

If you want test if functions are ok, there are unit test for each function in unit_test folder

python3.10 -m unittest .\unit_test\test_orderPrice.py

python3.10 -m unittest .\unit_test\test_slice_base_title.py

python3.10 -m unittest .\unit_test\test_text_to_list.py
