# 🚗 DM-ML-ProjectTask
This web application can detect fraud in accident insurance claims by allowing users to input transaction data through a form. The data is then sent to the server to be processed using a machine learning model to determine whether the transaction is fake or not. The classification results are immediately returned and displayed to the user on the same page.

## Group Member:
- [Mario Valerian Rante Ta'dung - H071221075](https://github.com/riooorante)
- [Jonathan Kwan - H071221067](https://github.com/Jnxx02)
- [Henokh Abhinaya Tjahjadi - H071221045](https://github.com/HenokhIS)
- [Rahmatia - H071221004](https://github.com/rahmatia20april)

## Repository Structure
🚗 DM-ML-ProjectTask
- ├── data
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

3. Install the necessary dependencies:
   
   ```bash
   pip install -r requirements.txt

4. Run the Streamlit application:
   
   ```bash
   streamlit run app.py

5. Open your browser and access `http://localhost:8501` to view the application.
