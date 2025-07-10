# 🤖 AI Dance Trainer avec MediaPipe et OpenCV

Cette application permet d’enregistrer une séquence de mouvements corporels via webcam avec **MediaPipe Pose**, afin de créer une référence, puis d’enregistrer les mouvements de l’utilisateur pour une comparaison ou analyse ultérieure.

---

## 🚀 Fonctionnalités

- Capture vidéo en temps réel via webcam  
- Détection des points clés du corps avec MediaPipe Pose  
- Enregistrement de séquences de pose (référence & utilisateur)  
- Indication visuelle du mode d’enregistrement (référence ou utilisateur)  
- Sauvegarde de la séquence de référence dans un fichier `.npy`

---

## ▶️ Utilisation

1. Cloner le dépôt ou copier le script  
2. Installer les dépendances :

```bash
pip install opencv-python mediapipe numpy scipy
