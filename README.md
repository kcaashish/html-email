# html-email

### Project 

    .
    ├── data                  # keep the csv files here
    ├── references            # reference html and css (not required for this proejct CAN REMOVE)
    ├── site                  # generated / rendered html will be placed here 
    ├── templates             # the used html template is placed here
    ├── data.json             # will get generated while running email-maker.py
    ├── email-maker.py        # main file, only need to change the address / name of csv and run
    ├── requirements.txt
    └── README.md

### Setup virtual environment ".venv"

- For Linux:
  ```sh
  $ python -m venv .venv
  $ source .venv/bin/activate
  ```
- For Windows:
  Go to the folder, then open Git Bash, then:
  ```sh
  $ python -m venv .venv
  $ source .venv\Scripts\activate.bat
  ```

### Installing requirements in .venv

```sh
$ pip install -r requirements.txt
```

### How to run

After activating .venv and installing from the requirements, 
add the path to new csv file in email-maker.py and run.
```py
if __name__ == "__main__":
    # add the path to the CSV file as argument
    email_maker('data/09172021_complete_data.csv')  #<--place new file in data/, change name and run
```
