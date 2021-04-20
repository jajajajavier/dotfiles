# Dotfiles
mi configuracion de arch en español, qtile

# Mi configuracion 
**[aqui]()** te dejo mi configuracion de arch linux 
con qtile un gestor de ventanas

# Arch guia de instalacion (UEFI) :
- [Preinstalacion](#-Preinstalacion)
- [Instalacion](#-Instalacion)
- [configurar](#-Configurar-arch)
- [Post instalacion](#-Post-instalacion)

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
si dice DOWN es porque esta bloqueada y tendremos que escribir
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
tienes que escribir eso con ambas particiones.                                                             
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
si tienes un internet tercermundista como yo de 300kbs de descarga                    
esto va a tener para rato, haci que levantate de esa silla                             
muevete un poco y come algo :)                                                

# -Configurar arch

debemos generar el archivo fstab, para ello lo hacemos con:
```bash
genfstab -U /mnt >> /mnt/etc/fstab
```
comprobamos que todo este en orden 
```bash
cat /mnt/etc/fstab
```
hay leemos que cada particion este con su respectivo directorio.     
Ahora entramos dentro de arch como root
```bash
arch-chroot /mnt
```
Ahora que estamos dentro de arch hay que configurar algunas cosas como la
zona horaria, para colocar tu zona horaria hay que ejecutar
```bash
ln -sf /usr/share/zoneinfo/Region/Ciudad /etc/localtime
```
en donde pudes ver las opciones para Region con 
```bash
ls /usr/share/zoneinfo/
``` 
si tu pais esta hay colocas tu pais si no colocas el continente en que
se encuentra, en el caso de chile ya esta en esa lista y deberias volver
a enlistar de tal manera 
```bash 
ls /usr/share/zoneinfo/Chile/
```
y ves las opciones, en mi caso quedaria tal que haci 
```bash
/usr/share/zoneinfo/Chile/Continental
```
si en Region colocaste un continente luego tienes que simplemente
colocar tu ciudad.                                                                    
ahora ejecutas hwclock
```bash
hwclock --systohc
```
puedes ver que la hora este bien con 
```bash
date
```
Localizacion, para colocar tu localizacion edita /etc/locale.gen
pero primero necesitas un editor de texto como nano y lo instalas 
de la sigiente manera
```bash
pacman -S nano
```
ahora si edita /etc/locale.gen
```bash
nano /etc/locale.gen
```
aca descomentas tu pais que termine en UTF-8, guardas cambios
con ctrl + o y sales con ctrl + x, ahora ejecutas
```bash
locale-gen
```
si no te llevas muy bien con el ingles puedes cambiar el idioma para 
despues del reinicio.                                                 
para ponerlo en español es
```bash
nano /etc/locale.conf
```
y en el escribes
```bash
LANG=es_[las siglas de tu pais tipo CL para chile].UTF-8
```
para mantener tu distribucion de teclado para despues del reinicio 
creas el archivo /etc/locale.conf
```bash
nano /etc/locale.conf
```
y en el escribes
```bash
KEYMAP=es 
```
o para latam 
```bash
KEYMAP=la-latin1
```
Instalar el grub. necesitamos grub para arrancar el sistema
al prender el pc, instalamos los sigientes paquetes
```bash
pacman -S grub efibootmgr os-prober
```
instalamos grub con 
```bash
grub-install --target=x86_64-efi --bootloader-id=GRUB-arch
```
ejecutamos os-prober para detectar otros sistemas operativos
```bash
os-prober
```
y terminamos la instalacion de grub configurandolo con 
```bash
grub-mkconfig -o /boot/grub/grub.cfg
```
listo ya tenemos el grub                                                          
ahora vamos a colocarle una contraseña al usuario root
```bash
passwd
```
y escribes tu contraseña dos veces. Ahora toca crear tu usuario
pero primero instalamos sudo
```bash
pacman -S sudo
```
y ahora agregamos tu usuario
```bash
useradd -m [NOMBRE DE USUARIO]
```
y le pones contraseña
```bash
passwd [NOMBRE DE USUARIO]
```
tenemos que darle atributos a ciertas cosas a tu usuario,
para eso ejecutamos
```bash
usermod -aG wheel,audio,video,optical,storage [NOMBRE DE USUARIO]
EDITOR=nano visudo
```
bajas hasta la linea 
```bash
# %wheel ALL=(ALL) ALL
```
y la descomentas. guardas con ctrl + o y sales con ctrl + x.
listo ya podrias reiniciar pero, te olvidas de una cosa crack,
el internet, asi que vamos a crear el hostname con 
```bash
nano /etc/hostname
```
en el escribes tu hostname, puede ser cualquier cosa, luego de eso vamos a 
editar el archivo hosts
```bash
nano /etc/hosts
```
debajo del texto que viene tienes que colocar lo sigiente, de tal manera
```bash
127.0.0.1   localhost
::1         localhost
127.0.1.1   [tu hostname].localdomain   [tu hostname]
```
ahora instalas el network manager para tener acceso a conectarse a internet
```bash
pacman -S networkmanager
```
y lo activas con
```bash
systemctl enable NetworkManager
```
listo el sistema ya esta instalado falta salir de la imagen  iso , desmontar las 
particiones y reiniciar el sistema 
```bash
exit
umount -R /mnt
reboot
```

# -Post instalacion
luego de que el pc se alla reiniciado puedes sacar el  usb o cd 
en el que tenias el sistema live. Ahora el sistema te pedira logearte
colocas tu usuario y contraseña que creaste para este, estas otra ves en 
la terminal, ahora tenemos que activar tu nueva interfas de internet 
para ello volvemos a usar ip link 
```bash
ip link
```
si tu interfas esta en DOWN la tenemos que activar, esto con 
```bash
ip link set [TU INTERFAS] up
```
y queda conectarse a una red wifi, otra ves si usas cable de red no hagas esto.
Para conectarnos a una red wifi vamos a usar la opcion nmcli de network manager
```bash
nmcli device wifi connect [EL NOMBRE DE LA RED] password [CONTRASEÑA DE LA RED]
```
y listo probamos que estemos conectados con 
```
ping google.com
```
si transfiere datos es porque estamos correctamente conectados, si no vuelve a revisar 
tu interfas y volver a conectarte a tu red.                                 
Con esto concluyo la guia, ahora tienes una instalacion limpia de arch, puedes insta
lar los paquetes que quieras con pacman, tambien puedes instalarte un entorno grafico
y personalisar tu arch linux.                                                           
                                                           
# Mi configuracion de Qtile
si gustas puedes ver mi configuracion de Qtil en arch, 
**[Qtile](http://www.qtile.org/)** es un gestor de ventanas en baldosa
escrito en python.                                                       
**[mi configuracion]**
!(.screenshot/qtile_1.png)
!(.screenshot/qtile_2.png)
