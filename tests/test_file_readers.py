from unittest.mock import MagicMock, patch

from src.file_readers import read_csv_transactions, read_excel_transactions

# ---------- CSV ----------


@patch("pandas.read_csv")
def test_read_csv_transactions(mock_read_csv):
    mock_df = MagicMock()
    mock_df.to_dict.return_value = [{"amount": 100, "currency": "USD"}]

    mock_read_csv.return_value = mock_df

    result = read_csv_transactions("fake.csv")

    assert result == [{"amount": 100, "currency": "USD"}]
    mock_read_csv.assert_called_once_with("fake.csv")


# ---------- EXCEL ----------


@patch("pandas.read_excel")
def test_read_excel_transactions(mock_read_excel):
    mock_df = MagicMock()
    mock_df.to_dict.return_value = [{"amount": 200, "currency": "EUR"}]

    mock_read_excel.return_value = mock_df

    result = read_excel_transactions("fake.xlsx")

    assert result == [{"amount": 200, "currency": "EUR"}]
    mock_read_excel.assert_called_once_with("fake.xlsx")
