from configparser import ConfigParser, ExtendedInterpolation


class MyConfigParser(object):

    def __init__(self):
        """
        initialize the file parser with
        ExtendedInterpolation to use ${Section:variable} format
        [Section]
        option=variable
        """
        self.config_parser = ConfigParser(interpolation=ExtendedInterpolation())

    def read_ini_file(self, file):
        """
        Parses in the passed in INI file.

        :param file: INI file to parse
        :return: INI file is parsed
        """
        with open(file, 'r') as f:
            self.config_parser.read_file(f)

    def add_section_toFile(self, section):
        """
        adds a configuration section to a file

        :param section: configuration section to add in file
        :return: void
        """
        if not self.config_parser.has_section(section):
            self.config_parser.add_section(section)

    def add_configurations_to_section(self, section, lst_config):
        """
        Adds a configuration list to configuration section

        :param section: configuration section
        :param lst_config: key, value list of configurations
        :return: void
        """
        if not self.config_parser.has_section(section):
            self.add_section_toFile(section)

        for option, value in lst_config:
            print(option, value)
            self.config_parser.set(section, option, value)

    def get_config_items_by_section(self, section):
        """
        Retrieves the configurations for a particular section

        :param section: INI file section
        :return: a list of name, value pairs for the options in the section
        """
        return self.config_parser.items(section)

    def remove_config_section(self, section):
        """
        Removes a configuration section from a file
        :param section: configuration section to remove
        :return: void
        """
        self.config_parser.remove_section(section)

    def remove_options_from_section(self, section, lst_options):
        """
        Removes a list of options from configuration section
        :param section: configuration section in file
        :param lst_options: list of options to remove
        :return: void
        """
        for option, value in lst_options:
            self.config_parser.remove_option(section, option)

    def write_file(self, file, delimiter=True):
        with open(file, 'w') as f:
            self.config_parser.write(f, delimiter)
