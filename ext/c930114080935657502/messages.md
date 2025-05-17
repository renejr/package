**Desconhecido** _(2025-01-20 17:23:06)_
> 
[Anexo](https://cdn.discordapp.com/attachments/930114080935657502/1330950749080915998/image.png?ex=0&is=67fa03b8&hm=94b1802f9941dfb6a3abbb2ccba7e7c1724805dfc71f8c4033696a99e49a0c53&uc=dp&)

**Desconhecido** _(2025-01-20 17:22:43)_
> pdo-mysql): SELECT id, nome_canal, status FROM instancias WHERE id_cliente =1 AND id IN( ) ORDER BY id  
1064: You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near ') ORDER BY id' at line 1

**Desconhecido** _(2024-12-03 20:32:49)_
> https://iaexpert.academy/2019/04/12/word-embedding-transformando-palavras-em-numeros/

**Desconhecido** _(2024-12-03 19:58:27)_
> https://stackoverflow.com/questions/19185326/use-goto-inside-function-php

**Desconhecido** _(2024-11-13 18:39:47)_
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
