# 🔐 My_Encryption

This repository contains a simple character-level **substitution cipher** written in Python. It allows you to **encrypt** and **decrypt** messages using a randomly shuffled key based on punctuation, digits, and ASCII letters.

## 🧠 How It Works

The script performs basic encryption and decryption:
- A character list `chars` is created using punctuation, digits, and letters.
- A random shuffled copy of this list is used as the **encryption key**.
- Each character in the message is substituted based on the index from `chars` to the corresponding index in the shuffled `key`.

## 🔧 Features

- Encrypt any string message.
- Decrypt using the same shuffled key.
- Uses basic Python libraries: `random` and `string`.
```

## 📂 Code Overview

- `chars` – List of allowed characters.
- `key` – Shuffled version of `chars` used as the encryption key.
- `plain_text` – Input message to encrypt.
- `cipher_text` – Encrypted message.

```
## ⚠️ Limitations

- The encryption key is not saved or shared automatically; the same session must be used for decryption.
- Only works on characters present in `string.punctuation`, `string.digits`, and `string.ascii_letters`.

## 📜 License

This project is licensed under the MIT License. Feel free to use, modify, and share!
