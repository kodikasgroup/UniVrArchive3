import yaml


class Utils:
    file_path = "config.yaml"

    @staticmethod
    def __parse_yaml_file():
        """
        open settings yaml file and parse it
        :return: parsed file
        """
        with open(Utils.file_path, "r") as f:
            return yaml.load(f, Loader=yaml.BaseLoader)

    @staticmethod
    def get_token() -> str:
        """
        retrieve the api key for telegram from parsed yaml file
        :return: api key
        """
        parsed_yaml_file = Utils.__parse_yaml_file()
        return parsed_yaml_file["token"]
