"""
pymcpx.services.converter
-------------------------
MCP-compatible LangChain tools for unit conversions (length, weight, temperature).
"""

from pymcpx.services.converter.models import (
    LengthConversionInput,
    TemperatureConversionInput,
    WeightConversionInput,
)
from pymcpx.services.converter.SimulationEngine import (
    ConverterSimulationEngine,
    SimulatedResponse,
    SimulationCall,
    deep_merge,
    inputs_match,
)
from pymcpx.services.converter.tools import (
    MCP_TOOLS,
    ConverterToolkit,
    ConvertLengthTool,
    ConvertTemperatureTool,
    ConvertWeightTool,
)

__all__ = [
    "MCP_TOOLS",
    # Tools
    "ConvertLengthTool",
    "ConvertTemperatureTool",
    "ConvertWeightTool",
    # Simulation engine
    "ConverterSimulationEngine",
    # Toolkit
    "ConverterToolkit",
    # Input schemas
    "LengthConversionInput",
    "SimulatedResponse",
    "SimulationCall",
    "TemperatureConversionInput",
    "WeightConversionInput",
    "deep_merge",
    "inputs_match",
]
