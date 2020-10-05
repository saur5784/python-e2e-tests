# E2E tests for REST APIs #

### Env Setup
- Follow instructions to setup python3 and pip from
[this link](https://docs.python-guide.org/starting/install3/osx/)
- Install pytest using: `pip install pytest` or `pip3 install pytest` (depending on your pip install) 
- Download the project zip file and unzip it 

### Executing tests
```
cd <project_root_directory>
pytest [-s]
```
### Project structure
- root
    - tests
        - integration/routes/test_*.py
        - integration/utils
    - README
    
This project contains integration tests and utility for testing the Joke factory routes.
Following tests are executed in this project: 
- Route : https://official-joke-api.appspot.com/jokes/programming/random
    - Test : Validate that the returned Joke is of type "programming"
- Route : https://official-joke-api.appspot.com/jokes/programming/ten
    - Test : Validate that 10 jokes are returned
    - Test : Validate that all jokes are of type "programming"
