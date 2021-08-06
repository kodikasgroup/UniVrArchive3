import yaml


class Utils:
    file_path = "key.yaml"

    @staticmethod
    def get_key() -> str:
        """
        retrieve the api key for telegram from yaml file
        :return: api key
        """
        with open(Utils.file_path, "r") as f:
            parsed_yaml_file = yaml.load(f, Loader=yaml.BaseLoader)
            return parsed_yaml_file["key"]
