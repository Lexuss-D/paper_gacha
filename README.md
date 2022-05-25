# paper_gacha

## Intro

A gacha game for those who don't know which paper should read next. 

This game will generate 10 papers from all papers published by ACL. People who plays social games should be familier with this so I will not explain more, just have a try. 

Run gacha.py then start a suffering life!

## Data

ACL Anthology BibTex file
https://aclanthology.org/anthology.bib.gz

## Processing

`` bib_to_csv.py `` is to generate a csv file of formatted data from ``anthology.bib``.

``gacha.py`` is the main process of gacha game.   

Currently I made 4 rarities : R, SR, SSR, UR, 
and the probability is 50%, 30%, 15%, 5% respectively

## TODO

About rarity, I only decide few papers like BERT is UR, some annual best papers are SSR and SR. I am going to find somehow decide the rarity by citation counts or something else
