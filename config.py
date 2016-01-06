import configparser


class TrackerConfig:
    def __init__(self, path):
        self.config = configparser.ConfigParser()

        try:
            with open(path, mode='r', encoding='utf-8') as config_file:
                pass
        except IOError:
            self.create_config()
            with open(path, mode='w', encoding='utf-8') as config_file:
                self.config.write(config_file)

    def create_config(self):
        """Create a config file
        """
        self.config.add_section("Settings")
        self.config.set("Settings", "End of round alert", 'False')
        self.config.set("Settings", "Reset includes players", 'False')
        self.config.set("Settings", "Join Battle automatically adds 3", 'True')
