import os

def get_image_names(folder_path):
    image_names = set()
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            image_names.add(filename)
    return image_names

def find_missing_images(images_folder, processed_folder):
    images_set = get_image_names(images_folder)
    processed_set = get_image_names(processed_folder)
    
    missing_images = images_set - processed_set
    return missing_images

if __name__ == "__main__":
    images_folder = "C:/Users/petros/Documents/platerecognizer/images"  # Ersetzen Sie dies durch den tatsächlichen Pfad zu Ihrem 'images'-Ordner
    processed_folder = "C:/Users/petros/Documents/platerecognizer/processed"  # Ersetzen Sie dies durch den tatsächlichen Pfad zu Ihrem 'processed'-Ordner
    
    missing_images = find_missing_images(images_folder, processed_folder)
    print(f"Anzahl fehlender Bilder: {len(missing_images)}")
    print("Fehlende Bilder:")
    for image_name in missing_images:
        print(image_name)
