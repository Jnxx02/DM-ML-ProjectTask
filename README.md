# DM-ML-ProjectTask
This web application detects fraud in transactions by allowing users to input transaction data through a form. The data is then sent to the server for processing using a machine learning model to determine whether the transaction is fraudulent. The classification result is immediately returned and displayed to the user on the same page.

## Group Member:
- Mario Valerian Rante Ta'dung - H071221075
- Jonathan Kwan - H071221067
- Henokh Abhinaya Tjahjadi - H071221045
- Rahmatia - H071221004

## Repository Structure
DM-ML-ProjectTask
- ├── Data
- │ └── fraud_oracle.csv
- ├── notebook
- │ └── modeling.ipynb
- ├── .gitignore
- ├── README.md
- ├── app.py
- ├── model.pkl
- └── requirements.txt

## How to Run the Streamlit Application
1. Clone this repository to your computer:
   ```bash
   git clone https://github.com/Jnxx02/DM-ML-ProjectTask.git
   cd DM-ML-ProjectTask
2. Create and activate a virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate   # Untuk pengguna macOS/Linux
   .\env\Scripts\activate    # Untuk pengguna Windows
4. Install the necessary dependencies:
   ```bash
   pip install -r requirements.txt
5. Run the Streamlit application:
   ```bash
   streamlit run app.py
6. Open your browser and access `http://localhost:8501` to view the application.
