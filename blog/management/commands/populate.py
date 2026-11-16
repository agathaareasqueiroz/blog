import random

from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from datetime import datetime
from django.utils import timezone
from blog.models import Post


class Command(BaseCommand):

    help = 'Cria postagens fictícias para testes'

    def handle(self, *args, **options):

        # Verifica se já existem postagens
        if Post.objects.exists():
            self.stdout.write(
                self.style.WARNING(
                    'Já existem postagens cadastradas. Nada foi criado!'
                )
            )
            return

        # Recupera os usuários cadastrados
        User = get_user_model()
        users = list(User.objects.all())

        # Verifica se existem usuários
        if not users:
            self.stdout.write(
                self.style.ERROR(
                    'Nenhum usuário cadastrado!'
                )
            )
            return

        # Dados fictícios
        posts = [
            {
                'title': 'Por que o café não compila?',
                'summary': 'Uma análise profunda sobre a cafeína e o código.',
                'textbody': 'Porque faltou Java! Descubra como transformar 3 xícaras de espresso em 500 linhas de código sem bugs (ou quase isso).',
            },
            {
                'title': 'O mistério do "Funciona na minha máquina"',
                'summary': 'Um clássico do desenvolvimento de software.',
                'textbody': 'Se funciona na sua máquina, a solução é simples: vamos enviar a sua máquina para o cliente e colocá-la em produção!',
            },
            {
                'title': 'A vida secreta do CSS',
                'summary': 'Tentando centralizar uma div desde 1995.',
                'textbody': 'Adicionei margin: auto, position: absolute, flexbox e grid. A div continua no canto superior esquerdo e a página agora tem scroll infinito.',
            },
            {
                'title': '1001 maneiras de nomear variáveis',
                'summary': 'De temp1 a data_final_oficial_v2_final.',
                'textbody': 'Pesquisas apontam que 90% do tempo de um programador é gasto pensando em nomes para variáveis e os outros 10% caçando um ponto e vírgula.',
            },
            {
                'title': 'O ataque das 30 abas do Stack Overflow',
                'summary': 'Como resolver um erro colando código sem ler.',
                'textbody': 'Copiou, colou, funcionou! Ninguém sabe o motivo, nem o autor do código, mas o importante é dar commit antes que quebre de novo.',
            },
            {
                'title': 'Existem 10 tipos de pessoas no mundo',
                'summary': 'Uma piada binária para aquecer o coração.',
                'textbody': 'As que entendem código binário e as que não entendem. E as que não esperavam que essa piada estivesse na base 3!',
            },
                        {
                'title': 'O programador que queria dormir cedo',
                'summary': 'Só mais um pequeno ajuste antes de encerrar o dia.',
                'textbody': 'Eram 22h quando ele abriu o VS Code para corrigir um detalhe. Quando olhou novamente para o relógio, eram 4h da manhã e ele estava reescrevendo o sistema inteiro em outra linguagem.',
            },
            {
                'title': 'A vingança do ponto e vírgula',
                'summary': 'Um pequeno caractere, um grande estrago.',
                'textbody': 'Passei duas horas procurando um erro no código. No final, faltava um ponto e vírgula. O pior? Ele estava me olhando o tempo todo!',
            },
            {
                'title': 'O cliente pediu só uma coisinha',
                'summary': 'As famosas alterações simples que mudam tudo.',
                'textbody': 'Era só mudar a cor de um botão. Depois vieram o novo layout, o sistema de login, o painel administrativo e uma integração com inteligência artificial. Tudo para ontem, claro!',
            },
            {
                'title': 'Git: o diário das decisões duvidosas',
                'summary': 'Uma história de amor, ódio e conflitos.',
                'textbody': 'Meu commit dizia "pequenos ajustes". O próximo dizia "corrigindo os pequenos ajustes". O seguinte: "desfazendo tudo". E o último: "agora vai, confia!".',
            },
            {
                'title': 'O banco de dados está de mau humor',
                'summary': 'Quando o SQL resolve responder atravessado.',
                'textbody': 'Fiz uma consulta SELECT e recebi 15 mil registros. Fiz um UPDATE sem WHERE e recebi uma nova personalidade: a de alguém que faz backup todos os dias!',
            },
            {
                'title': 'A inteligência artificial também erra',
                'summary': 'Quando até o robô precisa de férias.',
                'textbody': 'Pedi para a IA criar um código simples, eficiente e sem bugs. Ela respondeu com 300 linhas de código, três dependências desconhecidas e a sugestão de procurar um programador humano.',
            },
            {
                'title': 'O misterioso desaparecimento da internet',
                'summary': 'O terror de todo desenvolvedor web.',
                'textbody': 'Tudo funcionava perfeitamente até a internet cair. Foi nesse momento que descobri que meu sistema dependia de 47 bibliotecas externas, 12 APIs e uma fonte do Google Fonts.',
            },
            {
                'title': 'A reunião que poderia ser um comentário',
                'summary': 'Mais uma aventura no mundo corporativo.',
                'textbody': 'Foram duas horas de reunião para decidir o nome de uma variável. No final, alguém sugeriu "data" e todos concordaram. O programador já tinha usado esse nome no primeiro minuto.',
            },
            {
                'title': 'CSS: agora vai!',
                'summary': 'A eterna batalha entre desenvolvedor e navegador.',
                'textbody': 'Finalmente consegui deixar o site bonito no Chrome. Abri no Firefox e estava tudo torto. Abri no Safari e desapareceu metade da página. Abri no celular e descobri uma nova dimensão do sofrimento.',
            },
            {
                'title': 'O deploy de sexta-feira',
                'summary': 'Uma decisão que pode mudar seu fim de semana.',
                'textbody': 'O chefe perguntou se poderíamos publicar uma pequena atualização na sexta-feira à tarde. Respondi que sim. Desde então, meu sábado tem sido dedicado a descobrir por que o servidor decidiu tirar férias.',
            },
        ]

        # Cria as postagens
        for data in posts:

            randon_image = random.randint(1, 100)
            post = Post.objects.create(
                user=random.choice(users),
                title=data['title'],
                created_at=self.random_date(),
                summary=data['summary'],
                textbody=data['textbody'],
                thumbnail=f'https://picsum.photos/800/450?random={randon_image}',
                is_active=True,
                is_deleted=False,
            )

            self.stdout.write(
                self.style.SUCCESS(
                    f'Post criado: {post.title} (ID: {post.id})'
                )
            )

        self.stdout.write(
            self.style.SUCCESS(
                'População concluída com sucesso!'
            )
        )

    @staticmethod
    def random_date(start_date="2026-01-01 00:00:00"):

        start = datetime.strptime(start_date, "%Y-%m-%d %H:%M:%S")
        now = datetime.now()

        random_timestamp = random.randint(
            int(start.timestamp()),
            int(now.timestamp())
        )

        return timezone.make_aware(
            datetime.fromtimestamp(random_timestamp)
        )