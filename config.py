import configparser, os
import ZeltInit


class TrackerConfig:
    def __init__(self, path):
        self.application_path = path
        self.path = os.path.join(path, 'Ex3-Tracker.cfg')
        self.config = configparser.ConfigParser()

        try:
            self.config.read_file(open(self.path))

        except IOError:
            self.create_config()
            with open(self.path, mode='w', encoding='utf-8') as config_file:
                self.config.write(config_file)
        else:
            self.config.sections()
            print(self.config.sections())

        ZeltInit.config = self.config

    def create_config(self):
        """Create a config file
        """
        self.config.add_section("Settings")
        self.config.set("Settings", "End of round alert", 'False')
        self.config.set("Settings", "Reset includes players", 'False')
        self.config.set("Settings", "Join Battle automatically adds 3", 'True')
        
        #'Every turn', 'Every round', 'Off'
        self.config.set("Settings", "Auto-save","Every turn")

        auto_save = os.path.join(self.application_path, '__resume.txt')
        self.config.set('Settings', 'auto_save_custom_path', 'False')
        self.config.set('Settings', 'Auto-save path', auto_save)
