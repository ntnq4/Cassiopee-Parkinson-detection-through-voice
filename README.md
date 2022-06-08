# 82 - Study of Longitudinal Voice Features for Early Detection and Monitoring of Parkinson’s Disease

Ce projet est réalisé dans le cadre du projet *Cassiopée* à Télécom SudParis.

## Introduction

Les troubles vocaux, connus sous le nom de dysarthrie hypokinétique, sont l’un des premiers symptômes détectables chez un parkinsonien. À l’heure actuelle, il existe un grand nombre d’articles sur la détection de la maladie de Parkinson se basant sur l’analyse de la voix. Cependant, peu d’entre eux se sont concentrés sur les premiers stades de la maladie et les recherches associées sont souvent réalisées dans un cadre audiophonique optimal.

Le but de notre projet est alors d’étudier les changements vocaux dans la maladie de Parkinson à un stade précoce et préclinique dans un cadre où la parole serait transmise par des canaux téléphoniques. Afin d’atteindre cet objectif, nous utiliserons plusieurs approches d’apprentissage automatique appliquées à des enregistrements audios et téléphoniques.

Le projet est divisé en trois parties distintes ayant vocation plus tard à fusionner.
Ainsi, il se compose d'une partie traitement la classification des données grâce à des sepctrogrammes et un réseau de neurones convolutifs (CNN), d'une classification des données brutes via l'architecture neuronnale SincNet permettant de traiter directement l'audio brut sans calcul de paramètres vocaux globaux et d'un travail de traitement des données audio.

## Classification à partir d'une forme d'onde brute, SincNet

Cette partie repose sur l'architecture neuronnale SincNet proposée par Mirco Ravanelli et Yoshua Bengio [1] [2].

<img src="https://github.com/mravanelli/SincNet/blob/master/SincNet.png" width="400" img align="right">

### Prérequis

- Linux
- Python 3.6/2.7
- pytorch 1.0
- pysoundfile (``` conda install -c conda-forge pysoundfile```)
- l'utilisation d'un environnement anaconda est conseillée.


### Utilisation de SincNet pour la classification du genre avec TIMIT

**1. Normalisation des données.**

Cette étape est nécessaire pour stocker une version de TIMIT dans laquelle les silences de début et de fin sont supprimés et l'amplitude de chaque énoncé vocal est normalisée. Pour ce faire, exécutez le code suivant :

``
python TIMIT_preparation.py $TIMIT_FOLDER $OUTPUT_FOLDER data_lists/TIMIT_all.scp
``

où:
- *$TIMIT_FOLDER*  est le dossier contenant la base TIMIT originelle
- *$OUTPUT_FOLDER* est le dossier où sera stockée la version normalisée de la base de donnée
- *data_lists/TIMIT_all.scp*  est la liste de tous les fichiers de TIMIT.

**2. Entraînement du modèle.**

- Modifiez la section *[data]* du fichier *cfg/SincNet_TIMIT.cfg* avec vos chemins d'accès. En particulier, modifiez le répertoire *data_folder* avec *$OUTPUT_FOLDER* que vous avez spécifié à l'étape précédente. Les autres paramètres du fichier de configuration appartiennent aux sections suivantes :
 1. *[windowing]*, qui définit comment chaque phrase est divisée en plus petits morceaux..
 2. *[cnn]*,  qui spécifie les caractéristiques de l'architecture CNN.
 3. *[dnn]*,  qui spécifie les caractéristiques de l'architecture DNN entièrement connectée suivant les couches CNN.
 4. *[class]*, qui spécifient la partie class
 5. *[optimization]*, qui indique les principaux hyperparamètres utilisés pour entraîner l'architecture.

**Attention :** ne pas oublier de modifier le paramètre **class-lay** conformément au nombre de classe que l'on attend. Ici, *class_lay=2*.

- Une fois le fichier cfg configuré, vous pouvez lancer les expériences d'identification du haut-parleur en utilisant la commande suivante :

``
python speaker_id.py --cfg=cfg/SincNet_TMT.cfg
``

L'entraînement peut prendre du temps à converger selon la rapidité de votre carte graphique (GPU).

**3. Résultats.**

### utilisation de SincNet pour la classification des Parkinsoniens



## Références
[1]  Mirco Ravanelli, Yoshua Bengio, “Speaker Recognition from raw waveform with SincNet” [Arxiv](http://arxiv.org/abs/1808.00158)

[2] SincNet original code written in PyTorch by the autor (https://github.com/mravanelli/SincNet)

[3] [Voice characteristics from isolated rapid eye movement sleep behavior disorder to early Parkinson's disease](https://www.prd-journal.com/action/showPdf?pii=S1353-8020%2822%2900003-7)
