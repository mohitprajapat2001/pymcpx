from pymcpx.services.converter import (
    ConverterToolkit,
    ConvertLengthTool,
    ConvertTemperatureTool,
    ConvertWeightTool,
)
from pymcpx.services.converter.SimulationEngine import ConverterSimulationEngine


def test_convert_length_tool() -> None:
    tool = ConvertLengthTool()
    assert tool.name == "convert_length"
    # m to cm
    assert tool.run({"value": 1.5, "from_unit": "m", "to_unit": "cm"}) == "150"
    # km to mile
    assert tool.run({"value": 1.0, "from_unit": "km", "to_unit": "m"}) == "1000"
    # Error handling
    assert "Error:" in tool.run({"value": 1.0, "from_unit": "invalid", "to_unit": "m"})


def test_convert_weight_tool() -> None:
    tool = ConvertWeightTool()
    assert tool.name == "convert_weight"
    # kg to g
    assert tool.run({"value": 2.5, "from_unit": "kg", "to_unit": "g"}) == "2500"
    # lb to oz (1 lb = 16 oz)
    assert tool.run({"value": 2.0, "from_unit": "lb", "to_unit": "oz"}) == "32"


def test_convert_temperature_tool() -> None:
    tool = ConvertTemperatureTool()
    assert tool.name == "convert_temperature"
    # C to F
    assert tool.run({"value": 0.0, "from_unit": "c", "to_unit": "f"}) == "32"
    # F to C
    assert tool.run({"value": 212.0, "from_unit": "f", "to_unit": "c"}) == "100"
    # C to K
    assert tool.run({"value": 25.0, "from_unit": "c", "to_unit": "k"}) == "298.15"


def test_converter_toolkit() -> None:
    toolkit = ConverterToolkit()
    tools = toolkit.get_tools()
    assert len(tools) == 3
    names = {t.name for t in tools}
    assert "convert_length" in names
    assert "convert_weight" in names
    assert "convert_temperature" in names


def test_converter_simulation_engine() -> None:
    engine = ConverterSimulationEngine()
    engine.register(
        tool_name="convert_length",
        input_match={"value": 10.0, "from_unit": "m", "to_unit": "cm"},
        output="OVERRIDDEN_VAL",
    )

    assert (
        engine.run("convert_length", {"value": 10.0, "from_unit": "m", "to_unit": "cm"})
        == "OVERRIDDEN_VAL"
    )
    # Real fallback
    assert engine.run("convert_length", {"value": 1.0, "from_unit": "m", "to_unit": "cm"}) == "100"
