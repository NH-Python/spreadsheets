import xlwings as xw
from pathlib import Path
from typing import Optional


file_path = Path().cwd() / "excel.xlsx"

wb = xw.Book(
    "excel.xlsx"
)  # connect to an existing file in the current working directory
sheet = wb.sheets["Sheet1"]


def clear_range(range: str) -> None:
    sheet.range(range).clear()


def add_text_to_cell(range: str, text: str) -> None:
    sheet.range(range).value = text


def add_formula_to_cell(range: str, formula: str, format: str = "") -> None:
    sheet.range(range).formula = str(formula)
    sheet.range(range).number_format = format


def colorize_cell(range: str, color: tuple) -> None:
    """
    use RGB triplet as tuple: (255,255,255)
    """
    sheet.range(range).color = color


def uncolorize_cell(range: str) -> None:
    sheet.range(range).color = None


def get_value_from_cell(range: str) -> str:
    return sheet.range(range).value


def autofit_column(column: str) -> None:
    sheet.range(column).columns.autofit()


def run() -> None:
    print("Running Excel Demo")
    clear_range("A1:A5")

    add_text_to_cell("A1", "Live Free or Die!")
    value_0 = get_value_from_cell("A1")
    print(value_0)
    assert value_0 == "Live Free or Die!"

    add_text_to_cell("A3", "1000")
    add_text_to_cell("A4", "2000")
    add_formula_to_cell("A5", "=SUM(A3:A4)", "0.00")
    value_1 = get_value_from_cell("A5")
    print(value_1)
    assert value_1 == float(3000)

    lilac = (200, 162, 200)
    lime_green = (127, 255, 0)
    colorize_cell("A1", lilac)
    colorize_cell("A5", lime_green)
    print(sheet.range("A1").color, sheet.range("A5").color)
    assert sheet.range("A1").color == (200, 162, 200)
    assert sheet.range("A5").color == (127, 255, 0)
    uncolorize_cell("A5")
    assert sheet.range("A5").color == None

    autofit_column("A1")


run()
