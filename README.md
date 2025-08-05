[![DOI](https://zenodo.org/badge/452388873.svg)](https://doi.org/10.5281/zenodo.15871796)
![Visitors Badge](https://visitor-badge.laobi.icu/badge?page_id=RuiGao9.Group_Materials)<br>

# Data_Auto_Transfer
## A Python Tool for Data Transfering from the SD Card to Your Field Computer - Data_Auto_Transfer
<p align="center">Rui Gao<sup>1,2</sup>, Mohammad Safeeq<sup>1,2</sup>, Joshua H. Viers<sup>1,2</sup></p>
<sup>1</sup>Department of Civil and Environmental Engineering, University of California Merced, Merced, CA 95343, USA<br>
<sup>2</sup>Valley Institute for Sustainable Technology & Agriculture, University of California Merced, Merced, CA 95343, USA<br>

## Project overview
Field data collection from Eddy-Covariance (EC) flux towers often requires direct access to an SD card—an otherwise straightforward process that can become cumbersome under challenging environmental conditions. While copying the entire dataset is an option, it is time-consuming, often taking up to 10 minutes per session. Moreover, when temperatures soar above 40 °C (with surface temperatures exceeding 50 °C), prolonged exposure in the field is not just uncomfortable—it can be hazardous.<br>
Manually selecting and transferring only the recent data files in such conditions is inconvenient and error-prone. It involves navigating laptop screens under harsh sunlight, finding shade, and carefully managing file selection with unstable gestures—all of which increase the chance of mistakes or incomplete transfers.<br>
To streamline this process, we developed this Python-based tool. It allows researchers to:
1. Specify the SD card source path,
2. Define a target directory on their computer,
3. Choose how many recent days’ worth of data to transfer.

The tool automatically identifies and copies only the relevant files, with intelligent handling of file name collisions—ensuring nothing is lost or overwritten. <br>
This utility enables efficient and reliable data acquisition directly in the field, minimizing human effort and maximizing comfort and productivity, whether you're working under vineyard vines or back in the lab.

## Document description
This repository is designed to generate footprint estimates for Apogee IRT sensors with circular fields of view. Upon completion, the program outputs the results in both GeoTIFF and Shapefile formats.
- Apogee_IRT_Footprint.pdf – This document provides a detailed explanation of the footprint calculation method and associated parameters.
- main.ipynb – This Jupyter Notebook allows users to modify input parameters as needed. It also includes explanations of the input variables and their meanings.

## Citation
If you use this repository in your work, please cite it using the following DOI:

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.16581912.svg)](https://doi.org/10.5281/zenodo.16581912)

**BibTeX:**
```bibtex
@misc{gao2025apogee,
  author       = {Rui Gao, Mohammad Safeeq, and Joshua H. Viers},
  title        = {A Python Tool for Apogee IRT Sensor Footprint Generation and Georeferencing – Apogee_IRT_Footprint},
  year         = {2025},
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.16581912},
  url          = {https://doi.org/10.5281/zenodo.16581912}
}
```
## Repository update information:
- **Creation date:** 2025-07-11
- **Last update:** 2025-07-29

## Contact information if issues were found:
Rui Gao<br>
Rui.Ray.Gao@gmail.com<br>
RuiGao@UCMerced.edu