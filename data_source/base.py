class BaseDataSource:
    def __init__(self, description: str):
        self.description = description

    def get_data(self):
        pass

    def __str__(self):
        return (f"{self.description}\n"
                f"\n"
                f"{self.get_data()}")
