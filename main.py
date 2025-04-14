import cv2
import mediapipe as mp
import numpy as np
from scipy.spatial.distance import euclidean

# Initialiser MediaPipe Pose
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()
mp_drawing = mp.solutions.drawing_utils

# Ouvrir la caméra
cap = cv2.VideoCapture(0)

# Stocker la séquence de référence (vide pour l’instant)
reference_sequence = []
user_sequence = []
recording = False

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    # Convertir en RGB pour MediaPipe
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = pose.process(rgb_frame)
    
    if results.pose_landmarks:
        mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
        landmarks = results.pose_landmarks.landmark
        
        # Extraire les coordonnées X, Y des points clés
        pose_data = np.array([(lm.x, lm.y) for lm in landmarks]).flatten()
        
        if recording:
            reference_sequence.append(pose_data)
        else:
            user_sequence.append(pose_data)
    
    # Afficher un message d'enregistrement
    text = "Recording reference..." if recording else "Recording user movement..."
    cv2.putText(frame, text, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    
    # Afficher la vidéo
    cv2.imshow('AI Dance Trainer', frame)
    key = cv2.waitKey(1) & 0xFF
    
    if key == ord('r'):
        recording = not recording  # Toggle l’enregistrement
        print("Recording state:", "ON" if recording else "OFF")
    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

# Sauvegarder la séquence de référence
np.save("reference_dance.npy", reference_sequence)
