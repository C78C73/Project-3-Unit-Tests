import unittest
from unittest.mock import patch
import StockDataVisualizer

class TestInputs(unittest.TestCase):

    @patch('builtins.input', side_effect=["F"])
    def test_stock_symbol_valid(self, mock_input):
        stockSymbol = StockDataVisualizer.input("\nPlease enter the stock symbol for the company you want data for: ").upper()
        self.assertTrue(stockSymbol.isalpha())
        self.assertTrue(stockSymbol.isupper())
        self.assertTrue(1 <= len(stockSymbol) <= 5)

    @patch('builtins.input', side_effect=["1"])
    def test_chart_type_valid(self, mock_input):
        chartOptions = {"1": "LINE", "2": "BAR"}
        chartChoice = StockDataVisualizer.input("\nPlease enter the chart type you would like (LINE, BAR): ").upper()
        self.assertIn(chartChoice, chartOptions)

    @patch('builtins.input', side_effect=["2"])
    def test_time_series_valid(self, mock_input):
        timeSeriesOptions = {"1": "INTRADAY", "2": "DAILY", "3": "DAILY_ADJUSTED", "4": "WEEKLY", "5": "WEEKLY_ADJUSTED", "6": "MONTHLY", "7": "MONTHLY_ADJUSTED"}
        timeSeriesChoice = StockDataVisualizer.input("\nPlease enter the time series function you would like the api to use (INTRADAY, DAILY, DAILY_ADJUSTED, WEEKLY, WEEKLY_ADJUSTED, MONTHLY, MONTHLY_ADJUSTED): ").upper()
        self.assertIn(timeSeriesChoice, timeSeriesOptions)

    @patch('builtins.input', side_effect=["2025-04-16"])
    def test_start_date_valid(self, mock_input):
        date_str = StockDataVisualizer.input("\nPlease enter the beginning date in M-D-YY or MM-DD-YY format: ")
        date_obj = StockDataVisualizer.datetime.datetime.strptime(date_str, "%Y-%m-%d")
        self.assertIsInstance(date_obj, StockDataVisualizer.datetime.datetime)
        self.assertLessEqual(date_obj, StockDataVisualizer.datetime.datetime.now())

    @patch('builtins.input', side_effect=["2025-04-20"])
    def test_end_date_valid(self, mock_input):
        date_str = StockDataVisualizer.input("\nPlease enter the beginning date in M-D-YY or MM-DD-YY format: ")
        date_obj = StockDataVisualizer.datetime.datetime.strptime(date_str, "%Y-%m-%d")
        self.assertIsInstance(date_obj, StockDataVisualizer.datetime.datetime)
        self.assertLessEqual(date_obj, StockDataVisualizer.datetime.datetime.now())

unittest.main()