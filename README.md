# Raspberry Pi Pico RP2040 clone 16 MB, RP2040-Zero 2 MB

VCC-GND.COM - YD-RP2040 GPIO dijagram

![My Image](images/YD-RP2040.png)

TZT RP2040-Zero GPIO dijagram

![My Image](images/rp2040-zero.png)

<hr>
Micropython kod za Raspberry Pi Pico i "kineske klonove".
<hr>

**file_manager.py**

Skripta za obavljanje osnovnih radnji s datotekama i direktorijima.

![My Image](images/file_manager.png)
<hr>

**rpi_cpu_set_MHz.py**

Skripta za postavljanje frekvencije RP2040 procesora u rasponu od 125 MHz do 250 MHz.

![My Image](images/RP2040-set-freq.png)
<hr>

**sysinfo.py**

Skripta za ispis sistemskih informacija vezano uz cpu, ram, flash, datum, uptime, sadržaj flash memorije.

![My Image](images/RP2040-sysinfo.png)
<hr>

**led_onboard.py**

Skripta blinkanja led lampice na ploči mikrokontrolera spojenoj na Pin 25.

![My Image](images/RP2040-led-onboard.png)
<hr>

**led_onboard-pwm_brightness-data_txt.py**

Skripta blinkanja led lampice na ploči mikrokontrolera s kontrolom količine svjetlosti. Vrši se ispis vrijednosti osvjetljenja led lampice i pretvorba u pripadnu vrijednost napona u terminalu i isti podaci se zapisuju u datoteku pwm_data.txt.

![My Image](images/RP2040-led-onboard-pwm_brightness-data_txt.png)
<hr>

**ssd1306_i2c_check_20-21-gnd-3V3.py**

Skripta provjere postojanja funkcionalnog I2C uređaja povezanog s RP2040

![My Image](images/ssd1306-i2c-check.png)
<hr>

**Kolekcija ssd1306 skripti**

ssd1306_3d-cube-fps.py3d - žičani model kocke rotira na ssd1306 128x32 zaslonu.

ssd1306_clock-128x32.py - sat na ssd1306 128x32 zaslonu.

ssd1306_clock-128x64.py - sat na ssd1306 128x64 zaslonu.

ssd1306_date-clock-128x32.py - datum i sat na ssd1306 128x32 zaslonu.

ssd1306_date-clock-128x64.py - datum i sat na ssd1306 128x64 zaslonu.

ssd1306_random_circles_fps.py - krugovi na ssd1306 128x32 zaslonu po slučajnom odabiru položaja i veličine polumjera uz prikaz fps-a.

ssd1306_random_circles_squares_fps.py - krugovi i kvadrati na ssd1306 128x32 zaslonu po slučajnom odabiru položaja i veličine polumjera uz prikaz fps-a.

ssd1306_random_squares_fps.py - kvadrati na ssd1306 128x32 zaslonu po slučajnom odabiru položaja i veličine polumjera uz prikaz fps-a.

ssd1306_random_triangles_fps.py - trokuti na ssd1306 128x32 zaslonu po slučajnom odabiru položaja i veličine polumjera uz prikaz fps-a.

RP2040-demo.py - animacija za ssd1306 zaslon.

<hr>
