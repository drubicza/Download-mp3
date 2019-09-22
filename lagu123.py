"""
- Mau Ngapain onta Lihat" Script sederhana ini
- mau di bongkar Ya dan mau di RECODE YA begituh
- seperti script Tools yang kemarin saya buat dengan menggunakan BASH
- pass Gua lihat di Youtube / Sosial Media dll
- di RECODE DAN tidak rapih dan isinya Apa saja,
- begitu menurut Anda iyakan
- saya, juga Tau Onta!
-
- jadi Gini onta
- jika anda sudah tau bahasa python python2 python3 Bash C++ dll
- maka silahkan onta buat script sendiri Tidak usah Nge recode script orang Lain
- itu Tidak baik onta Tidak Malu ya
- jika Anda belum tau bahasa yang saya sebutkan
- tinggal pakai saja script sederhana ini susah Amat Lu
-
- NOTE :
- jangan di jual belikan script sederhana ini Okey
- ke teman" Anda maupun orang yang tidak di kenal
-
- Menurut Gua, silahkan bagikan script sederhana ini
- ke teman" Anda dan orang yang tidak di kenal juga
- biar Aman onta!!
-     <{ ---BERBAGI ITU INDAH--- }>

- NOTE :
- Ngoding itu simple onta itu Menurut saya,
- Tidak tau Menurut Anda!
- yang penting sudah Tau bahasa segitu apa susahnya... !
"""
import random, sys, wget, os, time, requests
from bs4 import BeautifulSoup
from time import sleep
GL = '\x1b[96;1m'
BB = '\x1b[34;1m'
YY = '\x1b[33;1m'
GG = '\x1b[32;1m'
RR = '\x1b[31;1m'
CC = '\x1b[36;1m'
B = '\x1b[34m'
Y = '\x1b[33;1m'
G = '\x1b[32m'
W = '\x1b[0;1m'
R = '\x1b[31m'
C = '\x1b[36;1m'

def tik(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.06)


rs = requests.Session()

def search():
    global url
    os.system('clear')
    print('')
    print('\x1b[0;1m+\x1b[34m---------------------------\x1b[0;1m+')
    print('\x1b[34m|\x1b[32mAuthor  : \x1b[0;1mMEiZU_M5         \x1b[34m|')
    print('\x1b[34m|\x1b[32mYoutube : \x1b[0;1mEdi ID           \x1b[34m|')
    print('\x1b[34m|\x1b[32mFacebook: \x1b[0;1mEdi Garsell      \x1b[34m|')
    print('\x1b[0;1m+\x1b[34m---------------------------\x1b[0;1m+\x1b[36;1m')
    os.system('date')
    print('')
    print('\x1b[34m--------------------------')
    print('\x1b[0;1m[\x1b[31m+\x1b[0;1m]\x1b[32m MENU\x1b[0;1m:')
    print('\x1b[34m--------------------------')
    print('\x1b[0;1m[\x1b[31m1\x1b[0;1m]\x1b[32m Download Musik Mp3')
    print('\x1b[0;1m[\x1b[31m2\x1b[0;1m]\x1b[32m Download Musik Terbaru')
    print('\x1b[0;1m[\x1b[31m0\x1b[0;1m]\x1b[32m \x1b[31mExit')
    print('\x1b[34m--------------------------')
    print('\x1b[0;1m[\x1b[31m+\x1b[0;1m]\x1b[32m Masukkan Nomornya\x1b[0;1m:')
    pilih = input('\x1b[0;1m=\x1b[31m>\x1b[0;1m: ')
    if pilih == '1' or pilih == '01':
        os.system('clear')
        print('')
        print('')
        print('')
        tik('\x1b[32mMASUKKAN NAMA LAGU KE KOTAK PENCARIAN ')
        sleep(2)
        tik('\x1b[32mUNTUK DOWNLOAD LAGU YANG ')
        sleep(2)
        tik('\x1b[32mANDA INGINKAN\x1b[31m...')
        sleep(1)
        print('\x1b[34m--------------------------------------')
        print('\x1b[0;1m[\x1b[31m+\x1b[0;1m]\x1b[32m Masukkan judul Musik\x1b[0;1m:')
        cari = input('\x1b[0;1m=\x1b[31m>\x1b[0;1m: ')
        os.system('clear')
        print('')
        print('')
        tik('\x1b[32mSEDANG MEMBUKA LiST MUSIK MP3\x1b[31m...')
        sleep(4)
        os.system('clear')
        print('')
        url = 'https://lagu123.mobi/search.html?q=' + cari
        print('')
        print('\x1b[34m----------------------------------------')
        print('\x1b[36;1m   Download Lagu Terbaru Gratis, Gudang')
        print('\x1b[36;1m       lagu Mp3 Terbaik 2019')
        print('\x1b[34m----------------------------------------')
    elif pilih == '2' or pilih == '02':
        os.system('clear')
        url = 'https://lagu123.mobi/download-lagu-terbaru.html'
        os.system('clear')
        print('')
        print('')
        tik('\x1b[32mSEDANG MEMBUKA LiST MUSIK MP3\x1b[31m...')
        sleep(4)
        os.system('clear')
        print('')
        print('\x1b[34m----------------------------------------')
        print('\x1b[36;1m   Download Lagu Terbaru Gratis, Gudang')
        print('\x1b[36;1m       lagu Mp3 Terbaik 2019')
        print('\x1b[34m----------------------------------------')
    elif pilih == '0' or pilih == '00':
        print('')
        tik('\x1b[32mBY\x1b[31m.. \x1b[32mBY\x1b[31m...')
        sleep(1)
        tik('\x1b[32mjangan Lupa Tinggalkan jejak ya')
        sleep(2)
        tik('\x1b[32mCaranya dengaN cara')
        sleep(2)
        tik('\x1b[32mKlik Like share And subcribe')
        sleep(2)
        tik('\x1b[32mVideo Channel \x1b[0;1mEdi ID')
        sleep(2)
        tik('\x1b[32mTerima Kasih\x1b[31m...\x1b[0;1m')
        sleep(2)
        sys.exit()
    else:
        print('')
        tik('\x1b[32mMasukkan pilihan Anda tidak terdaftar')
        sleep(2)
        tik('\x1b[32msilahkan Masukkan dengan benar')
        sleep(2)
        tik('\x1b[32mTerima Kasih\x1b[31m...')
        (os.execl)(sys.executable, sys.executable, *sys.argv)


def main():
    os.system('clear')
    search()
    r = rs.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    ulang = 0
    for lagu in soup.find_all('div', class_='detail-info'):
        ulang += 1
        for judul in lagu.findChildren('a'):
            print('\x1b[0;1m[\x1b[31m' + str(ulang) + '\x1b[0;1m]\x1b[32m', judul.text)


def lagu(x):
    global URL
    global nama
    os.system('clear')
    r = rs.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    ulang = 0
    for lagu in soup.find_all('div', class_='detail-info'):
        ulang += 1
        if ulang == x:
            for judul in lagu.findChildren('a'):
                nama = judul.text + '.mp3'
                URL = 'https://lagu123.mobi' + judul.get('href')
                break


def link():
    global URL1
    main()
    print('\x1b[34m----------------------------------------')
    print('\x1b[0;1m[\x1b[31m+\x1b[0;1m]\x1b[32m Masukkan judul Musik\x1b[0;1m: ')
    pil = input('\x1b[0;1m=\x1b[31m>\x1b[0;1m: ')
    lagu(int(pil))
    down = rs.get(URL)
    soup = BeautifulSoup(down.content, 'html.parser')
    for lagu1 in soup.find_all('div', class_='bh-audio'):
        for download in lagu1.findChildren('source'):
            URL1 = 'https://lagu123.mobi' + download.get('src')


def download():
    link()
    print('')
    print('\x1b[0;1m+\x1b[34m---------------------------------------\x1b[0;1m+')
    print('\x1b[34m|     \x1b[32mSedang Download Mp3\x1b[31m...            \x1b[34m|')
    print('\x1b[0;1m+\x1b[34m---------------------------------------\x1b[0;1m+')
    try:
        os.makedirs('/data/data/com.termux/files/home/storage/shared/Download MP3')
    except OSError:
        pass

    wget.download(URL1, '/data/data/com.termux/files/home/storage/shared/Download MP3/' + nama)
    tik('\x1b[32m\nSukses Musik Mp3 telah di download')
    sleep(2)
    print('')
    tik('\x1b[32mNote\x1b[0;1m:')
    sleep(2)
    tik('\x1b[32mUntuk Musiknya telah tersimpan')
    sleep(2)
    tik('\x1b[32mke Folder \x1b[0;1mDownload MP3')
    sleep(2)
    tik('\x1b[32msilahkan Cari Folder \x1b[0;1mDownload MP3')
    sleep(2)
    tik('\x1b[32mdi penyimpanan internal Hp Anda')
    sleep(2)
    tik('      \x1b[32mTerima kasih\x1b[31m... \x1b[0;1m^_^')
    sleep(2)
    print('\x1b[34m----------------------------------------')
    sleep(4)
    (os.execl)(sys.executable, sys.executable, *sys.argv)


if __name__ == '__main__':
    download()
