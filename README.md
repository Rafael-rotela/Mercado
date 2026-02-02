# Mercado

# 🛒 Sistema de Gestão de Vendas (PDV)

Este é um sistema de automação comercial desenvolvido em **Python**, focado na gestão de estoque, cadastro de clientes e simulação de um frente de caixa (PDV) com cálculo automatizado de impostos.

## 🚀 Funcionalidades

### 🔐 Módulo Gerente
* **Gestão de Produtos:** Cadastro com atribuição de impostos (Municipal, Estadual ou Nacional), listagem, atualização de estoque e exclusão.
* **Gestão de Clientes:** Cadastro completo com CPF, controle de duplicidade e edição de perfil.

### 👤 Módulo Cliente
* **Sistema de Login:** Acesso seguro para usuários cadastrados.
* **Carrinho de Compras:** Adição e remoção de itens com atualização em tempo real do estoque.
* **Cupom Fiscal:** Geração detalhada com subtotal e cálculo de impostos dinâmico por item.

## 📊 Estrutura de Impostos
O sistema utiliza um mapa de alíquotas para cálculos precisos:
- **Municipal (m):** 12%
- **Estadual (e):** 8%
- **Nacional (n):** 5%

## 🛠️ Tecnologias Utilizadas
* [Python 3](https://www.python.org/)
* Biblioteca `time` para simulação de processamento.
* Sequências de escape ANSI para interface colorida no terminal.

## 📦 Como executar
1. Certifique-se de ter o Python instalado.
2. Clone o repositório:
   ```bash
   git clone [https://github.com/seu-usuario/seu-repositorio.git](https://github.com/seu-usuario/seu-repositorio.git)
