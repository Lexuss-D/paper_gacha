# paper_gacha

## Intro

A gacha game for those who don't know which paper should read next. 

This game will select 10 papers from all papers published by ACL. People who plays social games should be familier with this so I will not explain more, just have a try. 

Run gacha.py then start a suffering life!

## Data

ACL Anthology BibTex file
https://aclanthology.org/anthology.bib.gz

## Processing

- `` bib_to_csv.py `` is to generate a csv file of formatted data from ``anthology.bib``.
  - The information of citation are from Google Scholar

  - The rarity is decided by the number of citations  
    $citations \geq 10000 = UR$  
    $10000 > citations \geq 5000 = SSR$  
    $5000 > citations \geq 1000 = SR$  
    $1000 > citations = R$

  - Terrible time cost
    - CPU: Intel(R) Xeon(R) CPU E5-2660 v4 @ 2.00GHz
      - About 14 hours
    - CPU: Ryzen 5900x
      - 11 h 33 m 

- ``gacha.py`` is the main process of gacha game.   

  - Currently I made 4 rarities : R, SR, SSR, UR, and the probability is 50%, 30%, 15%, 5% respectively
  
  - 10 papers per gacha

## TODO
- Maybe I should change the data file format from csv to Json ?
- Multiprocessing for acceleration <- Now here
- HTML is empty, why, why, Y <- Now here
