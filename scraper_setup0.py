from PyQt5 import QtWidgets, uic
import os
import fileinput
import sys
from shutil import copyfile
from pathlib import Path

ui_file = "common/gui/scraper_ui2.ui"
error_modal = "common/gui/error_modal.ui"


class ErrorDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(ErrorDialog, self).__init__()
        uic.loadUi(error_modal, self)
        # self.show()


class ScraperGui(QtWidgets.QMainWindow):
    # is_v3 = False
    def __init__(self):
        super(ScraperGui, self).__init__()
        uic.loadUi(ui_file, self)

        self.tabWidget.setCurrentIndex(0)       # Start on the first page
        self.tabWidget.setTabEnabled(1, False)  # Disable the Choose Scraper tab
        self.tabWidget.setTabEnabled(2, False)  # Disable the Setup tab
        self.tabWidget.setTabEnabled(3, False)  # Disable Crimegraphic's choose scraper tab
        self.setStyleSheet("QTabBar::tab::disabled {width: 0; height: 0; margin: 0; padding: 0; border: none;} ") # Hide the tabs

        """Initialize buttons"""
        self.next_button.clicked.connect(self.next_button_pressed)
        self.choose_scraper_button.clicked.connect(self.choose_scraper_pressed)
        self.create_scraper_button.clicked.connect(self.create_button_pressed)
        self.create_cg_button.clicked.connect(self.create_cg_pressed)
        self.choose_cg_button.clicked.connect(self.choose_cg_pressed)
        self.show()

    def dialog(self):
        dialog = ErrorDialog()
        dialog.exec_()

    def next_button_pressed(self):
        scraper_choice = self.scraper_choice.currentIndex()  # Get index of combobox
        print(scraper_choice)
        if scraper_choice == 0: #  0 is list_pdf
            print("0")
            self.tabWidget.setTabEnabled(1, True)  # Re-enable tabs
            self.tabWidget.setTabEnabled(2, True)
            self.setStyleSheet("QTabBar::tab::disabled {width: 0; height: 0; margin: 0; padding: 0; border: none;} ")  # Force stylesheet to recompute
            self.tabWidget.setCurrentIndex(1)  # Change to Choose Scraper Page

        elif scraper_choice == 1:  # 1 is opendata
            print("ERROR: Not Implemented")

        elif scraper_choice == 2:  # 2 is crimegraphics
            self.tabWidget.setTabEnabled(3, True)  # Enable Crimegraphics Choose Scraper
            self.setStyleSheet("QTabBar::tab::disabled {width: 0; height: 0; margin: 0; padding: 0; border: none;} ")  # Force stylesheet to recompute
            self.tabWidget.setCurrentIndex(3)

    def choose_cg_pressed(self):
        if self.choose_cg_input.currentIndex() == 0:
            self.save_dir_input_cg.setText("bulletins")
        elif self.choose_cg_input.currentIndex() == 1:
            self.save_dir_input_cg.setText("daily_bulletins")

    def create_cg_pressed(self):
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

            for line in fileinput.input(full_path, inplace=1):
                for i in range(len(lines_to_change)):
                    if lines_to_change[i] in line:
                        line = line.replace(lines_to_change[i], config_list[i])
                sys.stdout.write(line)
        else:
            print("ERROR: File already exists")

    def choose_scraper_pressed(self):
        global full_path
        global scraper_name
        # /country/state/county/type/city/
        # Get the directory information
        country_input = self.country_input.text()
        state_input = self.state_input.text()
        county_input = self.county_input.text()
        department_type_input = str(self.department_type_input.currentText())
        city_input = self.city_input.text()
        scraper_save_dir = f"./{country_input}/{state_input}/{county_input}/{department_type_input}/{city_input}/"

        # Create directory if it doesn't exist
        if not os.path.exists(scraper_save_dir):
            os.makedirs(scraper_save_dir)

        # Copy the scraper file
        scraper_name_input = self.scraper_name_input.text()
        scraper_name = scraper_name_input.replace(" ", "_") + "_scraper.py"
        template_folder = "./Base_Scripts/Scrapers/list_pdf_extractors/"
        scraper_input = self.scraper_input.currentText()  # Get the selected scraper text
        full_path = scraper_save_dir + scraper_name
        # Copy and rename the scraper
        copyfile(template_folder + scraper_input, full_path)

        # Edit the save_dir
        save_dir_input = self.save_dir_input.text().replace(" ", "_").rstrip("/")  # Clean input of spaces
        save_dir_input = "save_dir = ./data/" + save_dir_input.replace("./data/", "") + "/"  # Remove any accidental data prepends
        # make sure that black formatting does not affect this
        # outer two quotes should be single
        default_save_dir = 'save_dir = "./data/"'
        for line in fileinput.input(full_path, inplace=1):

            if default_save_dir in line:
                line = line.replace(default_save_dir, save_dir_input)
            sys.stdout.write(line)

    def create_button_pressed(self):
        # This is executed when the button is pressed
        is_v3 = False
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
            with open(full_path, "r+") as output:
                i = 0
                f = 0
                for num, line in enumerate(output, 1):
                    if "configs = {" in line:
                        i += 1
                        if i > 1:
                            config_start = num
                            print(line, num)
                    elif "}" in line:
                        f += 1
                        if f > 1:
                            config_end = num
                            print(line, num)
                    elif '"non_important": [],"' in line:
                        is_v3 = True

            '''Edit the config dictionary within the scraper script'''
            with open(full_path, "r+") as output:
                # output.seek(config_start)
                lines = output.readlines()[config_start:]  # This doesn't seem to do what I want
                print("Lines length: " + str(len(lines)))
                # for i in range(config_start, config_end):
                if not is_v3:
                    config_list = [
                        f'"webpage":"{webpage_input}"',
                        f'"web_path":"{web_path_input}"',
                        f'"domain_included":"{domain_included_input}"',
                        f'"domain":"{domain_input}"',
                        f'"sleep_time":"{sleep_time_input}"',
                    ]
                else:
                    config_list = [
                        f'"webpage":"{webpage_input}"',
                        f'"web_path":"{web_path_input}"',
                        f'"domain_included":"{domain_included_input}"',
                        f'"domain":"{domain_input}"',
                        f'"sleep_time": {sleep_time_input}',
                        f'"non_important":{unimportant_input_list}',
                    ]

            # Does not support more advanced arguments atm
            lines_to_change = ['"webpage": "",', '"web_path": "",', '"domain_included": False,', '"domain": "",', '"sleep_time": 5,']

            if is_v3:
                lines_to_change = lines_to_change.append('"non_important": [],')
            # Use fileinput to replace config lines.
            for line in fileinput.input(full_path, inplace=1):
                for i in range(len(lines_to_change)):
                    if lines_to_change[i] in line:
                        line = line.replace(lines_to_change[i], config_list[i])
                sys.stdout.write(line)

        except NameError as exception:
            import traceback
            traceback.print_exc()
            print(str(exception))
            print("You need to complete the first menu first")
            self.tabWidget.setCurrentIndex(0) # Go back to the start age
            self.dialog()
            return

app = QtWidgets.QApplication(sys.argv)
window = ScraperGui()
app.exec_()



# def create_new_folder(folder_name):
