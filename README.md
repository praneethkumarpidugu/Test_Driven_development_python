#Test Driven Development with Python

#TODO
-[x] Getting Django Set Up Using a Functional Test
-[x] Extending out Functional Test using the unittest Module
-[x] Testing a Simple Homepage with Unit Tests

#procedure to run the tests

First and foremost activate the virtualenvironment as follows:
```shell
cd /home/Test_Driven_development_python
```
```shell
source venv/bin/activate
```

Initially start the development server
```shell
python manage.py runserver
```
run the tests with Django Build test library where we are doing unit test case which decides how our business login should respond
```shell
python manage.py test
```

Run the functional test cases with selenium test automation tool as follows:

```shell
cd /home/Test_Driven_development_python
```

```shell
python functionaltests.py
```
#After you finish the Test cases please deactivate the virtualenvironment for a safe closing of file system directories which has your environment setup.

```shell
deactivate
```
#Installation Packages tools
Python*
git*
django
selenium
apium- automation tool (shrathank requirement)
selenium- Functional tests, 

Note:- normal unix- sudo apt-get install selenium
          (shrathank)-windows- pip already installed
                   pip3 install --upgrade selenium

```shell
pip3 install django==1.8
```

```shell
pip3 install --upgrade selenium
```
