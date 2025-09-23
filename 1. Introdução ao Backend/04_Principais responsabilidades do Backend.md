# Principais responsabilidades do Backend

O backend é responsável por garantir que **as regras de negócio** e **o fluxo de dados** funcionem corretamente.  
Abaixo estão algumas das tarefas mais importantes, com exemplos práticos:

---

## 1. Autenticação e Autorização 
- **Autenticação**: verificar se o usuário é quem diz ser (ex.: login com e-mail e senha).  
- **Autorização**: verificar se o usuário pode acessar determinada funcionalidade (ex.: somente administradores podem excluir dados).  

*Exemplo*:  
Você tenta entrar em um painel de controle.  
O backend checa se seu token de login é válido (**autenticação**) e se sua conta tem permissão de administrador (**autorização**).

---

## 2. Manipulação e Armazenamento de Dados 
- Receber informações do frontend.  
- Salvar, atualizar, remover e consultar dados em bancos de dados.  

*Exemplo*:  
Quando você se cadastra em um site, o backend recebe seu nome, e-mail e senha.  
Ele então **salva esses dados no banco de dados** para que você possa fazer login futuramente.

---

## 3. Regras de Negócio 
- Implementar a lógica central da aplicação.  
- Garantir que os processos sigam as condições definidas pelo sistema.  

*Exemplo*:  
Em um e-commerce, o backend calcula automaticamente o **frete** e os **descontos** no carrinho de compras antes de finalizar a transação.

---

## 4. Comunicação com outros serviços 
- Integrar APIs e serviços externos.  
- Enviar e receber dados de terceiros.  

*Exemplo*:  
Um app de viagens consulta a **API de clima** para exibir a previsão do tempo no destino escolhido pelo usuário.

---

## 5. Segurança 
- Proteger informações sensíveis (como senhas e dados de cartão de crédito).  
- Usar técnicas como **hashing**, **criptografia** e **controle de acesso**.  

*Exemplo*:  
Quando você cria uma senha, o backend não guarda o texto puro.  
Ele guarda um **hash criptográfico**, que garante mais segurança caso o banco de dados seja exposto.

---

Essas são as responsabilidades centrais que tornam o backend o **coração** de qualquer sistema moderno.
