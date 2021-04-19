# dotfiles
mi configuracion de arch en español, qtile


# Arch guia de instalacion (UEFI) :

esta es una guia de instalacion limpia de arch linux en maquinas
uefi, puede que en tu dispositivo tenga errores u otra cosa asi 
que aqui te dejo la santa biblia de arch su **[wiki oficial](https://wiki.archlinux.org/)**   
tambien su **[guia de instalacion](https://wiki.archlinux.org/index.php/Installation_guide_(Espa%C3%B1ol))** 
en español

# -Preinstalacion
primero debiste arrancar el sistema en un live usb o cd, si es 
asi debes estar dentro de una terminal.

vamos por cambiar la distribucion de teclado porque al menos yo
no tengo un teclado gringo.
para un teclado con distrbucion español:
```bash
loadkeys es
```
para uno con dstribucion latinoamericana
```bash
loadkeys la-latin1
```

ahora toca conectarse a internet, vamos a ver si nuestra interfas de 
internet esta abierta con:
```bash
ip link
```
si lo esta tenemos que escribir
```bash
ip link set [tu interfas] up
```
tambien veremos que tu tarjeta wifi no este bloqueada con 
```bash
rfkill list
```
si dice Hard bloqued:yes  es porque esta bloqueada, la desbloqueamos con:
```bash
rfkill unblock wifi
```
Para conectarnos a ua red wifi tenemos que usar iwctl
```bash
iwctl
```
en el escribimos 
```bash
station [tu interfas] connect [el nombre de la red wifi, SSID]
```
nos va a pedir la contraseña de la red y la escribimos, para salir escribimos
exit 
```bash
exit
```
ahora comprobamos que estamos con internet escribiendo
```bash
ping google.com
```
si empieza a transmitir datos es que estamos conectados

Generar locales, para eso vamos a editar el archivo /etc/locale.gen
```bash
nano /etc/locale.gen
```
buscamos y descomentamos el de nuestro pais con utf-8, en mi caso que es 
chile seria:
```bash
de esto: 
# es_CL.UTF-8
a esto:
es_CL.UTF-8
```
ctrl + o para guardar los cambios apretamos enter y ctrl + x para salir,
ahora ejecutamos
```bash
locale-gen
```

Para actualizar el reloj del sistema es con 
```bash
timedatectl set-ntp true
```
comprobamos que este bien 
```bash
timedatectl status
```

Particionar el disco, en esta parte si tienes windows u otro sistema
avansa con cuidado para no cagarla, si quieres tener arch junto con windows 
primero debiste crear una particion desde el admministrador de discos de windows

para crear las particiones de arch vamos a utilizar cfdisk para facilitarnos 
el trabajo y que sea mas facil de entender lo que estamos haciendo
```bash
cfdisk
```
como estamos en uefi vamos a tener que crear una particion (si ya la tienes omites esto),
para ello vamos a movernos a la particion en la que queremos instalar arch, seleccionamos
new y escribimos el tamaño de la particion que son 100mb
```bash 
100M
```
Ahora vamos a crear las particiones para el sistema de Arch, lo recomendable es tener
siquiera 3 particiones, uno para el swap, otro para el raiz / , y uno para el /home. 
Para todas esta particiones vas a tener que decidir tu cuanto le quieres dar, te recomiendo pensar
bien cuanto darle a cada uno. Cuando ya sabes cuanto le quieres dar a cada uno solo tienes que
seleccionar la particion vacia, ir a new y escribir el tamaño de la particion.
Cuando ya tengas las aprticiones para arch ve a Write y escribe:
```bash
yes
```
luego seleccionas Quit para salir
