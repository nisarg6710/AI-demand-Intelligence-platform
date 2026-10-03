from src.utils.config_loader import ConfigLoader


def test_config_loader(tmp_path):

    config_file = tmp_path / "test_config.yaml"

    config_file.write_text(
        """
database:
  host: localhost
  port: 3306
  user: test_user
  password: test_password
  database: test_db
"""
    )

    config = ConfigLoader.load(config_file)

    assert config["database"]["host"] == "localhost"
    assert config["database"]["port"] == 3306
    assert config["database"]["database"] == "test_db"