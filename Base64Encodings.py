#!/usr/bin/env python3


# THIS TOOL OR PROGRAM USING INDONESIA LANGUAGE.
# SUMBER: https://docs.python.org/3/library/base64.html
# Base16, Base32, Base64, Base85 Data Encodings


# Kode Oleh: Ruben Leonardo Sigalingging.
# Dibuat Pada: Kamis, 17 Juni 2022, Pukul 00:18 PM.
# Menggunakan: Bahasa Pemrogramman Python Versi 3.8.10


# Langkah Pertama Buat fungsi, lalu import semua module yang diperlukan.
def base64_encodings(code_by="Ruben Leonardo Sigalingging."):
	from os import system
	# Izin File
	system("clear")
	system("chmod 777 Base64Encodings.py")
	from pyfiglet import figlet_format
	from time import time, sleep
	from sys import exit
	import base64


	tema = figlet_format("Base64",font="slant")
	print(tema)
	print("[!] Kode Oleh: Ruben Leonardo Sigalingging.")
	print("[!] Dibuat Pada: Kamis, 17 Juni 2022, Pukul 00:18 PM.")
	print("[!] Menggunakan: Bahasa Pemrogramman Python Versi 3.8.10")
	print("[!] Program: Base64 Encodings")
	print("\n")


	waktu_awal_pengkodean = time()
	pesan_atau_kata_sandi = input("[!] Pesan atau Kata Sandi: ")
	enkode_ke_ascii = pesan_atau_kata_sandi.encode("ascii")
	dikodekan = base64.b64encode(enkode_ke_ascii)
	dekode_ke_ascii = dikodekan.decode("ascii")
	print(f"[!] Pengkodean Base64 Dari {pesan_atau_kata_sandi}: {dekode_ke_ascii}")
	waktu_akhir_pengkodean = time()
	print(f"[!] Total Waktu Pengkodean: {waktu_akhir_pengkodean - waktu_awal_pengkodean}")
	print("\n")


	jawaban="Y"
	pertanyaan=input("[!] Ingin Menyimpan Hasil Base64Encodings?\n[!] Y/n: ")
	if pertanyaan == "Y" or pertanyaan == "y" or pertanyaan == "yes" or pertanyaan == "ya":
		hasil_pengkodean_base64 = open("Base64EncodingResult.txt", "w")
		hasil_pengkodean_base64.write("PlainText: ")
		hasil_pengkodean_base64.write(pesan_atau_kata_sandi)
		hasil_pengkodean_base64.write("\n")
		hasil_pengkodean_base64.write("Base64 Encoding Result: ")
		hasil_pengkodean_base64.write(dekode_ke_ascii)
		hasil_pengkodean_base64.write("\n")


	elif pertanyaan == "N" or pertanyaan == "n" or pertanyaan == "no" or pertanyaan == "No":
		from os import system
		from time import sleep
		print("[!] Sampai Jumpa!")
		sleep(8)
		system("clear")
		from sys import exit
		exit(1)


	else:
		print("[!] Pilih Dengan Benar!")
base64_encodings()