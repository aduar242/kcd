import xml.etree.ElementTree as ET
from googletrans import Translator
import time

# Inisialisasi penerjemah
translator = Translator()

# Baca file XML
tree = ET.parse('c:\\Users\\adu\\Downloads\\Compressed\\English_xml_extracted\\text_ui_dialog.xml')
root = tree.getroot()

# Fungsi untuk menerjemahkan teks dengan penanganan kesalahan
def translate_text(text, src='en', dest='id'):
    try:
        translation = translator.translate(text, src=src, dest=dest)
        return translation.text
    except Exception as e:
        print(f"Error translating text: {text}. Error: {e}")
        return text

# Iterasi melalui elemen dan terjemahkan teks dalam elemen <Cell> setelah ID unik dan teks berikutnya
total_rows = len(root.findall('.//Row'))
print(f"Total rows to translate: {total_rows}")

for row_index, row in enumerate(root.findall('.//Row')):
    cells = row.findall('.//Cell')
    for i in range(2, len(cells)):
        original_text = cells[i].text
        translated_text = translate_text(original_text)
        cells[i].text = translated_text
        time.sleep(0.2)  # Tambahkan jeda waktu 1 detik untuk menghindari batasan API
    print(f"Translated row {row_index + 1} of {total_rows}")

# Simpan hasil terjemahan ke file baru
output_file = 'c:\\Users\\adu\\Downloads\\Compressed\\English_xml_extracted\\text_ui_dialog_translated.xml'
tree.write(output_file, encoding='utf-8', xml_declaration=True)
print(f"Translation completed. Translated file saved as {output_file}")