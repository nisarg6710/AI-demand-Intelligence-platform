import os
from datetime import datetime


class PromptWriter:

    @staticmethod
    def save(
        system_prompt,
        user_prompt,
    ):

        prompt_dir = "artifacts/prompts"

        os.makedirs(
            prompt_dir,
            exist_ok=True,
        )

        timestamp = datetime.now().strftime(
            "%Y%m%d_%H%M%S"
        )

        system_path = os.path.join(
            prompt_dir,
            f"system_prompt_{timestamp}.txt",
        )

        user_path = os.path.join(
            prompt_dir,
            f"user_prompt_{timestamp}.txt",
        )

        with open(
            system_path,
            "w",
            encoding="utf-8",
        ) as file:

            file.write(system_prompt)

        with open(
            user_path,
            "w",
            encoding="utf-8",
        ) as file:

            file.write(user_prompt)

        return {

            "system_prompt": system_path,

            "user_prompt": user_path,

        }