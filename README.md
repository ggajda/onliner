pipenv shell
nodemon --exec python onliner.py
pyinstaller --noconfirm --onefile --windowed --add-data "C:\Users\GG\.virtualenvs\on-liner-57tgxGno\Lib\site-packages\customtkinter;customtkinter/" "onliner.py"
