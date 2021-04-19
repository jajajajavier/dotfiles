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
si en el 2° dice DOWN es porque esta bloqueada y tendremos que escribir
```bash
ip link set [tu interfas] up
```
Si tienes internet mediante cable de red con tenerlo conectado basta,
comprueba que tienes internet con:
```bash
ping google.com
```
pero si usas wifi tendras que hacer los sigientes procesos. 

veremos que tu tarjeta wifi no este bloqueada con 
```bash
rfkill list
```
si dice Hard bloqued:yes  es porque esta bloqueada, la desbloqueamos con:
```bash
rfkill unblock wifi
```
Para conectarnos a una red wifi tenemos que usar iwctl
```bash
iwctl
```
en el escribimos 
```bash
station [tu interfas] connect [el nombre de la red wifi, el SSID]
```
nos va a pedir la contraseña de la red y la escribimos, para salir escribimos
exit 
```bash
exit
```
ahora comprobamos que tenemos acceso a internet escribiendo
```bash
ping google.com
```
si empieza a transmitir datos es que estamos correctamente conectados,
si sale *fallo temporal en la resolucion del nombre* entonces hay un error
y tendremos que comprobar nuevamente que esten desbloqueadas tu interfas y 
la tarjeta wifi ademas de volver a intentar la conexion a la red wifi 
mediante iwctl, si sige con error te recomiendo leer la info de la wiki

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
avanza con cuidado para no cagarla, si quieres tener arch junto con windows 
primero debiste crear una particion desde el admministrador de discos de windows

para crear las particiones de arch vamos a utilizar cfdisk para facilitarnos 
el trabajo y que sea mas facil de entender lo que estamos haciendo
```bash
cfdisk
```
como estamos en uefi vamos a tener que crear una particion EFI (si ya la tienes omites esto),
para ello vamos a movernos a la particion en la que queremos instalar arch, seleccionamos
new y escribimos el tamaño de la particion que son 260mb
```bash 
260M
```
Ahora vamos a crear las particiones para el sistema de Arch, lo recomendable es tener
siquiera 3 particiones, uno para el swap, otro para el raiz / , y uno para el /home. 
Para todas esta particiones vas a tener que decidir tu cuanto le quieres dar, te 
recomiendo pensar bien cuanto darle a cada uno. Cuando ya sabes cuanto le quieres 
dar a cada uno solo tienes que seleccionar la particion vacia del disco, ir a new 
y escribir el tamaño de la particion. Cuando ya tengas las particiones para arch ve 
a Write y escribe:
```bash
yes
```
listo las particiones ya estan echas, recuerda o anota el numero de cada una, por ejemplo
si la particion para el swap la quieres en /dev/sda2 recuerda ese 2, lo mismo para las demas

luego seleccionas Quit para salir de cfdisk

Ya tenemos las particiones, ahora solo falta formatearlas y darles un formato,
para la particion UEFI (en caso de que la creaste) tenemos que darle un formato  de
FAT32 y para eso escribimos:            
""la X representa el numero de tu particion""
```bash
mkfs.fat -F32 /dev/sdaX
```
ahora para darle formato y formatear el raiz / y el /home se ocupa el formato .ext4
de tal manera
```bash
mkfs.ext4 /dev/sdaX
```
tienes que escribir eso con ambas.                                                             
Y para la particion swap le tenemos que decir al sistema que tal particion va a ser
para el swap con:
```bash
mkswap /dev/sdaX
```
y la activamos
```bash
swapon /dev/sdaX
```
Ahora montamos las particiones en sus respectivos directorios.                                
la particion raiz / tiene que ir montada en /mnt
```bash
mount /dev/sdaX /mnt
```
la particion uefi la vamos a colocar en /boot/EFI,                                      
primero creamos el directorio con 
```bash
mkdir /mnt/boot/EFI
```
y ahora lo montamos en este
```bash
mount /dev/sdaX /mnt/boot/EFI
```
para montar el /home primero se debe crear su directorio con
```bash
mkdir /mnt/home
```
y lo montamos hay 
```bash
mount /dev/sdaX /mnt/home
```
Listo :) ya tienes montadas las particiones, ahora solo falta instalar el sistema
y configurarlo 

# -Instalacion

llegamos a la parte de instalar el sistema
primero vamos a instalar el sistema base, vamos a instalar los sigientes
paquetes                                                                                    
base : instala el sistema base
linux : instala el kernel
linux firmware : instala el firmware XD
base-devel : otras utilidades importantes
```bash
pacstrap /mnt base linux linux-firmware base-devel
```
