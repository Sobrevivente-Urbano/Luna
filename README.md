# Projeto-Luna

```
sudo apt update -y
sudo apt upgrade -y

sudo apt-get install curl nmap jq net-tools git unzip \
unrar youtube-dl ffmpeg ntpdate clamav clamav-daemon python3-pip --no-install-recommends -y

pip3 install pylint
pip3 install autopep8
pip3 install youtube-dl
pip3 install BeautifulSoup4
pip3 install python-aiml
pip3 install lxml
pip3 install GoogleNews
pip3 install wikipedia

sudo mkdir /etc/luna
sudo chmod 777 -R /etc/luna

sudo mkdir /etc/luna/tmp
sudo chmod 777 -R /etc/luna/tmp

sudo cp -RF ./* /etc/luna

sudo chmod +x /etc/luna/*
sudo chmod 777 -R /etc/luna/*

sudo ln -s /etc/luna/banner /usr/bin/banner
sudo ln -s /etc/luna/bkp /usr/bin/bkp
sudo ln -s /etc/luna/disco /usr/bin/disco
sudo ln -s /etc/luna/dispositivos /usr/bin/dispositivos
sudo ln -s /etc/luna/luna /usr/bin/luna
sudo ln -s /etc/luna/myip /usr/bin/myip
sudo ln -s /etc/luna/tempo /usr/bin/tempo
sudo ln -s /etc/luna/antivirus /usr/bin/antivirus
sudo ln -s /etc/luna/FUSB /usr/bin/FUSB
sudo ln -s /etc/luna/global /usr/bin/global
sudo ln -s /etc/luna/infosys /usr/bin/infosys
sudo ln -s /etc/luna/checkdns /usr/bin/checkdns
sudo ln -s /etc/luna/firewall /usr/bin/firewall
sudo ln -s /etc/luna/jailsys /usr/bin/jailsys
sudo ln -s /etc/luna/limpar /usr/bin/limpar
sudo ln -s /etc/luna/matematica /usr/bin/matematica
sudo ln -s /etc/luna/syncTime /usr/bin/syncTime
sudo ln -s /etc/luna/ytmp3 /usr/bin/ytmp3
sudo ln -s /etc/luna/ytmp4 /usr/bin/ytmp4
```

```
# Iniciar

$ luna
```

Comandos
```
IP
Rede
HD
TEMPO
CLIMA
KERNEL
OS
News *tema
news *tema
CLEAR
CLS
```

*Novas Funções
```
hora
abrir porta 33 TCP
fechar porta 33 TCP
quanto é 1 + 1 
quanto é 1 - 1
quanto é 1 * 1
quanto é 1 / 1
```

* Outros/Complementos
```
Baixar mp3 e mp4 do Youtube
$ ytmp3 URL_Youtube
$ ytmp4 URL_Youtube

Atualizar hora do Sistema
$ syncTime

Informações sobre o Sistema
$ infosys

Ver IP Externo
$ myip

Formatar Pendrive sem permições de diretorios/arquivos
$ FUSB

Hora Global 
$ global

Antivirus
$ antivirus


```
