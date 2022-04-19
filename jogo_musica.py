import random

question = ["Uma música com uma cor no título", "Uma música com um número no título", "Uma música com o nome de um homem no título", "Uma música com o nome de uma mulher no título", "Uma música com o nome de uma cidade no título", "Uma música com um verbo no título", "Uma música com uma hora do dia no título", "Uma música sobre drogas", "Uma música sobre sexo", "Uma música sobre amor", "Uma música sobre a noite", " Uma música que precisa ser tocada no volume máximo", "Uma música que te faça dançar", "Uma música para dirigir enquanto você a ouça", "Uma música para ser tocada no seu casamento", "Uma música para se fazer um dueto no karaokê", "Uma música para ser tocada durante seu enterro", "Uma música para ser tocada durante o sexo", "Uma música para ser tocada em uma batalha", "Uma música desse ano", "Uma música da sua pré-adolescência", "Uma música do ano que você nasceu", "Uma música de uma banda que você quisesse que ainda estivesse junta", "Uma música de um artista que morreu", "Uma música da década de ", "Uma música que você não se cansa de ouvir", "Uma música que te alegre", "Uma música que te entristeça", "Uma música que tenha muitos significados para você", "Uma música que te mova para frente", "Uma música que parta o seu coração", "Uma música que te faça pensar sobre a vida", "Uma música te faça querer se apaixonar", "Uma música que te lembre de alguém que você preferiria esquecer", "Uma música que te lembre de você", "Uma música sobre um filme", "Uma música sobre um livro ou peça", "Uma música sobre uma pintura ou escultura", "Uma música sobre a internet", "Uma música de um musical", "Uma música dedicada a pessoa mais bonita da mesa", "Uma música meme", "Uma música que sampleie ou remixe outra", "Uma música que seja um cover por um outro artista", "Uma obra erudita que você goste", "Uma música que você goste de um gênero que você normalmente não ouve", "Uma música em uma língua estrangeira que não seja inglês", "Uma música em português", "Uma música famosa que você ame", "Uma música obscura que você ame", "Uma música que você saiba que é uma das favoritas de uma outra pessoa na mesa", "Uma música sobre mágica", "Uma música que você ouve enquanto estuda", "Uma música instrumental", "Uma música que tenha sido recomendada por um amigo", "Uma música cujo clipe você ame", "Uma música com o nome de uma comida no título", "Uma música de um artista cuja voz você ame", "Uma música sobre o espaço e o universo", "Uma música tão ruim que é boa", "Uma música que seja um one hit gwonder", "Uma música sobre traição", "Uma música sobre tempo", "Uma música que você gosta de um artista que você geralmente não gosta", "Uma música com mais de  anos", "Uma música da trilha sonora de um filme", "Uma música que não é sobre o que parece ser", "Uma música que te conduziu por um período difícil", "Uma música com metais", "Uma música com o nome de um país no título", "Uma música com um solo", "Uma música sobre o tempo", "Uma música de ficção científica", "Uma música com uma assinatura de baixo marcante", "Uma música que é uma das favoritas de alguém na mesa", "Uma música que seja um guilty pleasure seu", "Uma música com uma mensagem que você não aprecia mas que você não consegue não gostar", "Uma música que você acha que todo mundo deveria escutar", "Uma música de um dos seus álbuns favoritos", "Uma música sobre dinheiro", "Uma música para ouvir chapado", "Uma música para ouvir quando está chovendo lá fora", "Uma música de protesto", "Uma música que você não gostou da primeira vez que ouviu mas que você ama agora", "Uma música de um artista lgbt", "Uma música que você ainda não ouviu de um artista que você goste", "Uma música cômica", "Uma música com só uma palavra no título", "Uma música de um artista que você gostava antes dele ser popular", "Uma música sobre religião", "Uma música de um artista que você tenha ouvido ao vivo", "Uma música intensa", "Uma música atmosférica", "Uma música que você não entende  como não é mais popular", "Uma música que você já indicou para um amigo", "Uma música que você ouviu pela primeira vez a menos de um mês", "Uma música retrô", "Uma música que fica reaparecendo na sua vida", "Uma música que não dá para ouvir uma só vez", "Uma música que te inspire", "Uma música com uma hora do dia no título", "Uma música com um dia da semana no título", "Uma música sobre sonhos", "Uma música sobre a morte", "Uma música sobre álcool", "Uma música doce-amarga", "Uma música que seus pais tenham apresentado a você", "Uma música que você descobriu através de recomendações automáticas", "Uma música com mais de  minutos", "Uma música com menos de  minutos", "Uma música que você não tem certeza sobre o que ela fala", "Uma música triunfal", "Uma música com o nome de um animal no título", "Uma música cujo bpm muda ao longo dela", "Uma música /mu/-core que você ame", "Uma música cujo estilo muda radicalmente ao longo dela", "Uma música abrasiva", "Uma música tecnicamente interessante", "Uma música com uma narrativa", "Uma música na qual o artista convidado é melhor que o artista principal", "Uma música que você considera subestimada", "Uma música de um artista que tenha morrido recentemente", "Uma música de um artista do clube dos ", "Uma música de um artista que morreu de overdose", "Uma música de um artista que morreu violentamente", "Uma música de um artista asiático", "Uma música de um artista africano", "Uma música de um artista da América espanhola", "Uma música de um artista da Oceania", "Uma música com elementos não-musicais", "Uma música com uma parte do corpo no título", "Uma música para te embalar ao sono", "Uma música sobre crime", "Uma música sobre moda", "Uma música sardônica", "Uma música com uma key change", "Uma música que você não escuta faz muito tempo", "Uma música obscura de um artista famoso", "Uma música sobre guerra", "Uma música soturna", "Uma música animada", "Uma das músicas favoritas do seu grupo de amigos", "Uma música sobre videogames", "Uma música minimalista", "Uma música intrincada", "Uma música sobre alienação", "Uma música que você ama mas que te aliena", "Uma música sobre dinheiro", "Uma música sobre uma outra música", "Uma música que resuma o opus e a mensagem do artista dela", "Uma música sobre círculos viciosos", "Uma música com um dos quatro elementos no título", "Uma música que estava tocando em um momento importante da sua vida", "Uma música sobre loucura", "Uma música fofa", "Uma música que retrate um diálogo", "Uma música que te lembra de alguém que você gostaria de rever", "Uma música esperançosa", "Uma música sobre vingança", "Uma música com o nome de uma parte do ano no título", "Uma música feita quase toda por uma pessoa só", "Uma música que só é boa quando você não presta atenção nela", "Uma música com palavra falada", "Uma música com vocais masculinos e femininos", "Uma música de um artista de Nova York", "Uma música de um artista de Los Angeles", "Uma música de um artista do Rio de Janeiro", "Ua música de um artista de Londres", "Uma música da carreira solo de um artista que é mais famoso como parte de uma banda", "Uma música de um artista que você acha atraente", "Uma música por um artista que também atue", "Uma música dê o nome ao álbum dela", "Uma música com um palavrão no título", "Uma música introspectiva", "Uma música que seja a última do álbum dela", "Uma música que te apresentou ao artista dela", "Uma música com o nome de um animal no título", "Uma música que te lembra do verão", "Uma música sobre um personagem fictício", "Uma música para pôr como seu despertador", "Uma música que te lembra do mar", "Uma música com um título longo", "Uma música que foi lançada quando o artista dela tinha menos de  anos", "Uma música que seja um collab improvável", "Uma música por um artista que foi preso", "Uma música de um artista do mundo árabe", "Uma música que combine muitos gêneros", "Uma música que te lembra do campo", "Uma música muito datada mas que você ainda ame", "Uma música sobre comércio", "Uma música sobre política", "Uma música que te lembra da cidade", "Uma música que você gosta mas não tem muita certeza de quem é o artista", "Uma música com um piano", "Uma música com o nome de um instrumento musical no título", "Uma música sobre parafilia", "Uma música que não soa como o artista se parece", "Uma música que não parece que foi feita pelo artista dela", "Uma música que parece que foi feita para atacar você", "Uma música que seja Purple Rain", "Uma música com um começo abrupto", "Uma música com um fim abrupto", "Uma música cujo começo seja a melhor parte", "Uma música cujo fim seja a melhor parte", "Uma música sobre tecnologia", "Uma música sexy", "Uma música para se ouvir na madrugada", "Uma música poética", "Uma música que você conheceu por ser sampleada por outra", "Uma música sobre trabalho", "Uma música que você goste de um artista que você não conheça muito", "Uma música sobre parafilia", "Uma música com dois artistas que cantam sobre coisas muito diferentes nela", "Uma música sobre família", "Uma música que flui para as adjacentes no álbum", "Uma música sobre juventude", "Uma música que fere a garganta do cantor", "Uma música que parece com a tocada antes", "Uma música que você gosta mas já não escuta faz muito tempo", "Uma música com um verso que você adore", "Uma música de um artista que você acha atraente", "Uma música cringy", "Um música sobre rompimento", "Uma música sobre ser o melhor", "Uma música sobre auto-desprezo", "Uma música sobre o oculto", "Uma música sem refrão", "Uma música com uma surpresa", "Uma música que você não entende o motivo de gostar tanto dela", "Uma música que seja meio gay", "Uma música para um dia ensolarado", "Uma música com um instrumento dominante incomum", "Uma música que reflita seu humor agora", "Uma música sobre eternidade", "Uma música sinistra", "Uma música que lhe foi apresentada pelos seus pais", "Uma música que lhe foi apresentada por uma namorada ou namorado", "Uma música na qual o cantor não canta em sua língua nativa", "Uma música letárgica", "Uma música animada", "Uma música com um interlúdio de silêncio", "Uma música que siga a estrutura verse-chorus-verse-chorus a risca", "Uma música com uma letra que você ame", "Uma música com modulação de voz", "Uma música com uso extensivo de backing vocals", "Uma música youtube-core", "Uma música para se tocar durante um piquenique", "Uma música com o nome de um monstro no título", "Uma música boa cantada por alguém que você não considera uma boa pessoa", "Uma música sobre casa", "Uma música sobre distância", "Uma música comum riff que você adore", "Uma música feminina", "Uma música masculina", "Uma música ritmicamente complexa", "Uma música com um crossover inesperado", "Uma música gravada ao vivo", "Uma música com uma figura mitológica no título", "Uma música com uma backstory interessante ", "Uma música de propaganda de carro", "Uma música com o nome de alguém famoso no título", "Uma música que tenha sido formativa para seu gosto", "Uma música que derreta o cérebro", "Uma música que você ame com um clipe que você deteste", "Uma música que tocaria na sua cinebiografia", "Uma música que te evoca sentimentos mistos intensos", "Uma música com um corpo celeste no título", "Uma música que você gostava ironicamente mas que passou a genuinamente adorar", "Uma música que te deixe arrepiado", "A música que você ouve enquanto você morte", "Uma música com um build up que você adore", "Uma música sobre vício", "Uma música sobre psicossexualidade", "Uma música que signifique muito pra voce", "Uma música séria", "Uma música poética", "Uma música propositalmente sem sentido", "Uma música que pede perdão", "Uma música que tenha sido formativa para seu gosto", "Uma música com uma palavra repetida no título", "Uma música que te encha de saudade", "Uma música que nenhum dos seus amigos adivinharia que voce gosta", "Uma música com uma profissão no título", "Uma música que te relaxe", "Uma música para ser tocada na primavera ", "Uma música para ser tocada no verão", "Uma música para ser tocada no outono", "Uma música para ser tocada no inverno", "Uma música de afterparty", "Uma música com uma assinatura de ritmo estranha", "Uma música sobre o sol", "Uma música sobre a lua", "Uma música que toca no paraíso", "Uma música que toca no inferno", "Uma música espasmódica", "Uma música que incorpora a gravação de uma conversa", "Uma música que é enriquecida por saber a história pessoal do artista", "Uma música sobre obsessão", "Uma música de um artista cuja história de vida tenha sido adaptada ao cinema", "Uma música QUALQUER!"]

# with open('sfuck.txt', 'a', encoding='utf-8') as the_file:
#     for q in question:
#         the_file.write(q + '\n')

file1 = open('sfuck.txt', 'r', encoding='utf-8')
Lines = file1.readlines()
 
count = 0
# Strips the newline character
for line in Lines:
    count += 1
    print("Line{}: {}".format(count, line.strip()))

usadas = []
prompt = "R: rerola | N: next | Q: quit -> "
total = len(question)

check = (len(usadas) < total)
print(check)
while check:
    n =  random.randrange(0, 299, 1)
    if question[n] not in usadas:
        print(question[n])
        i = input(prompt).lower()
        if i == "q":
            break
        if i == "n":
            usadas.append(n)
print("O jogo acabou! Voce jogou todas as muscias, como?")