# GoldSrc CS-1.6 / Xash3D Server Info Detector Using UDP-Server-Query By TheRealsGMMa

<p align="center">
  <img src="https://i.top4top.io/p_3937rvecg0.jpg" alt="GoldSrc Server Query" width="750">
</p>

<p align="center">
  <a href="https://github.com/therealsgmmaaa/Game-Server-Checker-/releases"><img src="https://img.shields.io/github/v/release/therealsgmmaaa/Game-Server-Checker-?style=for-the-badge&color=brightgreen&logo=github&label=Latest%20Release" alt="Latest Release"></a>
  <a href="https://github.com/therealsgmmaaa/Game-Server-Checker-/releases"><img src="https://img.shields.io/github/downloads/therealsgmmaaa/Game-Server-Checker-/total?style=for-the-badge&color=blue&logo=github&label=Total%20Downloads" alt="Total Downloads"></a>
  <img src="https://img.shields.io/github/stars/therealsgmmaaa/Game-Server-Checker-?style=for-the-badge&color=yellow&logo=github" alt="GitHub Stars">
</p>

---

## 🚀 Our Tool Features

* ⚡ **Instant & Lightweight Query**: Fetch accurate, real-time server stats instantly using direct UDP `A2S_INFO` queries without joining or downloading map assets.
* 🛡️ **Zero External Dependencies**: No need for complex setup, external API keys, or heavy Discord tracking bots.
* 🎮 **Multi-Engine Support**: Full compatibility with **Counter-Strike 1.6**, **Half-Life 1**, and custom **Xash3D FWGS** server instances (Protocol 49).
* 🔍 **Deep Server Insights**: Instantly reveals server hostname, colored tags, current map, active players count, protocol version, and real ISP ping.
* 📱 **Termux & Mobile Friendly**: Optimized to run seamlessly on Android via Termux, Linux CLI, and low-spec environments.
* 🤝 **Solo Friendly**: Check if your favorite server is alive and populated without asking friends or joining empty games.

---

## 📥 Downloads & Releases

Choose one of the following methods to install and run the tool on your system:

### Option 1: Direct Release From GitHub Relases
<p align="left">
  <a href="https://github.com/therealsgmmaaa/Game-Server-Checker-/releases">
    <img src="https://img.shields.io/badge/GitHub-Releases_%26_Downloads_Page-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub Releases Page">
  </a>
</p>

### Option 2: Direct Release Install via Termux (Recommended)
Run this one-line command in **Termux** to create the project folder, install python/curl, download the latest standalone release script directly, and run it automatically:

```bash
cd ~ && mkdir Game-Server-Checker && cd Game-Server-Checker && pkg update && pkg upgrade -y && pkg install python curl -y && curl -O -L https://github.com/therealsgmmaaa/Game-Server-Checker-/releases/download/main/Game-Server-Checker.py && python Game-Server-Checker.py`
```

## 🎮 How To Use After Installation

Once the tool is running, simply enter any Counter-Strike 1.6, Half-Life 1, or Xash3D server IP and Port (or Domain/DNS name).

### 💡 Examples:
* **Using IP & Port:** `192.168.1.1:27015`
* **Using Domain Name:** `cs.example.com:27015`

> ℹ️ **Note:** If you don't enter a port, the tool will automatically default to `27015`.

## 🗑️ Delete The Tool From Ur Device 

```
cd ~
```
```
rm -f Game-Server-Checker
```


The tool will immediately query the server and display live details such as current map, player counts, ping, and server name!
