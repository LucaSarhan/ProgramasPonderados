Explicação:

# Bibliotecas usadas
O rclpy e Node, que instanciam o cliente ROS e a classe de nó. O Twist define a mensagem como tipo Twist. O Odometry define a extração como tipo de odometria. Euler_from_quaternion calcula a posição de rotação do robô.

# Classe TurtlebotMove
Ela herda o nó e é responável por instanciar o construtor da classe do nó, chamado de 'turtlebot_controller'. Ele tem o editor que pública mensagens do tipo Twist no tópico '/cmd_vel' e também tem o subscriber que extrai dados de odometria no tópico /odom. Essa classe é responsável pela movimentação do robô.

# Explicando a movimentação do robô
Na classe, é criada uma lista de caminhos que o robô irá percorrer. Assim como seu tamanho e endereço inicial que irá percorrer a lista. Quando são recebidos os dados de osometria, é calculado a posição de rotação do robô com biblioteca de euler_from_quaternion, e com todos os dados, eles são informados através do terminal e começa o processo da movimentação, isso tudo ocorrendo a cada 0,1s. No começo, será conferido se há valores na lista de caminhos a serem percorridos. Caso há, um valor alvo para o robô se locomover será determinado, ele corresponde a posição atual dele somado a posição que ele irá se locomover. Quando o robô chegar nessa posição pretendida, com uma margem de erro (podendo ir para frente ou para conferindo autocorreção) ele irá para o próximo caminho da lista se houver, caso não ele parará por lá mesmo.
Na função main, ocorre a inicialização do ROS, do objeto da classe TurtlebotMove e do encerramento do nó e do programa ROS.

# Vídeo do TurtlebotMove

Link do video comprovando o funcionando: https://drive.google.com/file/d/1kb86FrsE-WW2s2EIkEu8CDR5f7gHqdY6/view?usp=sharing
