import pandas as pd
from sqlalchemy import create_engine, text
import sys
from pathlib import Path

# Konfiguraatio
EXCEL_FILE = "test.xlsx"  # Vaihda tähän Excel-tiedostosi nimi
DB_CONFIG = {
    "database": "testdb",
    "hostname": "localhost",
    "port": "50000",
    "uid": "db2inst1",
    "pwd": "YourStrongPassword123"
}

def sanitize_table_name(name):
    """Muuta tabin nimi DB2-yhteensopivaksi taulun nimeksi"""
    sanitized = "".join(c if c.isalnum() or c == "_" else "_" for c in name)
    return sanitized.upper()[:128]

def sanitize_column_name(name):
    """Muuta sarakkeen nimi DB2-yhteensopivaksi"""
    sanitized = "".join(c if c.isalnum() or c == "_" else "_" for c in str(name))
    return sanitized.upper()[:128]

def main():
    if not Path(EXCEL_FILE).exists():
        print(f"❌ Virhe: Tiedostoa '{EXCEL_FILE}' ei löydy!")
        sys.exit(1)
    
    print(f"📊 Luetaan Excel-tiedostoa: {EXCEL_FILE}")
    
    try:
        excel_file = pd.ExcelFile(EXCEL_FILE)
    except Exception as e:
        print(f"❌ Virhe Excel-tiedoston lukemisessa: {e}")
        sys.exit(1)
    
    print(f"📑 Löydettiin {len(excel_file.sheet_names)} tabia: {excel_file.sheet_names}")
    
    print("\n🔌 Yhdistetään DB2:een...")
    
    # Connection string for ibm_db_sa
    conn_str = (
        f"db2+ibm_db://{DB_CONFIG['uid']}:{DB_CONFIG['pwd']}@"
        f"{DB_CONFIG['hostname']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}"
    )
    
    try:
        engine = create_engine(conn_str)
        # Testaa yhteys
        with engine.connect() as connection:
            result = connection.execute(text("SELECT 1 FROM SYSIBM.SYSDUMMY1"))
            result.fetchone()
        print("✅ Yhteys muodostettu!\n")
    except Exception as e:
        print(f"❌ Virhe yhdistämisessä: {e}")
        print("\nTarkista että DB2 on käynnissä:")
        print("  podman ps | grep db2")
        sys.exit(1)
    
    # Käsittele jokainen tabi
    for sheet_name in excel_file.sheet_names:
        print(f"\n📋 Käsitellään tabia: '{sheet_name}'")
        
        try:
            df = pd.read_excel(excel_file, sheet_name=sheet_name)
            
            if df.empty:
                print(f"  ⚠️  Tabi on tyhjä, ohitetaan")
                continue
            
            print(f"  📊 Rivejä: {len(df)}, Sarakkeita: {len(df.columns)}")
            
            # Sanitoi sarakkeiden nimet
            df.columns = [sanitize_column_name(col) for col in df.columns]
            
            # Luo taulun nimi
            table_name = sanitize_table_name(sheet_name)
            
            # Poista vanha taulu jos on olemassa
            try:
                with engine.connect() as connection:
                    connection.execute(text(f"DROP TABLE {table_name}"))
                    connection.commit()
                print(f"  ⚠️  Poistettu vanha taulu: {table_name}")
            except:
                pass
            
            # Luo taulu ja lisää data
            df.to_sql(
                table_name, 
                engine, 
                if_exists='replace',
                index=False,
                chunksize=1000
            )
            
            print(f"  ✅ Luotu taulu: {table_name}")
            print(f"  ✅ Lisätty {len(df)} riviä tauluun: {table_name}")
            
        except Exception as e:
            print(f"  ❌ Virhe tabin käsittelyssä: {e}")
            import traceback
            traceback.print_exc()
            continue
    
    print("\n\n🎉 Valmis! Kaikki tabit tuotu DB2:een.")

if __name__ == "__main__":
    main()