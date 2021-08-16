rom _version import __version__
from PyQt5 import QtCore, QtWidgets, uic
from PyQt5.QtWidgets import QTableWidgetItem
import os
import fileinput
import sys
from shutil import copyfile
from pathlib import Path
import jmespath
import requests
import json

# Support for high resolution screens
os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"

ui_file = "common/gui/scraper_ui.ui"
error_modal = "common/gui/error_modal.ui"
success_modal = "common/gui/success_modal.ui"

class ErrorDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(ErrorDialog, self).__init__()
        uic.loadUi(error_modal, self)
        # self.show()

# class SuccessDialog(QtWidgets.QDialog):
#     def __init__(self, parent=None):
#         super(SuccessDialog, self).__init__()
#         uic.loadUi(success_modal, self)
#         self.yes_no_box.accepted.connect(self.accept_button())

#     def accept_button(self):
#         ScraperGui.start_over(ScraperGui.self)


class ScraperGui(QtWidgets.QMainWindow):
    # is_v3 = False
    def __init__(self):
        super(ScraperGui, self).__init__()
        uic.loadUi(ui_file, self)

        self.version_label.setText("Version: " + str(__version__))
        self.tabWidget.setCurrentIndex(0)       # Start on the first page
        self.tabWidget.setTabEnabled(1, False)  # Disable the Choose Scraper tab
        self.tabWidget.setTabEnabled(2, False)  # Disable the Setup tab
        self.tabWidget.setTabEnabled(3, False)  # Disable Crimegraphic's choose scraper tab
        self.tabWidget.setTabEnabled(4, False)  # Disable SetupOpendata tab
        self.tabWidget.setTabEnabled(5, False)  # Disable opendata row tab
        self.tabWidget.setTabEnabled(6, False)  # Disable search schema
        self.tabWidget.setTabEnabled(7, False)  # Disable schema tab
        self.setStyleSheet("QTabBar::tab::disabled {width: 0; height: 0; margin: 0; padding: 0; border: none;} ")  # Hide the tabs

        """Initialize buttons"""
        self.next_button.clicked.connect(self.next_button_pressed)
        self.choose_scraper_button.clicked.connect(self.choose_scraper_pressed)
        self.create_scraper_button.clicked.connect(self.create_button_pressed)
        self.create_cg_button.clicked.connect(self.create_cg_pressed)
        self.choose_cg_button.clicked.connect(self.choose_cg_pressed)
        self.setup_opendata_button.clicked.connect(self.setup_opendata_pressed)
        self.addRow_button.clicked.connect(self._addRow)
        self.removeRow_button.clicked.connect(self._removeRow)
        self.opendata_create_button.clicked.connect(self.opendata_create_pressed)
        self.search_button.clicked.connect(self.get_agency_info)
        self.create_schema_button.clicked.connect(self.create_schema)

        self.show()

    def error_dialog(self):
        error_dialog = ErrorDialog()
        error_dialog.exec_()

    def success_dialog(self):
        success_dialog = SuccessDialog()
        success_dialog.exec_()

    def get_agency_info(self):
        '''Get agency info from dolthub
        :param self: self
        :param search_schema: whether it is search schema tab or not (bool)
        '''
        global searched

        homepage_url = self.homepageURLSearch_input.text()
        # Make sure that there is only one slash after URL
        homepage_url = homepage_url.rstrip("/") + "/"

        owner, repo, branch = 'pdap', 'datasets', 'master'
        query = '''SELECT * FROM `agencies` WHERE `homepage_url` = ''' + f"'{homepage_url}'"
        # print(query)
        res = requests.get('https://www.dolthub.com/api/v1alpha1/{}/{}/{}'.format(owner, repo, branch), params={'q': query})
        jsoned = res.json()
        # print(json.dumps(jsoned, indent=4))
        # Filter out everything except the "rows" table
        expression = jmespath.compile("rows[]")
        searched = expression.search(jsoned)

        """
        Todo:
            create new tab for selecting correct agency
                create form to fill out schema
            switch to tab
                portions can be preloaded from info provided by list_pdf_scrapers tabs
                    homepage_url = webpage_input
            tabulize json rows, send to GUI table
            add buttons per row or something to select the correct agency
            copy schema_template.json to scraper path if it doesn't exist


        """
        # Separate expression to only get what we need to show user
        # rows_expression = jmespath.compile('rows[].{"id":"id", "name":"name","city":"city","state_iso":"state_iso","homepage_url":"homepage_url"}')
        rows_expression = jmespath.compile('rows[].["id", "name","city","state_iso", "homepage_url"]')
        rows_searched = rows_expression.search(jsoned)

        header = self.searchResult_table.horizontalHeader()

        # header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        # header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        if len(rows_searched) > 1:
            # Iterate over rows_searched json "rows"
            for column_number, response_row in enumerate(rows_searched):
                print(column_number)
                self.searchResult_table.insertColumn(column_number)
                row_number = self.searchResult_table.rowCount()

                current_row = 0
                # Add data to table
                for cell_data in response_row:
                    print(cell_data)
                    # print(current_row, column_number, response_row)
                    # print(rows_searched[i])
                    self.searchResult_table.setItem(current_row, column_number, QTableWidgetItem(str(cell_data)))
                    current_row += 1
                    if current_row == row_number:
                        break
            success = True

        elif len(searched) == 0:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setText("Couldn't find anything, may not have an existing dataset!")
            msg.setWindowTitle("Error")
            msg.exec_()

            success = False
            print("Couldn't find anything")

        # Go back through and resize the columns.
        # I tried putting it in the first loop, but it caused it to crash...
        for column_number in range(self.searchResult_table.columnCount()):
            header.setSectionResizeMode(column_number, QtWidgets.QHeaderView.ResizeToContents)
        # print(json.dumps(searched, indent=4))

        if success:
            self.tabWidget.setTabEnabled(7, True)
            self.tabWidget.setCurrentIndex(7)

    def create_schema(self):
        selected_index = self.schema_spinBox.value()
        # Lists start at 0, table doesn't
        selected_agency = selected_index - 1

        try:
            schema_data = searched[selected_agency]
            print(schema_data)

        except IndexError:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setText("Index error: Table isn't that long")
            msg.setWindowTitle("Error")
            msg.exec_()

            print("Index error: Table isn't that long")
        template_folder = "./Base_Scripts/"

        scraper_save_dir_cwd = os.path.join(os.getcwd(), scraper_save_dir.lstrip(".").rstrip("/").rstrip("\\"))
        print("scraper_save_dir: " + str(scraper_save_dir_cwd))

        # Copy and rename the scraper
        scraper_input_text = "schema.json"
        copyfile(template_folder + scraper_input_text, scraper_save_dir_cwd)

    def next_button_pressed(self):
        """Next button on `Choose type` tab"""
        scraper_choice = self.scraper_choice.currentIndex()  # Get index of combobox
        print(scraper_choice)
        if scraper_choice == 0:  #  0 is list_pdf
            print("0")
            self.tabWidget.setTabEnabled(2, False)  # Disable second page of list_pdf setup
            self.tabWidget.setTabEnabled(3, False)  # Disable crimegraphics tabs if enabled
            self.tabWidget.setTabEnabled(4, False)  # Disable Initial Setup page
            self.tabWidget.setTabEnabled(5, False)  # Disable Scraper Setup for opendata
            self.tabWidget.setTabEnabled(1, True)   # Re-enable tabs
            self.setStyleSheet(
                "QTabBar::tab::disabled {width: 0; height: 0; margin: 0; padding: 0; border: none;} "
            )  # Force stylesheet to recompute
            self.tabWidget.setCurrentIndex(1)  # Change to Choose Scraper Page

        elif scraper_choice == 1:  # 1 is opendata
            self.tabWidget.setTabEnabled(1, False)
            self.tabWidget.setTabEnabled(2, False)
            self.tabWidget.setTabEnabled(3, False)
            self.tabWidget.setTabEnabled(4, True)
            self.setStyleSheet(
                "QTabBar::tab::disabled {width: 0; height: 0; margin: 0; padding: 0; border: none;} "
            )  # Force stylesheet to recompute
            self.tabWidget.setCurrentIndex(4)
            print("ERROR: Not Implemented")

        elif scraper_choice == 2:  # 2 is crimegraphics
            # Disable the list_pdf tabs (if enabled)
            self.tabWidget.setTabEnabled(1, False)
            self.tabWidget.setTabEnabled(2, False)
            self.tabWidget.setTabEnabled(4, False)
            self.tabWidget.setTabEnabled(5, False)

            # Enable Crimegraphics Choose Scraper
            self.tabWidget.setTabEnabled(3, True)
            self.setStyleSheet(
                "QTabBar::tab::disabled {width: 0; height: 0; margin: 0; padding: 0; border: none;} "
            )  # Force stylesheet to recompute
            self.tabWidget.setCurrentIndex(3)

    def setup_opendata_pressed(self):
        # Step 1
        global full_path
        global scraper_name
        global is_v3
        global sleep_time
        global save_dir_input
        global scraper_save_dir

        country_input = self.country_input_opendata.text().upper()
        state_input = self.state_input_opendata.text().lower()
        county_input = self.county_input_opendata.text().lower()
        department_type_input = str(self.department_type_input_opendata.currentText()).lower()
        city_input = self.city_input.text().lower()
        save_dir_input = self.save_dir_input_opendata.text().lower()
        # scraper_save_dir = f"./{country_input}/{state_input}/{county_input}/{department_type_input}/{city_input}/"
        scraper_save_dir = os.path.join(country_input, state_input, county_input, department_type_input, city_input)
        scraper_save_dir = scraper_save_dir
        sleep_time = self.sleep_time_input_opendata.value()

        # Create directory if it doesn't exist
        if not os.path.exists(scraper_save_dir):
            os.makedirs(scraper_save_dir)

        # Step 2
        save_dir_input = self.save_dir_input_opendata.text().replace(" ", "_").rstrip("/")  # Clean input of spaces

        if save_dir_input:
            print("save_dir_input not blank")
            save_dir_input = save_dir_input.replace("./data/","")  # Remove any accidental data prepends
            save_dir_input = 'save_dir = "./data/' + save_dir_input + '/"'
        else:
            print("save_dir_input blank")
            save_dir_input = 'save_dir = "./data/"'

        # Step 3
        # Copy the scraper file
        scraper_name_input = self.scraper_name_input_opendata.text()
        scraper_name = scraper_name_input.replace(" ", "_") + "_scraper.py"
        template_folder = "./Base_Scripts/Scrapers/opendata/"
        full_path = scraper_save_dir + scraper_name
        print("full_path: " + str(full_path))

        # Copy and rename the scraper
        scraper_input_text = "opendata_scraper.py"
        copyfile(template_folder + scraper_input_text, full_path)

        self.tabWidget.setTabEnabled(5, True)
        self.tabWidget.setCurrentIndex(5)
        self.setStyleSheet(
            "QTabBar::tab::disabled {width: 0; height: 0; margin: 0; padding: 0; border: none;} "
        )  # Force stylesheet to recompute

    def opendata_create_pressed(self):
        """Edit the config dictionary within the scraper script"""
        try:
            with open(full_path, "r+") as output:
                # output.seek(config_start)
                lines = output.readlines() #[config_start:]  # This doesn't seem to do what I want
                print("Lines length: " + str(len(lines)))
                save_url = [[]]
                print(self.opendataTable.rowCount())
                for i in range(self.opendataTable.rowCount()):
                    data = []
                    for column in range(0,2):  # There are two columns to get
                        # print(f"i = {i}, column = {column} " + str(self.opendataTable.item(i, column).text()))
                        data.append(self.opendataTable.item(i, column).text())

                    save_url[0].append(data)
                print(save_url)

            # for line in fileinput.input(full_path, inplace=1):
            #     if "save_url = []" in line:
            #         line = line.replace(line, "save_url = " + str(save_url))
            #         sys.stdout.write(line)

            save_url_string = "save_url = " + str(save_url)

            lines_to_change = ['save_url = []','save_folder = "./data/"', 'opendata_scraper2(save_url, save_folder, sleep_time=1)']
            change_to = [save_url_string, save_dir_input, f"opendata_scraper2(save_url, save_folder, sleep_time={sleep_time})"]
            for line in fileinput.input(full_path, inplace=1):
                for i in range(len(lines_to_change)):
                    if lines_to_change[i] in line:
                        line = line.replace(lines_to_change[i], change_to[i])
                sys.stdout.write(line)
            print("enabled")

            # Enable and switch to schema tab
            self.tabWidget.setTabEnabled(6, True)
            self.tabWidget.setCurrentIndex(6)
            self.setStyleSheet(
                "QTabBar::tab::disabled {width: 0; height: 0; margin: 0; padding: 0; border: none;} "
            )  # Force stylesheet to recompute
            # self.success_dialog()

        except NameError as exception:
            import traceback

            traceback.print_exc()
            print(str(exception))
            print("You need to complete the first menu first")
            self.tabWidget.setCurrentIndex(0)  # Go back to the start age
            self.error_dialog()
            return

    def _addRow(self):
        rowCount = self.opendataTable.rowCount()
        self.opendataTable.insertRow(rowCount)

    def _removeRow(self):
        if self.opendataTable.rowCount() > 0:
            self.opendataTable.removeRow(self.opendataTable.rowCount()-1)

    # Choose crimegraphic scraper
    def choose_cg_pressed(self):
        if self.choose_cg_input.currentIndex() == 0:
            self.save_dir_input_cg.setText("bulletins")
        elif self.choose_cg_input.currentIndex() == 1:
            self.save_dir_input_cg.setText("daily_bulletins")

    # Create crimegraphic scraper
    def create_cg_pressed(self):
        global scraper_save_dir

        #  Get user input
        country_input = self.country_input_cg.text()
        state_input = self.state_input_cg.text()
        county_input = self.county_input_cg.text()
        department_type_input = str(self.department_type_input_cg.currentText())
        city_input = self.city_input.text()
        url_input = self.url_input_cg.text()
        save_dir_input = self.save_dir_input_cg.text()

        if self.choose_cg_input.currentIndex() == 0:
            cg_type = "crimegraphics_bulletin.py"
        elif self.choose_cg_input.currentIndex() == 1:
            cg_type = "crimegraphics_clery.py"

        scraper_save_dir = f"./{country_input}/{state_input}/{county_input}/{department_type_input}/{city_input}/"
        full_path = scraper_save_dir + cg_type

        # Create directory if it doesn't exist
        if not os.path.exists(scraper_save_dir):
            os.makedirs(scraper_save_dir)

        cg_template_folder = "./Base_Scripts/Scrapers/crimegraphics/"
        # configs = {
        #     "url": "",
        #     "department_code": "",
        department_code = url_input.split(".")
        department_code = str(department_code[0]).replace("https://", "")
        print(department_code)
        save_dir = "./data/" + save_dir_input
        lines_to_change = ['"url": "",', '"department_code": "",', 'save_dir = "./data/"']
        config_list = [f'"url": "{url_input}",', f'"department_code": "{department_code}"', f'save_dir = "{save_dir_input}"']

        if not os.path.exists(scraper_save_dir + cg_type):
            copyfile(cg_template_folder + cg_type, scraper_save_dir + cg_type)

            # Iterate over file to find and replace the configs
            for line in fileinput.input(full_path, inplace=1):
                for i in range(len(lines_to_change)):
                    if lines_to_change[i] in line:
                        line = line.replace(lines_to_change[i], config_list[i])
                sys.stdout.write(line)

            # Enable and switch to schema tab
            self.tabWidget.setTabEnabled(6, True)
            self.tabWidget.setCurrentIndex(6)
            self.setStyleSheet(
                "QTabBar::tab::disabled {width: 0; height: 0; margin: 0; padding: 0; border: none;} "
            )  # Force stylesheet to recompute
            # self.success_dialog()

        else:
            print("ERROR: File already exists")

    # Choose Scraper list_pdf
    def choose_scraper_pressed(self):
        """ 'Enter' button on `Choose Scraper` tab"""
        global full_path
        global scraper_name
        global is_v3
        global scraper_save_dir

        # Step 2
        # /country/state/county/type/city/
        # Get the directory information
        country_input = self.country_input.text()
        state_input = self.state_input.text().lower()
        county_input = self.county_input.text().lower()
        department_type_input = str(self.department_type_input.currentText().lower())
        city_input = self.city_input.text().lower()
        scraper_save_dir = f"./{country_input}/{state_input}/{county_input}/{department_type_input}/{city_input}/"

        # Create directory if it doesn't exist
        if not os.path.exists(scraper_save_dir):
            os.makedirs(scraper_save_dir)

        # Step 4
        # Copy the scraper file
        scraper_name_input = self.scraper_name_input.text()
        scraper_name = scraper_name_input.replace(" ", "_") + "_scraper.py"
        template_folder = "./Base_Scripts/Scrapers/list_pdf_scrapers/"

        # Step 1
        scraper_input_text = self.scraper_input.currentText()  # Get the selected scraper text
        scraper_input_index = self.scraper_input.currentIndex()
        full_path = scraper_save_dir + scraper_name

        if scraper_input_index == 0:
            is_v3 = False
        elif scraper_input_index == 1:
            is_v3 = True

        # Copy and rename the scraper
        copyfile(template_folder + scraper_input_text, full_path)

        # Step 3
        # Edit the save_dir
        save_dir_input = self.save_dir_input.text().replace(" ", "_").rstrip("/")  # Clean input of spaces

        if save_dir_input:
            print("save_dir_input not blank")
            save_dir_input = save_dir_input.replace("./data/","")  # Remove any accidental data prepends
            save_dir_input = 'save_dir = "./data/' + save_dir_input + '"'
        else:
            print("save_dir_input blank")
            save_dir_input = 'save_dir = "./data/"'


        # make sure that black formatting does not affect this
        # outer two quotes should be single
        default_save_dir = 'save_dir = "./data/"'
        print(save_dir_input)
        for line in fileinput.input(full_path, inplace=1):
            if default_save_dir in line:
                line = line.replace(default_save_dir, save_dir_input)
            sys.stdout.write(line)

        # Enable next page, then switch to it
        self.tabWidget.setTabEnabled(2, True)
        # Force stylesheet to recompute
        self.setStyleSheet("QTabBar::tab::disabled {width: 0; height: 0; margin: 0; padding: 0; border: none;} ")
        self.tabWidget.setCurrentIndex(2)

    # list_pdf create
    def create_button_pressed(self):
        # This is executed when the button is pressed

        # if self.button_pressed
        webpage_input = self.webpage_input.text()
        web_path_input = self.web_path_input.text()
        domain_included_input = self.domain_included_input.currentText()
        # print(domain_included_input)
        domain_input = self.domain_input.text()
        sleep_time_input = self.sleep_time_input.value()
        unimportant_input = self.unimportant_input.toPlainText().rstrip(", ").replace(",", ", ")  # Get and clean input
        unimportant_input_list = unimportant_input.split(", ")
        # print(unimportant_input_list)

        # Get the index of config = {
        try:
            """Edit the config dictionary within the scraper script"""
            with open(full_path, "r+") as output:
                # output.seek(config_start)
                lines = output.readlines() #[config_start:]  # This doesn't seem to do what I want
                print("Lines length: " + str(len(lines)))
                # for i in range(config_start, config_end):
                if not is_v3:
                    config_list = [
                        f'"webpage":"{webpage_input}"',
                        f'"web_path":"{web_path_input}"',
                        f'"domain_included":{domain_included_input}',
                        f'"domain":"{domain_input}"',
                        f'"sleep_time":{sleep_time_input}',
                    ]
                else:
                    print("is v3, putting non_important list")
                    config_list = [
                        f'"webpage":"{webpage_input}"',
                        f'"web_path":"{web_path_input}"',
                        f'"domain_included":{domain_included_input}',
                        f'"domain":"{domain_input}"',
                        f'"sleep_time": {sleep_time_input}',
                        f'"non_important":{unimportant_input_list}',
                    ]

            # Does not support more advanced arguments atm
            lines_to_change = ['"webpage": "",', '"web_path": "",', '"domain_included": False,', '"domain": "",', '"sleep_time": 5,']

            if is_v3:
                print("is v3")
                lines_to_change = lines_to_change.append('"non_important": [],')
            # Use fileinput to replace config lines.
            for line in fileinput.input(full_path, inplace=1):
                for i in range(len(lines_to_change)):
                    if lines_to_change[i] in line:
                        line = line.replace(lines_to_change[i], config_list[i] + ",")
                sys.stdout.write(line)

            # Enable and switch to schema tab
            self.tabWidget.setTabEnabled(6, True)
            self.tabWidget.setCurrentIndex(6)
            self.setStyleSheet(
                "QTabBar::tab::disabled {width: 0; height: 0; margin: 0; padding: 0; border: none;} "
            )  # Force stylesheet to recompute
            # self.success_dialog()

        except NameError as exception:
            import traceback

            traceback.print_exc()
            print(str(exception))
            print("You need to complete the first menu first")
            self.tabWidget.setCurrentIndex(1)  # Go back to the first list_pdf page
            self.error_dialog()
            return

    def start_over():
        for tab in range(1,6):
            print(" [*] Tab: " + str(tab))
            self.tabWidget.setTabEnabled(tab, False)

app = QtWidgets.QApplication(sys.argv)
app.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
window = ScraperGui()
app.exec_()


# def create_new_folder(folder_name):
