nodemon --exec python onliner.py
.\.venv\Scripts\pyinstaller.exe --noconfirm --onefile --windowed --add-data "D:\Projects\Python\on-liner\.venv\Lib\site-packages\customtkinter;customtkinter/" main.py --name onliner
