"""yunpy — Python caller for the project "yun".

Provides domain models for logistics optimization: locations, vehicles,
carriers, orders, distance matrices, and supporting dictionary types.
"""

from importlib.metadata import PackageNotFoundError, version

from yunpy.domain.schema import (
    CargoOrder,
    CargoSubOrder,
    CargoSubOrderDimensionValue,
    CargoSubOrderLabelValue,
    Carrier,
    CarrierLabelValue,
    Dimension,
    DistMatrixCode,
    DistMatrix,
    Label,
    LabelApply,
    LabelValue,
    LabelApplyItem,
    Location,
    LocationAvailableVehicle,
    LocationLabelValue,
    Vehicle,
    VehicleModel,
    VehicleModelDimensionValue,
    VehicleModelLabelValue,
    WorkCalendarDaily,
    WorkCalendarWeekly,
    WorkEffect,
    WorkFixed,
)

from yunpy.domain.schema_model import SchemaModel

try:
    __version__ = version("yunpy")
except PackageNotFoundError:  # pragma: no cover
    __version__ = "0.0.0"

__all__ = [
    "__version__",
    # base_dict
    "Dimension",
    "Label",
    "LabelApply",
    "LabelValue",
    "LabelApplyItem",
    # location
    "Location",
    "LocationAvailableVehicle",
    "LocationLabelValue",
    "WorkCalendarDaily",
    "WorkCalendarWeekly",
    "WorkEffect",
    "WorkFixed",
    # vehicle_model
    "VehicleModel",
    "VehicleModelDimensionValue",
    "VehicleModelLabelValue",
    # carrier
    "Carrier",
    "CarrierLabelValue",
    "Vehicle",
    # network
    "DistMatrixCode",
    "DistMatrix",
    # order
    "CargoOrder",
    "CargoSubOrder",
    "CargoSubOrderDimensionValue",
    "CargoSubOrderLabelValue",
    # SchemaModel
    "SchemaModel",
]
