from PyQt5 import QtWidgets, uic
import os
import fileinput
import sys
from shutil import copyfile

ui_file = "common/gui/scraper_ui.ui"
error_modal = "common/gui/error_modal.ui"

class ErrorDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(ErrorDialog, self).__init__()
        uic.loadUi(error_modal, self)
        # self.show()

class ScraperGui(QtWidgets.QMainWindow):
    is_v3 = False
    def __init__(self):
        super(ScraperGui, self).__init__()
        uic.loadUi(ui_file, self)

        self.tabWidget.setCurrentIndex(0) # Start on the first page
        self.choose_scraper_button.clicked.connect(self.choose_scraper_pressed)
        self.create_scraper_button.clicked.connect(self.create_button_pressed)
        self.show()

    def dialog(self):
        dialog = ErrorDialog()
        dialog.exec_()

    def choose_scraper_pressed(self):
        # /country/state/county/type/city/
        # Get the directory information
        country_input = self.country_input.text()
        state_input = self.state_input.text()
        county_input = self.county_input.text()
        department_type_input = str(self.department_type_input.currentText())
        city_input = self.city_input.text()
        scraper_save_dir = f"./{country_input}/{state_input}/{county_input}/{department_type_input}/{city_input}/"
        if not os.path.exists(scraper_save_dir):
            os.makedirs(scraper_save_dir)

        # Copy the scraper file
        scraper_name_input = self.scraper_name_input.text()
        scraper_name = scraper_name_input.replace(" ","_") + "_scraper.py"
        template_folder = "./Base_Scripts/Scrapers/list_pdf_extractors/"
        scraper_input = self.scraper_input.currentText() # Get the selected scraper text
        global full_path
        full_path = scraper_save_dir + scraper_name
        # Copy and rename the scraper
        copyfile(template_folder + scraper_input, full_path)

        # Edit the save_dir
        save_dir_input = self.save_dir_input.text().replace(" ","_").rstrip("/") # Clean input of spaces
        save_dir_input = "save_dir = ./data/" + save_dir_input.replace("./data/","") + "/" # Remove any accidental data prepends
        print(save_dir_input)
        default_save_dir = 'save_dir = \"./data/\"'
        for line in fileinput.input(full_path, inplace=1):
            # make sure that black formatting does not affect this
            # outer two quotes should be single
            if default_save_dir in line:
                line = line.replace(default_save_dir,save_dir_input)
            sys.stdout.write(line)



    def create_button_pressed(self):
        # if self.button_pressed:
        # This is executed when the button is pressed
        webpage_input = self.webpage_input.text()
        web_path_input = self.web_path_input.text()
        domain_included_input = self.domain_included_input.currentText()
        # print(domain_included_input)
        domain_input = self.domain_input.text()
        sleep_time_input = self.sleep_time_input.value()
        unimportant_input = self.unimportant_input.toPlainText().rstrip(", ").replace(",", ", ") # Get and clean input
        unimportant_input_list = unimportant_input.split(", ")
        # print(unimportant_input_list)

        # Get the index of config = {
        try:
            # print("stuff")
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

            with open(full_path, "r+") as output:
                lines = output.readlines()
                print("Lines lenght: " + str(len(lines)))
                # for i in range(config_start, config_end):

                if not is_v3:
                    config_list = [f'"webpage":"{webpage_input}"',f'"web_path":"{web_path_input}"', f'"domain_input":"{domain_included_input}"',f'"domain":"{domain_included_input}"',f'"sleep_time":"{sleep_time_input}"']
                else:
                    config_list = [f'"webpage":"{webpage_input}"',f'"web_path":"{web_path_input}"', f'"domain_input":"{domain_included_input}"',f'"domain":"{domain_included_input}"',f'"sleep_time":"{sleep_time_input}"',f'"{unimportant_input_list}"']
                for i in range(len(config_list)):
                    print(str(i) + "     " + lines[i])



        except NameError:
            print("You need to complete the first menu first")
            self.dialog()
            return


app = QtWidgets.QApplication(sys.argv)
window = ScraperGui()
app.exec_()

# def create_new_folder(folder_name):
