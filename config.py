import configparser
import ZeltInit


class TrackerConfig:
    def __init__(self, path):
        self.path = path
        self.config = configparser.ConfigParser()

        try:
            self.config.read_file(open(path))

        except IOError:
            self.create_config()
            with open(path, mode='w', encoding='utf-8') as config_file:
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
