# Nightingale

A python library for statistical and scientific computations.

## Description

Nightingale is a statistical and scientific computational library that offers high-level
features including but not limited to:
- Sampling functionality
- Basic computations

Planned features:
- Regression algorithms
  - Linear
  - Logistic
- The dataset object
- Probability Statistical Analysis

## Table of Contents

<!-- toc -->

- [Installation](#installation)
- [Usage](#usage)
- [Release Notes](#release-notes)
  - [0.1](#01)
- [Contributing](#contributing)
- [Credits](#credits)
- [License](#license)

<!-- tocstop -->

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install nightingale.

```bash
pip install nightingale
```

## Usage

```python
import nightingale as ng

# returns mean of the dataset
ng.mean(data_set=saturn_moon_radii)

# a sample of 10 of Saturn's moon's radii
ng.rand_sample(data_set=saturn_moon_radii, 10)
```

## Release Notes

### 0.1

#### Initial Release
- Code base is implemented
- Sampling methods introduced using the numpy.ndarray object type
  - Simple Random Sampling
  - Systematic Random Sampling
- Basic measures of centeral tendency implemented.
  - Mean
  - Median

#### 0.1.1
 - Updated README to reflect the nature of the project.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Credits

### Robb Northrup

- [Github](https://github.com/NorthrupRobert)
- Email: RobbNorthrup@outlook.com


## License
[MIT](https://choosealicense.com/licenses/mit/)
