ChatExport
ChatExport is a desktop application built with PyQt6 for converting JSON-based chat logs into HTML, Markdown, or PDF formats. It provides a user-friendly interface to import, view, and export chat messages, with a SQLite database to store messages, channels, attachments, and export logs. The application is ideal for archiving and analyzing chat data from platforms like Discord or similar messaging systems.
Features

Import and Preview: Load JSON files or folders containing chat logs and preview their content.
Export Options: Convert chat logs to HTML, Markdown, or PDF with formatted output preserving author, timestamp, and attachments.
Database Storage: Store messages, channels, attachments, and export logs in a SQLite database, tracking metadata like machine ID and IP address.
Search Functionality: Query stored messages and view results in a tabular format.
Export Logging: Track export operations with details like timestamp, file path, and export type.
Cross-Platform: Runs on Windows, macOS, and Linux (with appropriate dependencies).

Prerequisites
To run ChatExport, ensure you have the following installed:

Python 3.8 or higher: Download from python.org.
pip: Python package manager (included with Python).
A compatible operating system (Windows, macOS, or Linux).

Installation
Follow these steps to set up the project:
1. Clone the Repository
Clone the repository to your local machine using Git:
git clone https://github.com/renejr/package.git
cd package

Replace your-username with your GitHub username or the correct repository URL.
2. Create a Virtual Environment (Recommended)
Set up a virtual environment to manage dependencies:
python -m venv venv

Activate the virtual environment:

Windows:
venv\Scripts\activate


macOS/Linux:
source venv/bin/activate



3. Install Dependencies
Install the required Python libraries using pip. The project depends on the following packages:

PyQt6: For the graphical user interface.
reportlab: For generating PDF files.
Other standard libraries (sqlite3, os, json, shutil, uuid, socket, datetime) are included with Python.

Run the following command to install the dependencies:
pip install PyQt6 reportlab

Alternatively, if you have a requirements.txt file, use:
pip install -r requirements.txt

To create a requirements.txt file, you can generate it with:
pip freeze > requirements.txt

Example requirements.txt content:
PyQt6==6.7.0
reportlab==4.2.2

4. Database Setup
ChatExport uses a SQLite database (chat_export.db) to store chat data and export logs. The database is automatically created when you run the application for the first time, but you can manually initialize it by running the database.py script.
Steps to Initialize the Database

Ensure you are in the project directory with the virtual environment activated.

Run the following Python code to create the database and tables:
from database import Database
db = Database()

This will create a file named chat_export.db in the project directory with the following tables:

channels: Stores channel information (id, channel_id, name, description).
messages: Stores message details (id, channel_id, author, timestamp, content, machine_id, ip).
attachments: Stores attachment URLs linked to messages (id, message_id, url).
import_log: Tracks export operations (id, import_time, machine_id, ip, file_path, export_type).



Database Notes

The database file is created in the same directory as database.py.
A unique machine ID is generated and stored in a .machine_id file in the project directory.
The local IP address is automatically detected (falls back to 127.0.0.1 if detection fails).
No manual SQL commands are required; the Database class handles table creation and data insertion.

Running the Application
To start the application, run the main.py script:
python main.py

This will launch the ChatExport GUI with two tabs: Conversão (Conversion) and Consulta (Query).
Application Usage
Conversion Tab

Select File or Folder:

Click "Selecionar Pasta ou Arquivo" to choose a JSON file or a folder containing JSON files.
Supported JSON files must contain chat log data (e.g., messages with author, timestamp, content, and optional attachments).
If a folder is selected, all .json files in the folder are listed.


Preview Content:

Click a file in the list to display its raw JSON content in the text area.
The content is loaded and parsed for conversion.


Convert and Export:

Click one of the conversion buttons: "Converter para HTML", "Converter para Markdown", or "Converter para PDF".
Choose a destination folder for the exported files.
The application creates a subfolder named after the source folder and saves:
The converted file (.html, .md, or .pdf).
A copy of the original JSON file with an _EXTRAIDO suffix.


Messages are saved to the SQLite database, and the export is logged.



Query Tab

Search Messages:

Enter a search term in the "Pesquisar" field and click "Buscar".
(Note: Search functionality is not fully implemented in the provided code and requires additional development.)


View Export Log:

The "Log de Exportação" table displays recent export operations, including timestamp, machine ID, IP, file path, and export type.
The log is updated automatically after each export.


Exit:

Click "Sair" to close the application.



Project Structure
Here’s an overview of the key files in the repository:

main.py: Entry point; initializes the PyQt6 application and handles user interactions.
ui_mainwindow.py: Defines the GUI layout using PyQt6 widgets (tabs, buttons, tables, etc.).
database.py: Manages the SQLite database, including table creation, message storage, and export logging.
converter.py: Contains functions to convert JSON data to HTML, Markdown, or PDF formats.
chat_export.db: SQLite database file (created automatically).
.machine_id: Stores the unique machine ID (created automatically).

Troubleshooting

Error: "No module named PyQt6":

Ensure PyQt6 is installed (pip install PyQt6).
Verify the virtual environment is activated.


Error: "No module named reportlab":

Install reportlab (pip install reportlab).


Database not created:

Check write permissions in the project directory.
Run database.py manually to initialize the database (see "Database Setup").


JSON file not loading:

Ensure the JSON file is valid and contains expected fields (e.g., author, timestamp, content).
Check the file encoding (must be UTF-8).


PDF export fails:

Verify reportlab is installed and the destination folder is writable.
Ensure sufficient disk space.



Contributing
Contributions are welcome! To contribute:

Fork the repository.
Create a new branch (git checkout -b feature/your-feature).
Make your changes and commit (git commit -m "Add your feature").
Push to the branch (git push origin feature/your-feature).
Open a Pull Request.

Please include tests and update documentation as needed.
License
This project is licensed under the MIT License. See the LICENSE file for details.
Contact
For questions or support, open an issue on the GitHub repository or contact the maintainer at your-email@example.com.

Built with ❤️ by [Rene Ballesteros Machado Junior - MDXHQ]
