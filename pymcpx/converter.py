"""
pymcpx.converter — MCP-compatible LangChain tools for unit conversions.

Re-exports from ``pymcpx.services.converter`` for convenient access via
``from pymcpx.converter import ConvertLengthTool``.

The original ``from pymcpx.services.converter import ...`` path also works.
"""

from pymcpx.services.converter import (
    MCP_TOOLS,
    ConverterSimulationEngine,
    ConverterToolkit,
    ConvertLengthTool,
    ConvertTemperatureTool,
    ConvertWeightTool,
    LengthConversionInput,
    SimulatedResponse,
    SimulationCall,
    TemperatureConversionInput,
    WeightConversionInput,
    deep_merge,
    inputs_match,
)

__all__ = [
    "MCP_TOOLS",
    "ConvertLengthTool",
    "ConvertTemperatureTool",
    "ConvertWeightTool",
    "ConverterSimulationEngine",
    "ConverterToolkit",
    "LengthConversionInput",
    "SimulatedResponse",
    "SimulationCall",
    "TemperatureConversionInput",
    "WeightConversionInput",
    "deep_merge",
    "inputs_match",
]
