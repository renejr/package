**Desconhecido** _(2025-03-21 13:44:27)_
> // Configuração de máscaras e validações para os campos do formulário (exemplo já existente)
    camposConfig.forEach((campo) => {
        let selector = `[name="${campo.nome.toLowerCase().replace(/\s/g, "_")}"]`;
        if ($(selector).length) {
            let campoAtual = $(selector);
            if (campo.nome.toLowerCase().includes("moeda")) {
                campoAtual.mask("#.##0,00", { reverse: true });
                campoAtual.attr("inputmode", "numeric");
            } else if (campo.mascara && campo.tipo !== 'date' && campo.tipo !== 'datetime-local') {
                campoAtual.mask(campo.mascara);
            }
            if (campo.atributos) {
                let atributos = JSON.parse(campo.atributos);
                Object.keys(atributos).forEach((key) => {
                    campoAtual.attr(key, atributos[key]);
                });
            }
            if (campo.tipo === 'date' || campo.tipo === 'datetime-local') {
                campoAtual.on('change', function() {
                    campoAtual.val($(this).val());
                });
            }
        }
    });

**Desconhecido** _(2025-03-21 13:32:40)_
> https://homolog.multi-atendimento.net.br/cadastrar/?c=MQ==

**Desconhecido** _(2024-12-11 18:59:43)_
> ../_lib/externa/img_perfil/cliente_1/cel_120363376901163735.jpg?ver=1733943403

**Desconhecido** _(2024-11-28 12:08:23)_
> if({foto} != ''){
    
    if(!file_exists({foto}) OR filesize({foto}) == 0){
        {foto} = "../_lib/img/icon_group.png";
        {img_foto} =  '<img class="img avatar" src="../_lib/img/icon_group.png">';
        $foto_com_ver = {foto} . '?ver=' . time();
        sc_exec_sql("UPDATE lista_grupos_zap SET foto = '".$foto_com_ver."' WHERE id_cliente = ".[id_clien]." AND id_grupo_zap ='".{id_grupo_zap}."'");
        sc_commit_trans();
    }else{
        {img_foto} =  '<img class="img avatar" src="'.{foto}.'">';
    }
}else{
    {foto} = "../_lib/img/icon_group.png";
    {img_foto} =  '<img class="img avatar" src="../_lib/img/icon_group.png">';
    $foto_com_ver = {foto} . '?ver=' . time();
    sc_exec_sql("UPDATE lista_grupos_zap SET foto = '".$foto_com_ver."' WHERE id_cliente = ".[id_clien]." AND id_grupo_zap ='".{id_grupo_zap}."'");
    sc_commit_trans();
}

if({descricao} == ""){
    $retorno_desc = membro_dos_grupos([id_cliente],$statusResult['id'],{id_grupo_zap});
    if(isset($retorno_desc['descricao'])){
        {descricao} = $retorno_desc['descricao'];
        sc_exec_sql("UPDATE lista_grupos_zap SET descricao = '".{descricao}."' WHERE id_cliente = ".[id_clien]." AND id_grupo_zap ='".{id_grupo_zap}."'");
        sc_commit_trans();
    }
    
}
$retornoPermissao = adminGrupo({id_grupo_zap},{numero_emparelhado},$statusResult);

**Desconhecido** _(2024-11-26 12:04:29)_
> $sql_msg_data = "
        SELECT
            id_grupo,
            MAX(conteudo_msg) AS ultima_msg,
            MAX(CAST(CONCAT(DATA, ' ', hora) AS DATETIME)) AS ultima_datahora,
            COUNT(CASE WHEN msg_lida = 'N' THEN 1 END) AS msgs_nao_lidas,
            COUNT(*) AS total_msgs,
            tipo_chat
        FROM group_historicos
        WHERE id_cliente = " . [id_clien] . "
        GROUP BY id_grupo
    ";
    sc_select(dataset_mensagens, $sql_msg_data);

**Desconhecido** _(2024-11-26 12:00:16)_
> SELECT 
            g.id_grupo_zap, 
            g.nome, 
            g.numero_emparelhado, 
            g.foto, 
            m.nome_canal, 
            m.cor_canal, 
            m.id, 
            g.ids_etiquetas,
            triagens.status_atendimento,
            triagens.atendente
        FROM lista_grupos_zap g
        INNER JOIN instancias m ON g.numero_emparelhado = m.numero_zap AND g.id_cliente = m.id_cliente
        INNER JOIN (
            SELECT 
                id_grupo, 
                MAX(CAST(CONCAT(`data`, ' ', `hora`) AS DATETIME)) AS `datahora` 
            FROM group_historicos 
            GROUP BY id_grupo
        ) h ON h.id_grupo = g.`id_grupo_zap`
        LEFT JOIN chatbot_triagem_grupos AS triagens 
            ON triagens.id_grupo = g.id_grupo_zap 
            AND g.id_cliente = triagens.id_cliente 
            AND triagens.status_atendimento IN ('AA', 'AE') 
        WHERE g.situacao = 1 
            AND g.id_cliente = " . [id_clien] . " 
            $sql_add_where_permissoes_grupos
        GROUP BY g.id_grupo_zap
        ORDER BY h.datahora DESC

**Desconhecido** _(2024-11-26 11:33:11)_
> DIOGO FRAGA GUZENSKI 
há 4 dias

Inicialmente vamos realizar uma analise dos selects existentes na listagem de grupos e fazer levantamento de melhorias a serem realizadas a fim de aumentar a perfomance das consultas que atualmente é fortemente afetada pela quantidade de grupos a serem consultados. 

Aplicação: Blank_chat_backend
Método: listar_grupos

**Desconhecido** _(2024-11-22 19:41:52)_
> webhook_wh_message

**Desconhecido** _(2024-11-22 19:02:11)_
> tel do bot: 555198724163

**Desconhecido** _(2024-11-22 13:56:59)_
> logica antiga
[Anexo](https://cdn.discordapp.com/attachments/844361758012342302/1309517993562079283/message.txt?ex=0&is=67fa03b9&hm=adbabf939408f39a34709ef1a495371d9b434ea0c470ece48951a47b9d38964c&uc=dp&)

**Desconhecido** _(2024-11-22 13:53:28)_
> webhook_wh_message

E dentro dele voce abre o metodo php: verificar_horario

**Desconhecido** _(2024-11-21 17:37:11)_
> eh isso
[Anexo](https://cdn.discordapp.com/attachments/844361758012342302/1309211022367920209/image.png?ex=0&is=67fa03b9&hm=36a7e83842d6b80158fe0650a79e65e93a84d775a825d5d8ee7d896fc163b544&uc=dp&)

**Desconhecido** _(2024-11-21 14:17:50)_
> hoplon

**Desconhecido** _(2024-11-21 14:02:20)_
> time
[Anexo](https://cdn.discordapp.com/attachments/844361758012342302/1309156953116905623/image.png?ex=0&is=67fa03b9&hm=cc6739fba2d4650590f484a4d57334162af47933c2136c3ee9210750dd85f416&uc=dp&)

**Desconhecido** _(2024-11-21 13:33:59)_
> para sincronizar as novas colunas
[Anexo](https://cdn.discordapp.com/attachments/844361758012342302/1309149816978407434/image.png?ex=0&is=67fa03b9&hm=a7ab4801f639256401b55ddca7457ac50f3fc65dae077c6afabf0a510c229e6c&uc=dp&)

**Desconhecido** _(2024-11-18 18:36:42)_
> https://chatgpt.com/share/673b8480-a6a4-8012-bf13-a289a45f1876

**Desconhecido** _(2024-11-18 13:48:08)_
> Esse e o que deve ir no scriptInit para o grid_url

**Desconhecido** _(2024-11-18 13:47:49)_
> alertaTutorial('Formulário Botões', '');

function alertaTutorial($titulo, $mensagem){
    $font = "font-family: 'Nunito', sans-serif !important;";
    echo '
      <h2>'.$titulo.' <i class="fas fa-exclamation-circle"  data-toggle="tooltip" data-placement="right" title="'.$mensagem.'" style="font-size: 20px;color: #2185d0;"></i></h2>
    ';
    
}

?>

<style>
.scFormDataOdd {
    padding: 0px 4px !important;
}
.scGridLabelFont {
    padding: 3px 15px !important;
}
.scGridFieldEvenFont, .scGridFieldOddFont {
    padding: 4px 15px !important;
}
.scGridFieldOddFont, .scGridFieldEvenFont {
    vertical-align: middle !important;
}
.scGridToolbarPadding {
    padding: 0px !important;
}
.scGridBorder {
    border-color: #FFF !important;
}
    
#TB_window {
    margin: auto !important;
    position: absolute;
    top: 50%;
    left: 50%;
    margin-right: -50%;
    transform: translate(-50%, -50%)
}

#TB_iframeContent{
    width: 100% !important;
    height: 75dvh !important;
}

</style>

<?php

**Desconhecido** _(2024-11-18 13:03:08)_
> 
[Anexo](https://cdn.discordapp.com/attachments/844361758012342302/1308054889703936091/image.png?ex=0&is=67fa03be&hm=6ced5faf7c728d619da222003ee0c515dd34fa0979c66c93c89c20cbd3734c94&uc=dp&)

**Desconhecido** _(2024-11-14 18:03:52)_
> Castlevania gratis
[Anexo](https://cdn.discordapp.com/attachments/844361758012342302/1306681019553808465/image.png?ex=0&is=67fa03be&hm=8f022d3f403a2e4e281d44f50ce17b3aad8c5a23d404bb8c4a915c12be160712&uc=dp&)

**Desconhecido** _(2024-11-14 16:54:31)_
> // Armazena os valores das variáveis
$url_webhook = $_POST['url_webhook'];
$token = $_POST['token'];

// Remove os elementos do array $_POST
unset($_POST['url_webhook']);
unset($_POST['token']);

// Agora, $_POST não contém mais 'url_webhook' e 'token'

**Desconhecido** _(2024-11-13 19:12:30)_
> // Serializa os dados do formulário como um array de objetos {name, value}
                const dadosArray = $("form").serializeArray();

                // Converte o array para um objeto JSON
                const dadosFormulario = {};
                dadosArray.forEach(item => {
                    dadosFormulario[item.name] = item.value;
                });

                // Transforma o objeto em uma string JSON
                const dadosFormularioJSON = JSON.stringify(dadosFormulario);
                
                // Envio via AJAX 
                $.ajax({
                    url: webhook.url_webhook,
                    method: "POST",
                    headers: { "Authorization": 'Bearer ' + webhook.token },
                    contentType: "application/json", // Define o tipo do conteúdo como JSON
                    data: dadosFormularioJSON // Envia os dados como JSON
                });

**Desconhecido** _(2024-11-13 17:23:35)_
> Rene Jr

**Desconhecido** _(2024-11-13 17:23:27)_
> Rene Ballesteros Machado Junior

**Desconhecido** _(2024-11-13 12:35:45)_
> SELECT GROUP_CONCAT(tc.nome ORDER BY tc.campo_obrigatorio SEPARATOR ', ') AS nomes
FROM tbl_webhook tw
INNER JOIN tbl_campos tc ON FIND_IN_SET(tc.id, tw.campos_obrigratorios) > 0
WHERE tc.id_cliente = [id_clien];

**Desconhecido** _(2024-11-13 11:45:47)_
> $check_sql = "
    SELECT
        tc.*,
        ttc.*
    FROM
        tbl_campos tc
    INNER JOIN tbl_tipos_campos ttc ON
        ttc.id = tc.tipo_da_informacao
    WHERE
        id_cliente = '" . [id_clien] . "' 
        AND FIND_IN_SET($departamento, departamento);
";

**Desconhecido** _(2024-11-12 18:28:56)_
> CREATE TABLE tbl_acoes_formulario (
    id INT PRIMARY KEY AUTO_INCREMENT,
    id_cliente INT NOT NULL,
    nome_botao_enviar VARCHAR(255) NOT NULL,
    url_envio_formulario VARCHAR(255) NOT NULL,
    CONSTRAINT fk_id_cliente FOREIGN KEY (id_cliente) REFERENCES tbl_clientes(id)
);

**Desconhecido** _(2024-11-12 17:11:15)_
> mandou isso
[Anexo](https://cdn.discordapp.com/attachments/844361758012342302/1305943003323695115/image.png?ex=0&is=67fa03be&hm=b7c17afb8937158061e998b16fab1772e47afa1f9a8cfc70ad063cbd94f42838&uc=dp&)

**Desconhecido** _(2024-11-11 13:45:02)_
> Authorization: Bearer 16d1f56a2f894b788de1bc7a4e9cde47

**Desconhecido** _(2024-11-11 13:25:05)_
> codeium

**Desconhecido** _(2024-11-11 13:09:14)_
> http://192.168.10.27:8081/scriptcase/app/SAAS_MULTI_GROW_V2/blank_api_teste/?nmgp_outra_jan=true&nmgp_start=SC&3431

**Desconhecido** _(2024-11-11 11:49:20)_
> // Query SQL
$check_sql = "
    SELECT
        tc.*,
        ttc.*
    FROM
        tbl_campos tc
    INNER JOIN tbl_tipos_campos ttc ON
        ttc.id = tc.tipo_da_informacao
    WHERE
        id_cliente = '" . sc_sql_injection([id_clien]) . "' 
        AND FIND_IN_SET($departamento, departamento);
";

sc_select(rs, $check_sql);

**Desconhecido** _(2024-11-08 16:48:50)_
> codigo da blank atualizado
[Anexo](https://cdn.discordapp.com/attachments/844361758012342302/1304487813248585820/message.txt?ex=0&is=67fa03c7&hm=78839fa1e7a0a93bfc720060c84bd8f0afda3863193aae32395b29946dd8fa73&uc=dp&)

**Desconhecido** _(2024-11-08 14:30:24)_
> SELECT 
    tbl_campos.id AS campo_id,
    tbl_campos.id_cliente,
    tbl_campos.nome AS campo_nome,
    tbl_campos.nome_integracao,
    tbl_campos.tipo_da_informacao,
    tbl_campos.limite_de_caracteres,
    tbl_campos.departamento,
    tbl_campos.dependencias,
    tbl_campos.url_informacoes,
    tbl_tipos_campos.id AS tipo_id,
    tbl_tipos_campos.nome AS tipo_nome,
    tbl_tipos_campos.tipo AS tipo_tipo,
    tbl_tipos_campos.descricao,
    tbl_tipos_campos.placeholder,
    tbl_tipos_campos.maxlength,
    tbl_tipos_campos.min_value,
    tbl_tipos_campos.max_value,
    tbl_tipos_campos.pattern,
    tbl_tipos_campos.required,
    tbl_tipos_campos.atributos,
    tbl_tipos_campos.mascara
FROM 
    tbl_campos
LEFT JOIN 
    tbl_tipos_campos 
ON 
    tbl_campos.tipo_da_informacao = tbl_tipos_campos.id;

**Desconhecido** _(2024-11-08 13:11:58)_
> // Código PHP completo no evento onExecute da aplicação Blank
echo '
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Aplicação Blank com jQuery Mask</title>

        <!-- Incluindo jQuery via CDN -->
        <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>

        <!-- Incluindo jQuery Mask via CDN -->
        <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery.mask/1.14.16/jquery.mask.min.js"></script>

        <!-- Código JavaScript para aplicar a máscara -->
        <script>
            $(document).ready(function(){
                $("#cpf").mask("000.000.000-00");
                $("#telefone").mask("(00) 00000-0000");
            });
        </script>
    </head>
    <body>
        <div style="margin: 20px;">
            <form method="POST" action="">
                <label for="cpf">CPF:</label>
                <input type="text" id="cpf" name="cpf" placeholder="000.000.000-00"><br><br>

                <label for="telefone">Telefone:</label>
                <input type="text" id="telefone" name="telefone" placeholder="(00) 00000-0000"><br><br>

                <input type="submit" value="Enviar">
            </form>
        </div>
    </body>
    </html>
';

**Desconhecido** _(2024-11-07 20:05:05)_
> function limparString($string) {
    // Remove caracteres especiais, números e acentos
    $string = preg_replace('/[^a-zA-Z ]/', '', $string);

    // Converte para minúsculas
    $string = strtolower($string);

    // Remove espaços em branco do início e fim da string
    $string = trim($string);

    // Verifica se há caracteres especiais no final e os remove
    $string = rtrim($string, ' -_');

    return $string;
}

// Exemplo de uso
$texto = "Olá-mundo! 123_áÇ";
echo limparString($texto); // Saída: "olamundo"

**Desconhecido** _(2024-11-07 18:30:40)_
> segue o arquivo
[Anexo](https://cdn.discordapp.com/attachments/844361758012342302/1304151048730050712/message.txt?ex=0&is=67fa03c7&hm=92f6f89e701c6845332832d44d549f8ac2bbd28ed7ca4a7e95af14a03bc000b7&uc=dp&)

**Desconhecido** _(2024-11-07 18:26:52)_
> https://g.co/verifyaccount
[Anexo](https://cdn.discordapp.com/attachments/844361758012342302/1304150095628996738/image.png?ex=0&is=67fa03c7&hm=ef8465cd65f064eb5706937780b2d5290fdfd3cca36ba1098c60b4828b5acfdc&uc=dp&)

**Desconhecido** _(2024-11-07 18:21:10)_
> https://chatgpt.com/share/672d04ed-c520-8000-9eda-fb90038d2f95

**Desconhecido** _(2024-11-07 17:50:01)_
> https://chatgpt.com/share/672cfdbb-f018-8000-a300-cb3f83d27a50

**Desconhecido** _(2024-11-07 14:14:43)_
> $(document).ready(function(){
  $('.date').mask('00/00/0000');
  $('.time').mask('00:00:00');
  $('.date_time').mask('00/00/0000 00:00:00');
  $('.cep').mask('00000-000');
  $('.phone').mask('0000-0000');
  $('.phone_with_ddd').mask('(00) 0000-0000');
  $('.phone_us').mask('(000) 000-0000');
  $('.mixed').mask('AAA 000-S0S');
  $('.cpf').mask('000.000.000-00', {reverse: true});
  $('.cnpj').mask('00.000.000/0000-00', {reverse: true});
  $('.money').mask('000.000.000.000.000,00', {reverse: true});
  $('.money2').mask("#.##0,00", {reverse: true});
  $('.ip_address').mask('0ZZ.0ZZ.0ZZ.0ZZ', {
    translation: {
      'Z': {
        pattern: /[0-9]/, optional: true
      }
    }
  });
  $('.ip_address').mask('099.099.099.099');
  $('.percent').mask('##0,00%', {reverse: true});
  $('.clear-if-not-match').mask("00/00/0000", {clearIfNotMatch: true});
  $('.placeholder').mask("00/00/0000", {placeholder: "__/__/____"});
  $('.fallback').mask("00r00r0000", {
      translation: {
        'r': {
          pattern: /[\/]/,
          fallback: '/'
        },
        placeholder: "__/__/____"
      }
    });
  $('.selectonfocus').mask("00/00/0000", {selectOnFocus: true});
});

**Desconhecido** _(2024-11-07 14:10:28)_
> https://igorescobar.github.io/jQuery-Mask-Plugin/docs.html

**Desconhecido** _(2024-11-06 18:50:05)_
> tbl_campos
id(id), id_cliente(id), nome(varchar), nome_integracao(varchar), mascara(varchar), tipo_da_informacao(varchar), limite_de_caracteres(int), departamento(varchar), dependencias(varchar), url_informacoes(mediumtext)


tbl_webhook
id(int),  id_cliente(int), url_webhook(varchar), token(varchar), titulo_botao(varchar), campos_obrigratorios(varchar)

**Desconhecido** _(2024-11-06 18:48:38)_
> tbl_campos
id(id), id_cliente(id), nome(varchar), nome_integracao(varchar), mascara(varchar), tipo_da_informacao(varchar), limite_de_caracteres(int), departamento(varchar), dependencias(varchar), informacoes(mediumtext)


tbl_webhook
id(int),  id_cliente(int), url_webhook(varchar), token(varchar), titulo_botao(varchar), campos_obrigratorios(varchar)

**Desconhecido** _(2024-11-06 18:45:50)_
> tbl_campos
id(id), id_cliente(id), nome(varchar), nome_integracao(varchar), mascara(varchar), tipo_da_informacao(varchar), limite_de_caracteres(int), departamento(varchar), dependencias(varchar)


tbl_webhook
id(int),  id_cliente(int), url_webhook(varchar), token(varchar), titulo_botao(varchar), campos_obrigratorios(varchar)

**Desconhecido** _(2024-11-06 18:43:58)_
> tbl_campos
id(id), id_cliente(id), nome(varchar), nome_integracao(varchar), mascara(varchar), tipo_da_informacao(varchar), limite_de_caracteres(int)


tbl_webhook
id(int),  id_cliente(int), url_webhook(varchar), token(varchar), titulo_botao(varchar), campos_obrigratorios(varchar)

**Desconhecido** _(2024-11-06 18:36:44)_
> As colunas a serem criadas?

id(id), id_cliente(id), nome(varchar), nome_integracao(varchar), mascara(varchar), tipo_da_informacao(varchar), limite_de_caracteres(int) ???


tbl_url_webhook
id(int),  id_cliente(int), url_webhook(varchar), token(varchar), titulo_botao(varchar), campos_obrigratorios(varchar)
