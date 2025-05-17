**Desconhecido** _(2025-03-14 17:47:20)_
> Ah beleza. estou sim,. hj to tendo que ciidadr um pouco da minha mae . esta com a pressao altissima.. 
as vezes ela tem isso. Esperando baixar para voltar a acap

**Desconhecido** _(2025-03-13 11:44:25)_
> if(!isset($_GET['clin'])){
    echo 'ERRO DOWNLOAD';
    exit;
}

if(!isset($_GET['ambie'])){
    echo 'ERRO DOWNLOAD';
    exit;
}

**Desconhecido** _(2025-03-13 11:44:00)_
> // Configurações do banco de dados
$hostname = '10.0.10.159';
$username = 'leandro';
$password = '@ogp9BLMo!';
if($ambiente == "dev"){
    $database = 'copy_prod__growhats';
}else{
    $database = 'growhats';
}

**Desconhecido** _(2025-03-13 11:39:46)_
> 
[Anexo](https://cdn.discordapp.com/attachments/1308500919608147978/1349708515257618462/bkp_teste.php?ex=0&is=67fa03b3&hm=7507f10162c72ba996ffcbf1f4daac81a16b8e3a1933a06f8c4d1fd64115d1aa&uc=dp&)

**Desconhecido** _(2025-03-13 11:37:50)_
> 
[Anexo](https://cdn.discordapp.com/attachments/1308500919608147978/1349708027606859776/bkp_teste.php?ex=0&is=67fa03b3&hm=0a1fb3410ecbd9345e6cde382bde0abfcfc43befa7bc6160a27dd8dee387f921&uc=dp&)

**Desconhecido** _(2025-03-13 11:37:35)_
> 
[Anexo](https://cdn.discordapp.com/attachments/1308500919608147978/1349707967460544582/blank_gera_bkp.php?ex=0&is=67fa03b3&hm=d9ae77e7f7fe8b1540584f82fbad7fe83b0bccd070096e8275ccd393b377e3e4&uc=dp&)

**Desconhecido** _(2025-03-13 11:24:58)_
> 
[Anexo](https://cdn.discordapp.com/attachments/1308500919608147978/1349704791252664331/image.png?ex=0&is=67fa03b3&hm=48f1ca6ea98c0a22bc709c1e29faaad4abd64174a7861a437374e401cdade1d6&uc=dp&)

**Desconhecido** _(2025-03-13 11:22:08)_
> http://192.168.10.27:8081/scriptcase/app/SAAS_MULTI_GROW_V2/blank_gerar_bkp/?clin=1&ambie=dev

**Desconhecido** _(2025-03-12 19:13:33)_
> Ok

**Desconhecido** _(2025-03-12 19:11:22)_
> 
[Anexo](https://cdn.discordapp.com/attachments/1308500919608147978/1349459774579933266/voice-message.ogg?ex=0&is=67fa03b3&hm=979cf88b49e8d83dece23854214237af2d1044ad295d37025faa7209cde3ac3e&uc=dp&)

**Desconhecido** _(2025-03-12 19:07:16)_
> Tudo tranquilo acredito que entre amanhã e sexta

**Desconhecido** _(2025-03-12 18:27:29)_
> eh sobre o bkp certo?

**Desconhecido** _(2025-03-12 18:26:22)_
> Nao entendi a pergunta.. Eu estou atuando nos cards
Vou portar para blank apos

**Desconhecido** _(2025-03-12 17:19:24)_
> OK

**Desconhecido** _(2025-03-12 14:38:24)_
> Mas se for o caso transformo em uma blank sim

**Desconhecido** _(2025-03-12 14:37:52)_
> 

**Desconhecido** _(2025-03-12 14:26:26)_
> Descrição
• Alterações não salvas

Este card é uma sub-tarefa do card 274, onde foram relatados erros na geração do backup de clientes. 
O backup atualmente é executado via Cron e disponibilizado para download ao cliente, no arquivo é disponibilizado a lista de contatos do cliente assim como todos os atendimentos registrados(uma pasta para cada contato, e dentro da pasta do contato uma pasta para cada atendimento, onde possui o histórico de anexos e mensagens trocadas durante o atendimento),  ocorre que por vezes a execução do backup fica muito extensa e a tarefa não é concluída por falta de memória ou tempo limite de conexão, alguns backups exigem um trabalho manual de execução parcial das consultas dos registros em partes para geração dos arquivos e execução da compactação dos arquivos via prompt de comando no servidor.


Considerando isso surge a necessidade de melhorias de perfomance e/ou formato das execuções desta tarefa, vejo que um caminho é a execução parcial de geração das pastas, percorrendo X contatos por vez ao invés da lista completa de contatos a cada execução, isso resolveria problemas de não chegar ao fim da geração dos dados descompactados, outro problema é a geração do arquivo compactado, atualmente ela pode falhar devido ao tamanho do arquivo, notei que ocorre geralmente com backup acima dos 3gbs, para isso talvez o caminho seja a disponibilização de mais de um arquivo compactado e não um arquivo final apenas, de modo a dividir tbm essa carga de geração do arquivo compactado

**Desconhecido** _(2025-03-12 14:25:38)_
> Porque esse script e disparado de outro servidor.
Foi a orientacao que eu recebi

O originar e o gerar_bkp.php
E a versao bkp_teste.php
[Anexo](https://cdn.discordapp.com/attachments/1308500919608147978/1349387869592223755/gerar_bkp.php?ex=0&is=67fa03b3&hm=59ed364d69d053e80f599de4e45e7c9ee744ed5b1174bb28ea7b07ab8c821995&uc=dp& https://cdn.discordapp.com/attachments/1308500919608147978/1349387870003134574/bkp_teste.php?ex=0&is=67fa03b3&hm=64cdb93847b2435df25927ed5b13c0d00e22fd4b1f79be82f10bd1f5db87502f&uc=dp&)

**Desconhecido** _(2025-03-12 14:10:34)_
> php puro

**Desconhecido** _(2025-03-12 13:22:38)_
> https://growhats.atlassian.net/browse/BEM-409

**Desconhecido** _(2025-03-12 13:15:31)_
> Bom dia Ederson. Eu estou dando prioridade aos outros cards.
Vou colar o arquivo do bkp la no card

**Desconhecido** _(2025-03-10 12:34:50)_
> na verdade quem processa a variavel e essa api. e tenho de que fazer a validacao la.
Estou com o Vinicius

**Desconhecido** _(2025-03-10 12:07:21)_
> Entao esse e o caso. Nao consegui achar o arquivo que esta dando problema
[Anexo](https://cdn.discordapp.com/attachments/1308500919608147978/1348628293888249917/2f911048-653b-41c3-a41d-4c6f2d275a46.png?ex=0&is=67fa03b3&hm=bebef0d7dc33cadd3a3f0fab0a8d92f7506e7e345f2be6c5880784aba9650d94&uc=dp&)

**Desconhecido** _(2025-03-10 12:05:15)_
> Bom dia1

**Desconhecido** _(2025-03-09 19:06:11)_
> Ederson boa tarde esta por ai?
Rapaz eu nao consigo achar o script que esta dando erro . Referente a demanda que tem que ser entregue amanha!

Sera que  voce ou pode me ajudar a localizar ele amanha?>

**Desconhecido** _(2025-03-06 19:08:54)_
> e mais uma coisa .. se quisermos treinar maquinas fora dos modelos de mercado
e python

**Desconhecido** _(2025-03-06 19:08:18)_
> ano passado passeio o ano todo estudando python

**Desconhecido** _(2025-03-06 19:07:53)_
> e seria legal propor aos squads a lidar com python
vai por mim.

**Desconhecido** _(2025-03-06 19:06:54)_
> e eu nao pretendo sair assim tao cedo. rsrs
como nas conversas e agregar e caminhar junto

**Desconhecido** _(2025-03-06 19:06:05)_
> rsrs

**Desconhecido** _(2025-03-06 19:06:05)_
> e dev python tem as pencas por ai

**Desconhecido** _(2025-03-06 19:05:50)_
> mas blz .. ja esta em php

**Desconhecido** _(2025-03-06 19:05:41)_
> q nada. nao vou fugir.. python e muito tranquilo

**Desconhecido** _(2025-03-06 19:03:45)_
> criar microservicos em python

**Desconhecido** _(2025-03-06 19:03:35)_
> e que realmente as vezes e melhor sair do php

**Desconhecido** _(2025-03-06 19:03:16)_
> nao tem problema

**Desconhecido** _(2025-03-06 19:03:10)_
> ai ele disse que era pra manter o php

**Desconhecido** _(2025-03-06 19:03:03)_
> eu falei pra ele que ia fazer um modelo em py tbm

**Desconhecido** _(2025-03-06 19:02:28)_
> pois ai fica em 2o plano

**Desconhecido** _(2025-03-06 19:02:02)_
> tem que executar via crontab

**Desconhecido** _(2025-03-06 19:01:50)_
> Outro ponto sobre esse servico e que ele e executa manualmente via web
Ele deveria so rodar 1 o 2 vezes ao dia
Loucura ficar processando de 1 em 1 hora

**Desconhecido** _(2025-03-06 19:00:43)_
> mas o Diogo nao topou

**Desconhecido** _(2025-03-06 19:00:35)_
> ele muito melhor pra processar grandes demandas de dados , analisar e agrupar
fora que ainda temos bibliotecas para paralelismo que aumenta a eficiencia alem

**Desconhecido** _(2025-03-06 18:59:49)_
> pela que ele faz o python e ideal

**Desconhecido** _(2025-03-06 18:59:38)_
> em php

**Desconhecido** _(2025-03-06 18:59:33)_
> nao.

**Desconhecido** _(2025-03-06 18:56:28)_
> Mas eu nao sei em que lugar ou servidor ele e executado

**Desconhecido** _(2025-03-06 18:56:05)_
> Um shell e uma pasta samba seriam ideias

**Desconhecido** _(2025-03-06 18:55:36)_
> E eu realmente preciso testar no ambiente
A questao dos arquivos dos chats que ele anexa e algo que eu nao consigo controlar aqui

**Desconhecido** _(2025-03-06 18:54:46)_
> Oi Ederson sera que voce consegue me liberar o acesso ao ambiente que o arquivo gerar_bkp.php roda . eu so vou conseguir testar mesmo no ambiente dele para validar se houve ou nao melhoria no desembenho bem como se o codigo vai rodar sem erros 

o gerar_bkp.php e o original
o bkp_test.php e a nova versao

E o gerar_bkp.py era o comeco do meu port .
pois Python e muito mais eficiente para esses processo
[Anexo](https://cdn.discordapp.com/attachments/1308500919608147978/1347281272442978304/bkp_test.php?ex=0&is=67fa03bc&hm=cd752e8c1bc8e80b84a0538c494609cf33d72d3eac07480b7606204eaa6a8f9c&uc=dp& https://cdn.discordapp.com/attachments/1308500919608147978/1347281272950493244/gerar_bkp.php?ex=0&is=67fa03bc&hm=497e697037fe0bed2a399fd7674d59dd4b9fd81662eaf17ad00d3a13b0e10e6e&uc=dp& https://cdn.discordapp.com/attachments/1308500919608147978/1347281273374113833/gerar_bkp.py?ex=0&is=67fa03bc&hm=b5063d23f04a18810cafd64418278eb08e4014e023dbca3aad3639b7090c13b9&uc=dp&)

**Desconhecido** _(2025-03-06 13:05:56)_
> 473 474 e que estou no chuveiro.  Kk

**Desconhecido** _(2025-03-06 11:50:00)_
> Oi Ederson entao acabei de testar a inclusao de cliente para um funil e tudo ok
[Anexo](https://cdn.discordapp.com/attachments/1308500919608147978/1347174375115329577/image.png?ex=0&is=67fa03bc&hm=607cf4b87edca6c1b4b50dee0590d8646319acc8eca59bbbfd1f974b19568a00&uc=dp&)

**Desconhecido** _(2025-01-30 22:22:59)_
> Oi Ederson tudo joia. No jira só tem 1 que comecei atuar e mais 2 que já entraram para finalização. Mas eu preenchi todas as infos referente a tempo.
De quais vc esta se referindo

**Desconhecido** _(2025-01-24 19:28:40)_
> sem acesso ainda
[Anexo](https://cdn.discordapp.com/attachments/1308500919608147978/1332431900853276743/image.png?ex=0&is=67fa03c4&hm=dd9adda6ffdab49e15027e72e1d98a5491edb4135ed8defc36d44d9e5cd0b589&uc=dp&)

**Desconhecido** _(2025-01-24 19:28:32)_
> agora sim

**Desconhecido** _(2025-01-24 19:27:04)_
> Acabei de tentar e nao rolou, Vou refazer o login

**Desconhecido** _(2025-01-24 18:23:17)_
> Legal. O Diogo me reportou também que estava sem acesso

**Desconhecido** _(2025-01-24 18:17:18)_
> Ederson boa tarde. Como vai? 
Perdi todo o meu acesso ao jira. Nem tentando logar novamente resolveu.
Meu email e renebmjr@gmail.com 

Obrigado

**Desconhecido** _(2025-01-05 13:01:19)_
> Ederson Bom dia ! Como vai. 
E so um comentário sobre segurança no formulário de despesas. Eu preenchi agora no último dia 3 e depois do processo lembrei que precisava adicionar algo no campo Descrição.  Ai pedi para editar e vi que o campo estava disable. Aí removi no console do navegador o disable fiz a alteração que era adicionar minha chave pix e pra minha não tão surpresa ele gravou a informação.
Acredito que não seja algo crítico como vulnerabilidade. Mas e possível alterar a informação anteriormente preenchida.  Se ele foi feito via scrptcase ele no afterUpdate vai identificar que o campo foi alterado e fazer o update do campo hora

**Desconhecido** _(2024-12-26 16:59:53)_
> rssrs

**Desconhecido** _(2024-12-26 16:58:07)_
> Ontem eu estava entediado e finalizei a unica que tinha

**Desconhecido** _(2024-12-26 16:57:49)_
> Sem tarefas desde a manha

**Desconhecido** _(2024-12-26 16:57:41)_
> Boa tarde Ederson!  Tudo otimo. Espero que esteja bem tbm

**Desconhecido** _(2024-12-12 11:21:43)_
> perfeito

**Desconhecido** _(2024-12-12 11:21:30)_
> ok

**Desconhecido** _(2024-12-12 10:25:35)_
> E assm . Da um sensação de derrota .. Pois apesar de estar 100% colocam o card em um local de erro 'Teste Rejeitado`

**Desconhecido** _(2024-12-12 10:22:10)_
> E acrediro que esse tipo de problema prejudique o fluxo normal da sprint

**Desconhecido** _(2024-12-12 10:21:23)_
> E isso esta ocorrendo com um card meu o BEM-102. Ele pedia uma correcao que foi efetuada rapidamente. E o pessoal de teste deu que a correcao foi ok. Mas para a minha surpresa eles voltaram o card com erro e pedindo uma nova solicitacao. Eu tentei argumentar que nao era esse o caminho. Mas eles ignoraram

**Desconhecido** _(2024-12-12 10:19:56)_
> Outra curiosidade. Lembro que voce comentou que nao se pode adicionar uma nova solicitacao dentro de uma solicitacao ja entregeu e ok

**Desconhecido** _(2024-12-12 10:18:20)_
> Como proceder com o novo lancamento de horas na sprint?

**Desconhecido** _(2024-12-12 10:17:56)_
> Muitas vezes acontece de ter feito o sprint. Colocado em code review e o Diogo lembrar que precisa algum acerto . Ou nao ficou completamente correto,
Ou na fase de teste o teste e rejeitado por algum motivo

**Desconhecido** _(2024-12-12 10:16:50)_
> Como alguns cards as vezes voltam. Poderia ser esse o problema?

**Desconhecido** _(2024-12-12 10:16:27)_
> Start Date , End Date
E depois lanco na opcao Registrar trabalho com as horas que eu levei no sprint

**Desconhecido** _(2024-12-12 10:15:23)_
> deixa eu falar quais. as vezes estou procedendo errado

**Desconhecido** _(2024-12-12 10:15:06)_
> perfeito.. mas eu tenho lancado em 2 lugares

**Desconhecido** _(2024-12-12 10:14:37)_
> ah pode deixar.. Voce consegue os ids dos cards? Que ai consigo achar na busca!?

**Desconhecido** _(2024-12-12 10:13:51)_
> obrigado por perguntar

**Desconhecido** _(2024-12-12 10:13:46)_
> Melhorei.. voltei a tarde para as atividades

**Desconhecido** _(2024-12-12 10:07:08)_
> Ederson bom dia. Sem os codigos dos cards que estao com inconsistencia eu nao consigo editar. A maioria dos meus cards ja sairam do fluxo

**Desconhecido** _(2024-11-21 15:46:18)_
> tranquilo! rsrsrs

**Desconhecido** _(2024-11-21 15:29:48)_
> e esto cuidando de um novo

**Desconhecido** _(2024-11-21 15:29:40)_
> eu lancei os dois do dia 18

**Desconhecido** _(2024-11-21 15:29:30)_
> ontem foi feriado..

**Desconhecido** _(2024-11-21 14:58:07)_
> Fiz a complementacao la no Registro

**Desconhecido** _(2024-11-21 14:57:56)_
> Acho que agora esta ok

**Desconhecido** _(2024-11-21 14:55:33)_
> vou verificar

**Desconhecido** _(2024-11-21 14:53:46)_
> Oi Ederson bom dia! Eu determinei o tempo estimado o tempo decorrido. So nao achei a tela timesheet . Nao consegui acessar ela.

**Desconhecido** _(2024-11-19 18:37:32)_
> No que posso ajudarr?

**Desconhecido** _(2024-11-19 18:35:49)_
> Oi Ederson tudo bem! Boa tarde
