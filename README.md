# Parallelepiped Geometry Calculator

## Overview

This Python project calculates various geometric properties of parallelepiped (rectangular cuboid) shapes using their side lengths. The application reads a JSON file containing dimensions of multiple parallelepiped figures and computes their geometric characteristics.

## Features

The calculator provides the following geometric calculations for each parallelepiped:

- Diagonal length
- Volume
- Surface area
- Angle calculations (alpha, beta, gamma)
- Radius of circumscribed sphere
- Volume of circumscribed sphere

## Project Structure

- `functions.py`: Contains mathematical functions for geometric calculations
- `main.py`: Main script for processing parallelepiped data
- `parallelepipeds.json`: Input file with parallelepiped dimensions
- `response.json`: Output file with calculated geometric properties

## Requirements

- Python 3.x
- `math` module (standard library)
- `json` module (standard library)
- `pathlib` module (standard library)

## How It Works

1. The input JSON file (`parallelepipeds.json`) contains parallelepiped dimensions with keys like "a", "b", and "c" representing side lengths.
2. The script reads these dimensions and calculates various geometric properties.
3. Results are saved in a formatted JSON file (`response.json`).

## Installation

1. Clone the repository
```bash
git clone https://github.com/yourusername/parallelepiped-calculator.git
cd parallelepiped-calculator
```

2. Ensure you have Python 3.x installed

## Usage

Run the main script:
```bash
python main.py
```

## Calculation Details

### Geometric Properties Calculated

- **Diagonal**: Length of the diagonal connecting opposite corners
- **Volume**: Product of three side lengths
- **Surface Area**: Total area of all six faces
- **Angles**: Spherical angles between sides
- **Circumscribed Sphere**: Smallest sphere that contains the parallelepiped

## Example Output

Each figure in the `response.json` will have properties like:
```json
{
    "diag": 23.49,
    "volume": 2240.0,
    "surface_area": 1048.0,
    "alpha": 47.08,
    "beta": 64.81,
    "gamma": 53.42,
    "radius_described_sphere": 11.75,
    "volume_described_sphere": 6790.59
}
```



## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request
