[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.16748203.svg)](https://doi.org/10.5281/zenodo.16748203)
![Visitors Badge](https://visitor-badge.laobi.icu/badge?page_id=RuiGao9.Data_Auto_Transfer)<br>

# Data_Auto_Transfer
## A Python Tool for Data Transfering from the SD Card to Your Field Computer - Data_Auto_Transfer
<p align="center">Rui Gao<sup>1,2</sup>, Mohammad Safeeq<sup>1,2</sup>, Joshua H. Viers<sup>1,2</sup></p>
<sup>1</sup>Department of Civil and Environmental Engineering, University of California Merced, Merced, CA 95343, USA<br>
<sup>2</sup>Valley Institute for Sustainable Technology & Agriculture, University of California Merced, Merced, CA 95343, USA<br>

## Project overview
Field data collection from Eddy-Covariance (EC) flux towers often requires direct access to an SD card—an otherwise straightforward process that can become cumbersome under challenging environmental conditions. While copying the entire dataset is an option, it is time-consuming, often taking up to 10 minutes per session. Moreover, when temperatures soar above 40 °C (with surface temperatures exceeding 50 °C), prolonged exposure in the field is not just uncomfortable—it can be hazardous.<br>
Manually selecting and transferring only the recent data files in such conditions is inconvenient and error-prone. It involves navigating laptop screens under harsh sunlight, finding shade, and carefully managing file selection with unstable gestures—all of which increase the chance of mistakes or incomplete transfers.<br>
To streamline this process, we developed this Python-based tool. All the processes are mainly concentrated in `transfer.py`. It allows researchers to:
1. Specify the SD card source path,
2. Define a target directory on their computer,
3. Choose how many recent days’ worth of data to transfer.

The tool automatically identifies and copies only the relevant files, with intelligent handling of file name collisions—ensuring nothing is lost or overwritten. <br>
This utility enables efficient and reliable data acquisition directly in the field, minimizing human effort and maximizing comfort and productivity, whether you're working under vineyard vines or back in the lab.

## Document description
In this repository, we have three documents:
1. transfer.py – All the process are programed here. 
2. main.ipynb – This Jupyter Notebook allows users to adjust input parameters as needed. After modifying the parameters, simply click `run` to generate results, which will be saved in the designated output folder. Three parameters are described below:
    - `source`: where the data comes from.
    - `destination`: where the data will be saved. 
    - `days`: specifies the number of days of data you want to extract.
3. README.md - which can help you to understand this repository.

## Citation
If you use this repository in your work, please cite it using the following DOI:

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.16748203.svg)](https://doi.org/10.5281/zenodo.16748203)

**BibTeX:**
```bibtex
@misc{gao2025apogee,
  author       = {Rui Gao, Mohammad Safeeq, and Joshua H. Viers},
  title        = {A Python Tool for Data Transfering from the SD Card to Your Field Computer - Data_Auto_Transfer},
  year         = {2025},
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.16748203},
  url          = {https://doi.org/10.5281/zenodo.16748203}
}
```
## Repository update information:
- **Creation date:** 2025-08-05
- **Last update:** 2025-08-05

## Contact information if issues were found:
Rui Gao<br>
Rui.Ray.Gao@gmail.com<br>
RuiGao@UCMerced.edu