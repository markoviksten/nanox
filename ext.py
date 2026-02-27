import os
import shutil

def process_markdown_files(folder_path=r'C:\Users\861100702\Documents\op-ehdot-materiaali\www015.kube.jty.op-palvelut.net_20260119_144713\www015.kube.jty.op-palvelut.net_20260119_144713\pages'):
    """
    Käy läpi kaikki .md tiedostot kansiossa ja kopioi ne uudella nimellä,
    jos kolmas rivi sisältää tietyn URL:n.
    """
    target_url = 'https://www015.kube.jty.op-palvelut.net/osuuspankit/'
    
    # Tarkista että kansio on olemassa
    if not os.path.exists(folder_path):
        print(f"Kansiota '{folder_path}' ei löydy!")
        return
    
    copied_count = 0
    skipped_count = 0
    
    # Käy läpi kaikki tiedostot kansiossa
    for filename in os.listdir(folder_path):
        # Tarkista että tiedosto on .md
        if not filename.endswith('.md'):
            continue
        
        filepath = os.path.join(folder_path, filename)
        
        # Lue tiedoston kolmas rivi
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                
                # Tarkista että tiedostossa on vähintään 3 riviä
                if len(lines) >= 3:
                    third_line = lines[2].strip()  # Indeksi 2 = kolmas rivi
                    
                    # Tarkista sisältääkö kolmas rivi target URL:n
                    if target_url in third_line:
                        # Luo uusi tiedostonimi
                        new_filename = f'scope_{filename}'
                        new_filepath = os.path.join(folder_path, new_filename)
                        
                        # Kopioi tiedosto
                        shutil.copy2(filepath, new_filepath)
                        print(f"✓ Kopioitu: {filename} -> {new_filename}")
                        copied_count += 1
                    else:
                        skipped_count += 1
                else:
                    print(f"⚠ Ohitettu: {filename} (tiedostossa alle 3 riviä)")
                    skipped_count += 1
                    
        except Exception as e:
            print(f"❌ Virhe tiedoston '{filename}' käsittelyssä: {e}")
            skipped_count += 1
    
    print(f"\n--- Yhteenveto ---")
    print(f"Kopioitu: {copied_count} tiedostoa")
    print(f"Ohitettu: {skipped_count} tiedostoa")

if __name__ == '__main__':
    process_markdown_files()