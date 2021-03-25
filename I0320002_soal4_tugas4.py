usia = int(input("Berapa umurmu: "))
if usia >= 21:
    syarat = str(input("Apakah Anda sudah lulus ujian kualifikasi (Y/T)? "))
    if syarat == "Y" or 'y':
        print("Anda dapat mendaftar di kursus")
    elif syarat == "T" or 't':
        print("Anda tidak dapat mendaftar di kursus")