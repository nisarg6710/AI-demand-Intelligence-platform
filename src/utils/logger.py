import logging
import os


class ProjectLogger:

    @staticmethod
    def get_logger():

        os.makedirs(
            "logs",
            exist_ok=True,
        )

        logging.basicConfig(

            filename="logs/project.log",

            level=logging.INFO,

            format="%(asctime)s | %(levelname)s | %(message)s",

            filemode="a",

        )

        return logging.getLogger("AIPlatform")