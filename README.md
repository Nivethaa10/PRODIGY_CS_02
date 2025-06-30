# PRODIGY_CS_02
# 🖼️ Image Encryption using Pixel Manipulation

This is a simple Python project that demonstrates image encryption and decryption using **pixel color inversion**. The technique is based on manipulating RGB values so that each pixel is flipped across the color spectrum. The same operation can be used for both encryption and decryption.

## 🔐 What is Pixel Inversion?

Pixel inversion is done by subtracting each RGB channel value from 255:
```
new_R = 255 - R
new_G = 255 - G
new_B = 255 - B
```
Applying this twice restores the original image:
```
255 - (255 - X) = X
```

---

## 📦 Features

- One-step **encryption and decryption**
- Uses Python’s `Pillow` library
- Simple logic ideal for learning image processing and reversible transformations
- CLI interaction to choose encrypt or decrypt

---

## 🧰 Requirements

- Python 3.x
- Pillow

Install dependencies:
```bash
pip install Pillow
```

---

## 📂 Project Structure

```
📁 pixel-image-encryption/
│
├── image_encryptor.py       # Main Python script
├── original.png             # Input image for encryption
├── encrypted.png            # Output after encryption
├── decrypted.png            # Output after decryption
└── README.md                # Project documentation
```

---

## 🚀 How to Run

### 🔒 To Encrypt:
```bash
python image_encryptor.py
# Choose option 1 when prompted
```

### 🔓 To Decrypt:
```bash
python image_encryptor.py
# Choose option 2 when prompted
```

> Make sure `original.png` or `encrypted.png` is placed in the same folder as the script.

---

## 📸 Sample Flow

- `original.png` ➝ (Encrypt) ➝ `encrypted.png`
- `encrypted.png` ➝ (Decrypt) ➝ `decrypted.png`

---

## 🧠 Educational Use

This project is intended **for educational purposes only**. It shows how simple image manipulation can be used to encrypt and decrypt visual data, but is **not secure for real-world cryptography applications**.

---

