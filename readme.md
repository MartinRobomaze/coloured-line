# IYPT 2023 Coloured line
This repository is a partial solution for problem IYPT problem number 4. It consists of 4 main directories:

- `angle_measurer` - Code for angle measuring device used in the experimental setup (Arduino + MPU6050), 
- `data` - Contains all experimental data (only processed csv files),
- `data_processing` - Contains jupyter notebook where data is processed and graphs are generated,
- `image_processor` - Python script which contains images from spectrometer to `csv` formatted data.

### Measurement of CD diffraction spectrum
A home-made spectrometer was used for measuring diffraction spectrum of CD/DVD drives. The spectrometer used a diffraction grating and a ZWO ASI120 MC camera. The body was 3D printed and its 3D model is in `spectrometer_model` directory. Images were then converted to csv-formatted data using a Python script in `image_processor` directory.
### What is done
* Measurements of CD diffraction spectra under different vertical observer angles (light source and specrometer were in the same plane),
* Measurements of CD diffraction spectra under different horizontal angles (light source and spectromer not in the same plane),
* Measurements of DVD diffraction spectra under different vertical observer angles,
* Comparison between measurements of diffr. spectra under various vertical observer angles with planar diffraction theory.
### What needs to be done
* Better theoretical model for conical diffraction (model + explanation),
* Explanation why only a coloured line is seen.

This presentation is partially based on presentations from the [Slovak YPT introductory meetup](tmfsr.sk/sk/aktuality/227) (presentations in slovak).

This work is licensed under a
[Creative Commons Attribution 4.0 International License][cc-by].

[![CC BY 4.0][cc-by-image]][cc-by]

[cc-by]: http://creativecommons.org/licenses/by/4.0/
[cc-by-image]: https://i.creativecommons.org/l/by/4.0/88x31.png
[cc-by-shield]: https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg
