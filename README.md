# DB920PluginFetcher

A plugin for Dreambox 920 (Enigma2/OpenATV) to fetch RSS and YouTube feeds and send them to WordPress as draft posts.

---

## Features

- Fetch RSS feeds and YouTube channel updates daily
- List and send items to one or more WordPress sites as drafts (for review/publishing)
- Simple Enigma2 menu UI for interaction

---

## Installation

### Option 1: Direct from GitHub

```bash
opkg update
opkg install git python3-feedparser python3-requests
cd /tmp
git clone https://github.com/sadiqaka/DB920PluginFetcher.git
cd DB920PluginFetcher
chmod +x setup.sh
./setup.sh
