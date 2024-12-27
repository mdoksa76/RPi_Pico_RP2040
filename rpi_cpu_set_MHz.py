import machine

# ANSI escape kod za crvenu boju
RED = "\033[91m"
RESET = "\033[0m"

# Odabir jezika
language = input("Odaberite jezik / Choose language (hr/en): ").strip().lower()

if language == "en":
    print("________________________________")
    print("")
    print("  CPU RP2040 Frequency/[MHz]  ")
    cpu_freq = machine.freq() / 1e6
    print(f"   CPU Frequency: {cpu_freq} MHz")
    print("________________________________")

    print("")
    print("Allowed values are between 125 MHz and 250 MHz.")
    print("")
    while True:
        try:
            cpu_freq_new = int(input("Enter CPU RP2040 frequency: "))
            break
        except ValueError:
            print("Please enter a valid numerical value.")
    print("")

    if cpu_freq_new < 125:
        machine.freq(125000000)
        cpu_freq = machine.freq() / 1e6
        print("________________________________")
        print("")
        print("  CPU RP2040 Frequency/[MHz]  ")
        cpu_freq = machine.freq() / 1e6
        print(f"   CPU Frequency: {RED}{cpu_freq} MHz{RESET}")
        print("________________________________")

    elif cpu_freq_new > 250:
        machine.freq(125000000)
        cpu_freq = machine.freq() / 1e6
        print("________________________________")
        print("")
        print("  CPU RP2040 Frequency/[MHz]  ")
        cpu_freq = machine.freq() / 1e6
        print(f"   CPU Frequency: {RED}{cpu_freq} MHz{RESET}")
        print("________________________________")

    else:
        machine.freq(int(cpu_freq_new * 1e6))
        cpu_freq = machine.freq() / 1e6
        print("________________________________")
        print("")
        print("  CPU RP2040 Frequency/[MHz]  ")
        cpu_freq = machine.freq() / 1e6
        print(f"   CPU Frequency: {RED}{cpu_freq} MHz{RESET}")
        print("________________________________")

else:
    print("________________________________")
    print("")
    print("  CPU RP2040 frekvencija/[MHz]  ")
    cpu_freq = machine.freq() / 1e6
    print(f"   CPU frekvencija: {cpu_freq} MHz")
    print("________________________________")

    print("")
    print("Dozvoljene vrijednosti su između 125 MHz i 250 MHz.")
    print("")
    while True:
        try:
            cpu_freq_new = int(input("Unesi frekvenciju CPU RP2040: "))
            break
        except ValueError:
            print("Molimo unesite valjanu numeričku vrijednost.")
    print("")

    if cpu_freq_new < 125:
        machine.freq(125000000)
        cpu_freq = machine.freq() / 1e6
        print("________________________________")
        print("")
        print("  CPU RP2040 frekvencija/[MHz]  ")
        cpu_freq = machine.freq() / 1e6
        print(f"   CPU frekvencija: {RED}{cpu_freq} MHz{RESET}")
        print("________________________________")

    elif cpu_freq_new > 250:
        machine.freq(125000000)
        cpu_freq = machine.freq() / 1e6
        print("________________________________")
        print("")
        print("  CPU RP2040 frekvencija/[MHz]  ")
        cpu_freq = machine.freq() / 1e6
        print(f"   CPU frekvencija: {RED}{cpu_freq} MHz{RESET}")
        print("________________________________")

    else:
        machine.freq(int(cpu_freq_new * 1e6))
        cpu_freq = machine.freq() / 1e6
        print("________________________________")
        print("")
        print("  CPU RP2040 frekvencija/[MHz]  ")
        cpu_freq = machine.freq() / 1e6
        print(f"   CPU frekvencija: {RED}{cpu_freq} MHz{RESET}")
        print("________________________________")
