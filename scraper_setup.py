from PyQt5 import QtWidgets, uic
import os
import fileinput
import sys
from shutil import copyfile
from pathlib import Path

ui_file = "common/gui/scraper_ui.ui"
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

        self.tabWidget.setCurrentIndex(0)  # Start on the first page
        self.choose_scraper_button.clicked.connect(self.choose_scraper_pressed)
        self.create_scraper_button.clicked.connect(self.create_button_pressed)
        self.show()

    def dialog(self):
        dialog = ErrorDialog()
        dialog.exec_()

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
        is_v3 = False
        # if self.button_pressed:
        # This is executed when the button is pressed
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
            # with open(full_path, "r+") as output:
            #     # output.seek(config_start)
            #     lines = output.readlines()[config_start:]  # This doesn't seem to do what I want
            #     print("Lines length: " + str(len(lines)))
            #     # for i in range(config_start, config_end):
            #     if not is_v3:
            #         config_list = [
            #             f'"webpage":"{webpage_input}"',
            #             f'"web_path":"{web_path_input}"',
            #             f'"domain_included":"{domain_included_input}"',
            #             f'"domain":"{domain_input}"',
            #             f'"sleep_time":"{sleep_time_input}"',
            #         ]
            #     else:
            #         config_list = [
            #             f'"webpage":"{webpage_input}"',
            #             f'"web_path":"{web_path_input}"',
            #             f'"domain_included":"{domain_included_input}"',
            #             f'"domain":"{domain_input}"',
            #             f'"sleep_time": {sleep_time_input}',
            #             f'{unimportant_input_list}',
            #         ]
            #
            #     for i in range(len(config_list)):
            #         # Need a way to set the pointer to the beginning of the config dictionary and
            #         # iterate over the lines.
            #         output.seek(config_start + i)
            #         output.write("    " + config_list[i] + ",\n")
            #         print(str(i) + "     " + lines[i])

            p = Path("./" + full_path)
            print("p: " + str(p.parent))
            config_filename = scraper_name.replace("_scraper.py", "_configs.py") # I could just split it into a list or something but im lazy
            config_path = str(p.parent).replace("\\", "/") + "/configs/" + config_filename

            p2 = Path("./" + config_path)
            config_dir = str(p2.parent)
            if not os.path.exists(config_dir):
                os.makedirs(config_dir)

            with open(config_path, "a") as output:
                # for i in range(config_start, config_end):
                if not is_v3:
                    config_list = [
                        f'webpage = "{webpage_input}"',
                        f'web_path = "{web_path_input}"',
                        f'domain_included = "{domain_included_input}"',
                        f'domain = "{domain_input}"',
                        f'sleep_time = {sleep_time_input}',
                    ]
                else:
                    config_list = [
                        f'"webpage":"{webpage_input}"',
                        f'"web_path":"{web_path_input}"',
                        f'domain_included = {domain_included_input}',
                        f'"domain":"{domain_input}"',
                        f'sleep_time = {sleep_time_input}',
                        f'non_important = {unimportant_input_list}',
                    ]

                for i in range(len(config_list)):
                    output.write(config_list[i] + "\n")

            # Open the scraper again to change import line
            for line in fileinput.input(full_path, inplace=1):
                # from configs import weekly_configs as configs
                new_import = "from configs import " + config_filename.replace(".py", "") + " as config"
                # Does not support more advanced arguments atm
                lines_to_change = ["import configs", "list_pdf_v2(configs, save_dir)", "list_pdf_v3(config, save_dir)", "configs = {"]
                change_lines_to = [new_import, "list_pdf_v2(config, save_dir, configs_file=True)", "list_pdf_v3(config, save_dir, configs_file=True)", "configs = { # This scraper is not using this"]

                # This method may work for the configs
                for i in range(len(lines_to_change)):
                    if lines_to_change[i] in line:
                        line = line.replace(lines_to_change[i], change_lines_to[i])
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
