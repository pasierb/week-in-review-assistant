import yaml
from data_source.jrnl import JrnlDataSource
from data_source.git_commits import GitCommitsDataSource
from processor import Processor


def load_config(config_path="config.yaml"):
    with open(config_path, "r") as f:
        return yaml.safe_load(f)


def create_data_source(source_config):
    if source_config["type"] == "jrnl":
        return JrnlDataSource(source_config["name"])
    elif source_config["type"] == "git_commits":
        return GitCommitsDataSource(source_config["name"], source_config["repositories"])
    else:
        raise ValueError(f"Unknown data source type: {source_config['type']}")


def main():
    config = load_config()
    
    data_sources = [
        create_data_source(source_config)
        for source_config in config["data_sources"]
    ]

    processor = Processor(
        system_prompt=config["system_prompt"],
        data_sources=data_sources,
    )

    print(processor.process())


if __name__ == "__main__":
    main()
