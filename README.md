# Annual data calculation - Assignment in flask

## introduction
#### This project will insert an Excel file data into a sqlite database and can access the data from it api.

## Getting Started

### Prerequisites
- Python 
- flask

### Installation

1. Clone the repository:
   ```bash
   https://github.com/Aswanym/inerg-flask.git
   
2. Create virtual environment
   ```bash
      virtualenv venv
   
3. activate virtualenv (windows)
   ```bash
      venv/Scripts/activate
   
4. Install dependencies
   ```bash
      pip install -r requirements.txt
   
5. Configuration
- Create a .env file in the project root. 
- Add the following environment variables to the .env file:

   ```bash
  PATH_TO_EXCEL_FILE=your_excel_file_location
  DB_LOCATION=your_db_loacation_in_local
  
- Replace the placeholder values with your actual values.

6. Running script to load data to db
    ```bash
      python annual_data\db_data_population_script.py
   
7. Running the Server - Start the development server:
   ```bash
   python main.py

8. Visit http://127.0.0.1:8080/data?well=34059242540000 in your browser to view project.

