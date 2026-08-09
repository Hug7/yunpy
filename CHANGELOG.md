# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] — Unreleased

### Added

- Domain schema dataclasses for logistics optimization:
  - `Dimension`, `Label`, `LabelValue`, `LabelApply` (base dictionaries)
  - `Location`, `LocationLabelValue`, `LocationAvailableVehicle`, `WorkCalendarDaily`, `WorkCalendarWeekly`, `WorkFixed`, `WorkEffect` (location)
  - `VehicleModel`, `VehicleModelDimensionValue`, `VehicleModelLabelValue` (vehicle models)
  - `Carrier`, `CarrierLabelValue`, `Vehicle` (carriers)
  - `DistMatrix` (route network)
  - `CargoOrder`, `CargoSubOrder`, `CargoSubOrderDimensionValue`, `CargoSubOrderLabelValue` (orders)
- Concise `__repr__` for all domain models
- Package-level `__version__` via `importlib.metadata`
- `py.typed` marker for PEP 561 compliance
- Poetry-based build with mypy, ruff, and pytest dev tooling
- GitHub Actions CI (lint, typecheck, test on 3.11/3.12/3.13)

[0.1.0]: https://github.com/yunpy-contributors/yunpy/releases/tag/v0.1.0
