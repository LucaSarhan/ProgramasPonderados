# Texto Explicativo

Foram utilizadas as bibliotecas da ultralytics, para a importação do método Yolo, o responsável pela detecção dos objetos, e a PIL, para a importação de Image e assim dar a possibilidade de vizualização da imagem.

Depois, carreguei um modelo pré treinado chamado "yolov8n", e o treinei com o dataset da roboflow para a detecção de rachaduras. Após isso, fiz a validação do modelo, para garantir que ele teve um treino eficaz.

Para testá-lo, peguei algumas imagens de teste oferecidos pela roboflow e o mandei prever se há algumas rachadura nas imagens, e o modelo encontrou em todas!
