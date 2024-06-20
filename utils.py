import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import joblib

# Fungsi untuk memuat data dari file CSV
def load_data(filepath):
    return pd.read_csv(filepath)

# Fungsi untuk melakukan preprocessing data
def preprocess_data(df):
    # Lakukan preprocessing sesuai kebutuhan
    df = df.dropna()  # Menghapus baris yang memiliki nilai kosong
    # Sebagai contoh, kita hanya akan menggunakan beberapa fitur sederhana
    features = df[['PolicyNumber', 'RepNumber', 'DriverRating']]  # Memilih fitur yang akan digunakan
    target = df['FraudFound_P']  # Menentukan target prediksi
    return features, target

# Fungsi untuk melatih model
def train_model(features, target):
    # Membagi data menjadi data latih dan data uji
    X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)
    # Membuat model RandomForestClassifier
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    # Melatih model dengan data latih
    model.fit(X_train, y_train)
    # Melakukan prediksi pada data uji
    predictions = model.predict(X_test)
    # Mencetak laporan klasifikasi
    print(classification_report(y_test, predictions))
    # Menyimpan model yang telah dilatih ke dalam file
    joblib.dump(model, 'model/fraud_model.pkl')

# Bagian utama program
if __name__ == "__main__":
    # Memuat data dari file CSV
    data = load_data('data/vehicle_claim.csv')
    # Melakukan preprocessing data
    features, target = preprocess_data(data)
    # Melatih model dengan data yang telah diproses
    train_model(features, target)
