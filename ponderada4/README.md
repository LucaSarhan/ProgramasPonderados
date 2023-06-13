# Ponderada 4

# Explicação

Para o projeto, criei um bucket no supabase onde serão adicionadas as imagens que eu desejar.

Foram utilizadas as bibliotecas de os, para obter os arquivos de mídia, de time, para obter a data atual e do supabase, para a criação de um cliente para envio de dados ao supabase.

Para o código, precisei inserir minhas credenciais do supabase, instanciei um cliente supabase, defini o nome do bucket que eu havia criado e a lista de arquivos que enviarei para lá.

Para mandar as imagens, usei um "for" para passar por cada arquivo da lista e seu diretório específico, os abrí em forma binária para que pudessem ser lidos e enviados com o nome em formato da data exata em que o processo foi realizado, junto com o nome do arquivo enviado.
