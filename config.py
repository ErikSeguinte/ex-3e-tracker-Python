import configparser, os
import ZeltInit


class TrackerConfig:
    def __init__(self, path):
        self.application_path = path
        self.path = os.path.join(path, 'Ex3-Tracker.cfg')
        self.path = os.path.relpath(self.path)
        self.config = configparser.ConfigParser()

        try:
            self.config.read_file(open(self.path))

        except IOError:
            self.create_config()
            self.save_config()
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

        # 'Every Turn', 'Every Round', 'Off'
        self.config.set("Settings", "Auto-save", "Every Turn")

        auto_save = os.path.join(self.application_path, '__autosave.sav')
        rel_path = os.path.relpath(auto_save)
        print(rel_path)
        print('config save', auto_save)
        self.config.set('Settings', 'auto_save custom path', 'False')
        self.config.set('Settings', 'Auto-save path', rel_path)

    def save_config(self):
        try:
            with open(self.path, mode='w', encoding='utf-8') as config_file:
                self.config.write(config_file)
        except IOError:
            pass

    def recreate_config(self):
        self.config = configparser.ConfigParser()
        self.create_config()
        self.save_config()
        ZeltInit.config = self.config
