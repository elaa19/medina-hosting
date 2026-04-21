import sys
from PIL import Image
from collections import Counter

def get_dominant_colors(image_path, num_colors=5):
    try:
        img = Image.open(image_path)
        img = img.convert('RGB')
        
        # Resize to speed up processing
        img = img.resize((100, 100))
        
        pixels = list(img.getdata())
        
        # Filter out white/transparent backgrounds roughly
        filtered_pixels = [p for p in pixels if not (p[0] > 240 and p[1] > 240 and p[2] > 240)]
        
        count = Counter(filtered_pixels)
        dominant = count.most_common(num_colors)
        
        for color, freq in dominant:
            hex_color = '#{:02x}{:02x}{:02x}'.format(color[0], color[1], color[2])
            print(f"{hex_color} (freq: {freq})")
    except Exception as e:
        print("Error:", e)

get_dominant_colors('media logo 1.png')
