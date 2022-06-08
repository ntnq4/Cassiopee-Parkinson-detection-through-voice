# 82 - Study of Longitudinal Voice Features for Early Detection and Monitoring of Parkinson’s Disease

Ce projet est réalisé dans le cadre du projet *Cassiopée* à Télécom SudParis.

## Introduction

Les troubles vocaux, connus sous le nom de dysarthrie hypokinétique, sont l’un des premiers symptômes détectables chez un parkinsonien. À l’heure actuelle, il existe un grand nombre d’articles sur la détection de la maladie de Parkinson se basant sur l’analyse de la voix. Cependant, peu d’entre eux se sont concentrés sur les premiers stades de la maladie et les recherches associées sont souvent réalisées dans un cadre audiophonique optimal.

Le but de notre projet est alors d’étudier les changements vocaux dans la maladie de Parkinson à un stade précoce et préclinique dans un cadre où la parole serait transmise par des canaux téléphoniques. Afin d’atteindre cet objectif, nous utiliserons plusieurs approches d’apprentissage automatique appliquées à des enregistrements audios et téléphoniques.

Le projet est divisé en trois parties distintes ayant vocation plus tard à fusionner.
Ainsi, il se compose d'une partie traitement la classification des données grâce à des sepctrogrammes et un réseau de neurones convolutifs (CNN), d'une classification des données brutes via l'architecture neuronnale SincNet permettant de traiter directement l'audio brut sans calcul de paramètres vocaux globaux et d'un travail de traitement des données audio.

## Classification à partir d'une forme d'onde brute, SincNet

Cette partie repose sur l'architecture neuronnale SincNet proposée par Mirco Ravanelli et Yoshua Bengio [1][2].


## Références
[1]  Mirco Ravanelli, Yoshua Bengio, “Speaker Recognition from raw waveform with SincNet” [Arxiv](http://arxiv.org/abs/1808.00158)
[2] SincNet original code written in PyTorch by the autor (https://github.com/mravanelli/SincNet)
