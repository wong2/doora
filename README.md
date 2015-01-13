##Doora: Just another file sharing service

### Introduction

Doora is a file sharing service powered by [qiniu](http://www.qiniu.com/).
It's build for speed and simplicity: Drop & Share, that's all.

### Screenshot

![Screenshot](http://doora.qiniudn.com/screenshot.png)

### Demo

A live demo is at: <http://lab.wong2.me/doora/> (files are kept for 30 minutes)

### Quick Start

1. Clone the repo: `git clone https://github.com/wong2/doora.git`
2. `cd doora`, edit `config.py`
3. run `app.py`
4. if you need file expiration, set the expire time in `config.py`, then run `rqworker doora` and `rqscheduler` in terminal.
5. if you need to modify `index.html`: (1) `npm install html-minifier -g`, (2) edit templates/index.tmpl (3) `make min`

❤
