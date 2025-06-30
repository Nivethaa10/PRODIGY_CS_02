from PIL import Image

def encrypt_image(input_file, output_file):
    img = Image.open(input_file)
    img = img.convert("RGB")
    pixels = img.load()

    for x in range(img.width):
        for y in range(img.height):
            r, g, b = pixels[x, y]
            pixels[x, y] = (255 - r, 255 - g, 255 - b)

    img.save(output_file)
    print(f"Encrypted image saved as {output_file}")

def decrypt_image(input_file, output_file):
    # Same operation decrypts, since (255 - (255 - X)) = X
    encrypt_image(input_file, output_file)
    print(f"Decrypted image saved as {output_file}")

if __name__ == "__main__":
    print("1. Encrypt Image")
    print("2. Decrypt Image")
    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        encrypt_image("original.png", "encrypted.png")
    elif choice == "2":
        decrypt_image("encrypted.png", "decrypted.png")
    else:
        print("Invalid choice. Exiting.")
