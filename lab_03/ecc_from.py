import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.ecc import Ui_MainWindow
import requests


class ECCApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # connect buttons (phải đúng objectName trong .ui)
        self.ui.btnGenerate.clicked.connect(self.call_api_generate)
        self.ui.btnSign.clicked.connect(self.call_api_sign)
        self.ui.btnVerify.clicked.connect(self.call_api_verify)

    # =========================
    # GENERATE KEYS
    # =========================
    def call_api_generate(self):
        url = "http://127.0.0.1:5000/api/ecc/generate_keys"
        try:
            response = requests.get(url)
            data = response.json()

            if response.status_code == 200:
                QMessageBox.information(self, "Info", data["message"])
            else:
                QMessageBox.warning(self, "Error", data.get("error", "Error"))

        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    # =========================
    # SIGN
    # =========================
    def call_api_sign(self):
        url = "http://127.0.0.1:5000/api/ecc/sign"

        payload = {
            "message": self.ui.txtMessage.toPlainText()
        }

        try:
            response = requests.post(url, json=payload)
            data = response.json()

            if response.status_code == 200:
                self.ui.txtSignature.setText(data["signature"])
                QMessageBox.information(self, "Info", "Signed Successfully")
            else:
                QMessageBox.warning(self, "Error", data.get("error", "Error"))

        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    # =========================
    # VERIFY
    # =========================
    def call_api_verify(self):
        url = "http://127.0.0.1:5000/api/ecc/verify"

        payload = {
            "message": self.ui.txtMessage.toPlainText(),
            "signature": self.ui.txtSignature.toPlainText()
        }

        try:
            response = requests.post(url, json=payload)
            data = response.json()

            if response.status_code == 200:
                if data.get("is_verified"):
                    QMessageBox.information(self, "Info", "Verify SUCCESS")
                else:
                    QMessageBox.warning(self, "Info", "Verify FAILED")
            else:
                QMessageBox.warning(self, "Error", data.get("error", "Error"))

        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))


# =========================
# MAIN
# =========================
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ECCApp()
    window.show()
    sys.exit(app.exec_())