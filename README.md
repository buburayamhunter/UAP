# DETEKSI KERUSAKAN PADA KARDUS

## Link dataset (Full)
- [object_detection_cardboard](https://drive.google.com/drive/folders/1Tzz94XEyqiADfEdvweKMCBZbdsS6KG6h?usp=sharing)

## Alur pengerjaan
- *split* setiap fitur yang akan dipakai menggunakan [split_dataset.ipynb](split_dataset.ipynb). Hasil split akan di simpan dalam format numpy (.npz) pada folder [split_data](numpy_files/split_data) yang ada di folder [numpy_files](numpy_files). Selain itu hasil dari split juga akan disimpan dalam bentuk *image* pada folder [images-split-data](images-split-data).
- Melakukan *train* dataset dengan algoritma CNN [svm_model.ipynb](svm_model.ipynb). Karena penggunaan CNN terbatas, maka hanya bisa melakukan klasifikasi kardus.


## `Folder: `
| Nama                                   | Isi                                                                                           |
| -------------------------------------- | --------------------------------------------------------------------------------------------- |
| [split-data](split-data)               | Berisi *image* setiap feature yang telah di *split*                                           |
| [numpy_files](numpy_files)             | Berisi file numpy (.npy) yang mana berisi dataset yang siap dipakai untuk keperluan mendatang |

## `Files: `
| Nama                                                 | Isi                                                                          |
| ---------------------------------------------------- | ---------------------------------------------------------------------------- |
| [dataset.csv](dataset.csv)                           | Berisi dataset dari hasil export `Label-Studio`                              |
| [cnn_model.ipynb](cnn_model.ipynb)           | Training menggunakan CNN                                                |
| [vgg_model.ipynb](vgg_model.ipynb)                   | Training menggunakan model VGG        |
| [streamlit.py](streamlit.py)   | User interface web |


---
