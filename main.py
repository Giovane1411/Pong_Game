import pygame
pygame.init() # inicia as multimidia do pygame para exibir áudio, animaçoes...

display = pygame.display.set_mode((1280, 720)) # Define a resolução da tela do jogo 

player1 = pygame.Rect(0, 0, 30, 150) # Definindo o retângulo do jogador 1
player1_speed = 12 # Velocidade do jogador 1
player1_score = 0


player2 = pygame.Rect(1250, 0, 30, 150) # Definindo o retângulo do jogador 2
player2_score = 0

ball = pygame.Rect(600,350, 15, 15) # Definindo o retângulo da bola
ball_dir_x = 12 # A bola movimenta na direção x
ball_dir_y = 12 # A bola movimente na direção y

font = pygame.font.Font(None, 50)
placar_player1 = font.render(str(player1_score), True, "white")
placar_player2 = font.render(str(player2_score), True, "white")


# Para exibir a tela é preciso sempre deixar em loop True
loop = True

fps = pygame.time.Clock() # Define velocidade

# Menu sera toda mecânica do jogo, jogo seria a movimentação do jogos, gameover seria a cena de jogo acabou
cena = "menu"

while loop:

    if cena == "jogo": 

        for event in pygame.event.get(): # Verifica os eventos que ocorrem na tela
            if event.type == pygame.QUIT: # Caso o evento de fechar a janela ocorra, a tela será fechada
                loop = False # Terminará o loop da tela
            if event.type == pygame.KEYDOWN: # Caso uma tecla seja pressionada
                if event.key == pygame.K_w: # Se a tecla pressionada for W, o jogador 1 se moverá para cima
                    player1_speed = -12 # Define a velocidade do jogador 1 para cima
                elif event.key == pygame.K_s: # Se a tecla pressionada for S, o jogador 1 se moverá para baixo
                    player1_speed = 12 # Define a velocidade do jogador 1 para baixo
        if player1_score >=3:
            cena = "gameover"
        
        if player2_score >= 3:
            cena = "gameover"

        if ball.colliderect(player1) or ball.colliderect(player2): # Aqui identificará se algo irá colidir com o retângulo
            ball_dir_x *= -1 # A bola irá ser arremessado para o lado oposto 
            hit = pygame.mixer.Sound("assets/pong.wav") # Aqui estou configurando o som e espeficando o caminho do arquivo 
            hit.play() # Começa a tocar caso a condição for afirmativa
    
        if player1.y <= 0: # Se caso a soma da atualização deu menor que 0, irá receber o valor de 0 para não passar da borda superior
            player1.y = 0
        elif player1.y >= 720 - 150: # Usei o 150, pois é o retangulo tem 150 pixel e preciso colocar o jogador dentro da tela
            player1.y = 720 - 150

        player1.y += player1_speed # Aqui vai somando a posição do player 1 no eixo y

        if ball.x <= 0: # Não deixa passar a bola no lado esquerdo
            #ball.x = 600
            player2_score += 1
            placar_player2 = font.render(str(player2_score), True, "white")
            ball_dir_x *= -1
        elif ball.x >= 1280: # Não deixa passar a bola no lado direito no eixo x
            #ball.x = 600
            player_score +=1
            placar_player1 = font.render(str(player1_score), True, "white")
            ball_dir_x *= -1

        ball.x += ball_dir_x # Faz o movimento no eixo x 

        if ball.y <= 0: # Aqui impedirá que a bola passa do limite superior do y da tela
            ball_dir_y *= -1 # aqui é pura matemática, inverte o sinal para a bola ir na direção oposta 
        elif ball.y >= 720 - 15: # Aqui impedirá que a bola passa do limite inferior do y da tela
            ball_dir_y *= -1
        ball.y += ball_dir_y # Esse comando faz realizar o movimento da bola

        player2.y = ball.y - 75  # Comando faz com que a bola quica no meio do player dois  

        


        display.fill("black")  # Qual cor de fundo na tela
        pygame.draw.rect(display, "green", player1) # Desenha o retângulo do jogador 1
        pygame.draw.rect(display, "green", player2) # Desenha o retângulo do jogador 2
        pygame.draw.circle(display, "green", ball.center, 8) # Desenha o círculo da bolinha, definindo um raio 8
        display.blit(placar_player1, (500,50))
        display.blit(placar_player2, (780,50))
    elif cena == "gameover":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    cena = "menu"

        display.fill((0,0,0))
        text_win = font.render("Game Over", True, "white")
        display.blit(text_win, (540,360))

    elif cena == "menu":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    player1_score = 0
                    placar_player1 = font.render(str(player1_score), True, "white")
                    player2_score = 0
                    placar_player2 = font.render(str(player2_score), True, "white")
                    player1.y = 0 
                    player2.y = 0
                    ball.x = 640
                    ball.y = 320
                    cena = "jogo"    

        display.fill((0,0,0))
        title = font.render("My Game", True, "white")
        text = font.render("Press Star to Play", True, "white")
        display.blit(title, (500,260))
        display.blit(text, (500,360))

    fps.tick(60)    
    pygame.display.flip()