# Exemplos do que acontece nos bastidores de uma aplicação

O backend está presente em quase tudo que usamos na internet.  
Veja alguns exemplos práticos de como ele atua nos **bastidores**:

---

## 1. Login em um site
- O usuário digita seu e-mail e senha.  
- O backend verifica no banco de dados se as credenciais estão corretas.  
- Caso estejam certas, gera um **token de autenticação** e devolve para o frontend.  
- Esse token permite que o usuário navegue pelo sistema sem precisar fazer login a cada clique.

---

## 2. Loja online
- O cliente adiciona um produto ao carrinho.  
- O backend atualiza o carrinho do usuário no banco de dados.  
- Ao finalizar a compra, o backend calcula preços, impostos, descontos e comunica com o sistema de pagamento.  
- Depois confirma o pedido e envia a resposta ao frontend.

---

## 3. Redes sociais
- Quando você posta uma foto, o frontend envia a imagem para o backend.  
- O backend armazena a foto em um servidor ou serviço de armazenamento em nuvem.  
- Salva informações sobre o post (quem publicou, horário, descrição, curtidas).  
- Retorna ao frontend o “post pronto” para ser exibido na sua timeline.

---

## 4. Aplicativos de transporte (ex.: Uber, 99)
- O backend recebe a localização do passageiro e dos motoristas.  
- Executa algoritmos para encontrar o motorista mais próximo.  
- Envia a informação para o celular do motorista e atualiza o status da corrida em tempo real.

---

Perceba que em todos esses casos, o usuário **não vê** nada disso acontecendo.  

Ele apenas interage com uma interface simples, mas quem garante que tudo funcione corretamente é o **backend**.
