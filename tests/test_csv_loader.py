from utils.csv_loader import CSVLoader

class FakeModel:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

def test_csv_loader_loads_models(tmp_path):
    csv_content = """ID,NAME
1,Alice
2,Bob
"""

    file_path = tmp_path / "test.csv"
    file_path.write_text(csv_content)

    loader = CSVLoader()
    records = loader.load(str(file_path), FakeModel)

    assert len(records) == 2
    assert records[0].ID == "1"
    assert records[0].NAME == "Alice"