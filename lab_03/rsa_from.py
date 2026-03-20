import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.rsa import Ui_MainWindow
import requests


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # connect buttons (đúng tên theo file UI của bạn)
        self.ui.btnGenerate.clicked.connect(self.call_api_gen_keys)
        self.ui.btnEncrypt.clicked.connect(self.call_api_encrypt)
        self.ui.btnDecrypt.clicked.connect(self.call_api_decrypt)
        self.ui.btnSign.clicked.connect(self.call_api_sign)
        self.ui.btnVerify.clicked.connect(self.call_api_verify)

    # ==============================
    # GENERATE KEYS
    # ==============================
    def call_api_gen_keys(self):
        url = "http://127.0.0.1:5000/api/rsa/generate_keys"
        try:
            response = requests.get(url)
            data = response.json()

            if response.status_code == 200:
                QMessageBox.information(self, "Info", data["message"])
            else:
                QMessageBox.warning(self, "Error", data.get("error", "Error"))

        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    # ==============================
    # ENCRYPT
    # ==============================
    def call_api_encrypt(self):
        url = "http://127.0.0.1:5000/api/rsa/encrypt"

        payload = {
            "message": self.ui.txtPlain.toPlainText(),
            "key_type": "public"
        }

        try:
            response = requests.post(url, json=payload)
            data = response.json()

            if response.status_code == 200:
                self.ui.txtCipher.setText(data["encrypted_message"])
                QMessageBox.information(self, "Info", "Encrypted Successfully")
            else:
                QMessageBox.warning(self, "Error", data.get("error", "Error"))

        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    # ==============================
    # DECRYPT
    # ==============================
    def call_api_decrypt(self):
        url = "http://127.0.0.1:5000/api/rsa/decrypt"

        payload = {
            "ciphertext": self.ui.txtCipher.toPlainText(),
            "key_type": "private"
        }

        try:
            response = requests.post(url, json=payload)
            data = response.json()

            if response.status_code == 200:
                self.ui.txtPlain.setText(data["decrypted_message"])
                QMessageBox.information(self, "Info", "Decrypted Successfully")
            else:
                QMessageBox.warning(self, "Error", data.get("error", "Error"))

        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    # ==============================
    # SIGN
    # ==============================
    def call_api_sign(self):
        url = "http://127.0.0.1:5000/api/rsa/sign"

        payload = {
            "message": self.ui.txtInfo.toPlainText()
        }

        try:
            response = requests.post(url, json=payload)
            data = response.json()

            if response.status_code == 200:
                self.ui.txtSign.setText(data["signature"])
                QMessageBox.information(self, "Info", "Signed Successfully")
            else:
                QMessageBox.warning(self, "Error", data.get("error", "Error"))

        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    # ==============================
    # VERIFY
    # ==============================
    def call_api_verify(self):
        url = "http://127.0.0.1:5000/api/rsa/verify"

        payload = {
            "message": self.ui.txtInfo.toPlainText(),
            "signature": self.ui.txtSign.toPlainText()
        }

        try:
            response = requests.post(url, json=payload)
            data = response.json()

            if response.status_code == 200:
                if data["is_verified"]:
                    QMessageBox.information(self, "Info", "Verified Successfully")
                else:
                    QMessageBox.warning(self, "Info", "Verify Failed")
            else:
                QMessageBox.warning(self, "Error", data.get("error", "Error"))

        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))


# ==============================
# MAIN
# ==============================
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())