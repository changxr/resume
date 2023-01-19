# Flask - Labs

This repository covers exercises in Flask labs.

Click on the relevant tag to access a snapshot of the state of the Blog project at a particular point of the lab tasks completion.

## Contents:

| Lab |      Functionality                | Git Tag |
|------|---------------------------|---------|
| 1.1 | Basic "Hello World!" page | [part 1.1](https://git.cardiff.ac.uk/scmne/flask-labs/-/tree/part_1.1) |
| 1.2 | Basic templating, routes, navigation and styling | [part 1.2](https://git.cardiff.ac.uk/scmne/flask-labs/-/tree/part_1.2) |
| 1.3 | Reorganising the project for Blogging Website | [part 1.3](https://git.cardiff.ac.uk/scmne/flask-labs/-/tree/part_1.3) |
| 2.1 | Blogging Website: database implementation, dynamic home page| [part 2.1](https://git.cardiff.ac.uk/scmne/flask-labs/-/tree/part_2.1) |
| 2.2 | Blogging Website: individual post pages| [part 2.2](https://git.cardiff.ac.uk/scmne/flask-labs/-/tree/part_2.2) |
| 3.1 | Blogging Website: user accounts | [part 3.1](https://git.cardiff.ac.uk/scmne/flask-labs/-/tree/part_3.1) |
| 3.2 | Blogging Website: validation | [part 3.2](https://git.cardiff.ac.uk/scmne/flask-labs/-/tree/part_3.2) |
| 4.0 | Blogging Website: deployment on OpenShift | [part 4.0](https://git.cardiff.ac.uk/scmne/flask-labs/-/tree/part_4.0) |

## Initial Project Setup Required:

- activation of virtual environment (see the lab instructions)
- installation of the necessary project dependencies

### Project Dependencies:

* to install a particular library:
```
pip install <LIBRARY>
```
&nbsp;&nbsp;&nbsp; e.g.: ```  pip install flask  ```

* to install all dependencies recursively from ```requirements.txt``` file:
```sh
pip install -r requirements.txt
```

* to see all installed dependencies in the console:
```console
pip freeze
```

* to save the project dependencies in ```requirements.txt``` file:

```console
pip freeze > requirements.txt
```
