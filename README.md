# MAC-CHANGER

**MAC-CHANGER** is a simple command-line tool that allows you to change the MAC (Media Access Control) address of your network interfaces. Changing your MAC address can help improve privacy, troubleshoot network issues, or bypass MAC address-based filtering.

---

## Features:
- **Change MAC Address**: Change the MAC address of your device’s network interface.
- **Restore Original MAC**: Restore the original MAC address after changing it.
- **Support for Multiple Interfaces**: Supports wired (Ethernet) and wireless (Wi-Fi) network interfaces.
- **Easy to Use**: Simple command-line interface for quick MAC address modification.

---

## Table of Contents

1. [Installation](#installation)
2. [Usage](#usage)
3. [Examples](#examples)
4. [Contributing](#contributing)
5. [License](#license)
6. [Acknowledgments](#acknowledgments)

---

## Installation

### Prerequisites:
- Linux or macOS (For Windows, use WSL or Cygwin)
- Python 3.x or higher

### Steps:
1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/MAC-CHANGER.git
    cd MAC-CHANGER
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

---

## Usage

### 1. Check Your Current MAC Address
To view the current MAC address of your network interface, run the following command:

```bash
python mac_changer.py --current
```

# Contributing
Contributions are welcome! If you would like to contribute to the project
