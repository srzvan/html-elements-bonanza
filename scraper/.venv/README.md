## Activate virtual environment

| Platform | Shell           | Command to activate virtual environment |
| -------- | --------------- | --------------------------------------- |
| POSIX    | bash/zsh        | `$ source .venv/Scripts/activate`       |
|          | fish            | `$ source .venv/Scripts/activate.fish`  |
|          | csh/tcsh        | `$ source .venv/Scripts/activate.csh`   |
|          | PowerShell Core | `$ .venv/Scripts/Activate.ps1`          |
| Windows  | cmd.exe         | `C:\> .venv\Scripts\activate.bat`       |
|          | PowerShell      | `PS C:\> .venv\Scripts\Activate.ps1`    |

## Deactivate virtual environment

`deactivate`

## Install dependencies

`py -m pip install -r scraper/.venv/requirements.txt`

## Run scraper from the virtual environment

`py scraper/.venv/src/scraper.py`
