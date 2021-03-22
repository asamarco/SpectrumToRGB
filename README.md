# SpectrumToRGB
Python script that displays the approximate color representation of a reflectance spectrum. Based on https://scipython.com/blog/converting-a-spectrum-to-a-colour/

Spectra should cover the range 380-780 nm with a 5 nm step, samples can can be generated here https://www.filmetrics.com/reflectance-calculator?wmin=380&wmax=780&wstep=5&angle=0&pol=mixed&units=nm&mat[]=Air&d[]=0&mat[]=SiO2&d[]=350&mat[]=Si&d[]=0&sptype=r

usage:

python SpectrumToRGB.py spectrum_data.txt
