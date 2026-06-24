from pymcpx.services.calculator import (
    AbsTool,
    AddTool,
    CalculatorToolkit,
    DivideTool,
    ModuloTool,
    MultiplyTool,
    PowerTool,
    SqrtTool,
    SubtractTool,
)


def test_add_tool() -> None:
    tool = AddTool()
    assert tool.name == "add_numbers"
    assert tool.run({"a": 3, "b": 4}) == "7"
    assert tool.run({"a": 3.5, "b": 1.5}) == "5"


def test_subtract_tool() -> None:
    tool = SubtractTool()
    assert tool.name == "subtract_numbers"
    assert tool.run({"a": 10, "b": 4}) == "6"
    assert tool.run({"a": 5.5, "b": 1.5}) == "4"


def test_multiply_tool() -> None:
    tool = MultiplyTool()
    assert tool.name == "multiply_numbers"
    assert tool.run({"a": 3, "b": 4}) == "12"
    assert tool.run({"a": 2.5, "b": 4}) == "10"


def test_divide_tool() -> None:
    tool = DivideTool()
    assert tool.name == "divide_numbers"
    assert tool.run({"a": 10, "b": 4}) == "2.5"
    assert tool.run({"a": 5, "b": 0}) == "Error: Division by zero is undefined."


def test_power_tool() -> None:
    tool = PowerTool()
    assert tool.name == "power_numbers"
    assert tool.run({"a": 2, "b": 3}) == "8"
    assert tool.run({"a": 9, "b": 0.5}) == "3"


def test_modulo_tool() -> None:
    tool = ModuloTool()
    assert tool.name == "modulo_numbers"
    assert tool.run({"a": 10, "b": 3}) == "1"
    assert tool.run({"a": 5, "b": 0}) == "Error: Modulo by zero is undefined."


def test_sqrt_tool() -> None:
    tool = SqrtTool()
    assert tool.name == "sqrt_number"
    assert tool.run({"a": 9}) == "3"
    assert tool.run({"a": -1}) == "Error: Square root of a negative number is not real."


def test_abs_tool() -> None:
    tool = AbsTool()
    assert tool.name == "abs_number"
    assert tool.run({"a": -5}) == "5"
    assert tool.run({"a": 3.14}) == "3.14"


def test_toolkit() -> None:
    toolkit = CalculatorToolkit()
    tools = toolkit.get_tools()
    assert len(tools) == 8
    names = {t.name for t in tools}
    assert "add_numbers" in names
    assert "subtract_numbers" in names
