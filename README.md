# dotfiles
mi configuracion de arch en español, qtile


# Arch guia de instalacion (UEFI) :

esta es una guia de instalacion limpia de arch linux en maquinas
uefi, puede que en tu dispositivo tenga errores u otra cosa asi 
que aqui te dejo la santa biblia de arch su wiki oficial
  https://wiki.archlinux.org/  
tambien su guia de instalacion en español
  https://wiki.archlinux.org/index.php/Installation_guide_(Espa%C3%B1ol)

# -Preinstalacion
primero debiste arrancar el sistema en un live usb o cd si es 
asi debes estar dentro de una terminal, ya podemos empezar

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
(omitir si estas por cable de red asta salir de iwctl)
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

