# GoldSrc CS-1.6 / Xash3D Server Info Detector Using UDP-Server-Query By TheRealsGMMa

<p align="center">
  <img src="https://i.top4top.io/p_3937rvecg0.jpg" alt="GoldSrc Server Query" width="750">
</p>

<p align="center">
  <a href="https://github.com/therealsgmmaaa/Game-Server-Checker-/releases"><img src="https://img.shields.io/github/v/release/therealsgmmaaa/Game-Server-Checker-?style=for-the-badge&color=brightgreen&label=Latest%20Release" alt="Latest Release"></a>
  <a href="https://github.com/therealsgmmaaa/Game-Server-Checker-/releases"><img src="https://img.shields.io/github/downloads/therealsgmmaaa/Game-Server-Checker-/total?style=for-the-badge&color=blue&label=Total%20Downloads" alt="Total Downloads"></a>
  <img src="https://img.shields.io/github/stars/therealsgmmaaa/Game-Server-Checker-?style=for-the-badge&color=yellow" alt="GitHub Stars">
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

يمكنك تحميل الأداة وتثبيتها مباشرة عبر خيارين:

### Option 1: Quick Install via Termux (Recommended)
شغّل الأوامر التالية داخل **Termux** لتثبيت الأداة والبدء في استخدامها مباشرة:

```bash
cd ~ && mkdir Game-Server-Checker && cd Game-Server-Checker && pkg update && pkg upgrade -y && pkg install python curl -y && curl -O -L https://github.com/therealsgmmaaa/Game-Server-Checker-/releases/download/main/Game-Server-Checker.py && python Game-Server-Checker.py
