import os


class PreFlightCheck:
    @staticmethod
    def _configuration_error(message: str):
        """ Print error message and exit """
        raise ValueError(message)

    @staticmethod
    def _check(env_key: str, env_value) -> str:
        """ Check if environment is set properly and return the value """
        if env_value is None or env_value == "":
            PreFlightCheck._configuration_error(f"PLEASE SET {env_key}")
        return env_value

    @staticmethod
    def get_config(env_key: str) -> str:
        """ Get environment value """
        return PreFlightCheck._check(env_key, os.getenv(env_key))
