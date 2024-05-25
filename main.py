from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QTreeView,
    QLineEdit,
    QMainWindow,
)
from PyQt5.QtGui import QStandardItemModel


class FinanceApp(QMainWindow):
    def __init__(self):
        super(FinanceApp, self).__init__()
        self.setWindowTitle("InterestMe 2.0")
        self.resize(800, 600)

        main_window = QWidget()

        self.rate_text = QLabel("Interest Rate (%):")
        self.rate_input = QLineEdit()

        self.initial_text = QLabel("Initial Investment:")
        self.initial_input = QLineEdit()

        self.years_text = QLabel("Years to Invest:")
        self.years_input = QLineEdit()

        # create TreeView
        self.model = QStandardItemModel()
        self.tree_view = QTreeView()
        self.tree_view.setModel(self.model)

        self.calc_button = QPushButton("Calculate")
        self.clear_button = QPushButton("Clear")

        self.figure = QLabel("--- CHART WILL BE HERE SOON ---")

        self.master_layout = QVBoxLayout()
        self.row1 = QHBoxLayout()
        self.row2 = QHBoxLayout()
        self.col1 = QVBoxLayout()
        self.col2 = QVBoxLayout()

        self.row1.addWidget(self.initial_text)
        self.row1.addWidget(self.initial_input)
        self.row1.addWidget(self.rate_text)
        self.row1.addWidget(self.rate_input)
        self.row1.addWidget(self.years_text)
        self.row1.addWidget(self.years_input)

        self.col1.addWidget(self.tree_view)
        self.col1.addWidget(self.calc_button)
        self.col1.addWidget(self.clear_button)

        self.col2.addWidget(self.figure)

        self.row2.addLayout(self.col1, 20)
        self.row2.addLayout(self.col2, 80)

        self.master_layout.addLayout(self.row1)
        self.master_layout.addLayout(self.row2)

        main_window.setLayout(self.master_layout)
        self.setCentralWidget(main_window)


if __name__ == "__main__":
    app = QApplication([])
    my_app = FinanceApp()
    my_app.show()
    app.exec_()
