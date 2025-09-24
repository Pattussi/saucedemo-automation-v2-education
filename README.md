# Projeto de Automação de Testes – SauceDemo  

## 📌 Sobre o Projeto  
Este projeto foi desenvolvido como parte do meu portfólio após a conclusão do **Bootcamp de QA da TripleTen** e do curso de **Automação de Testes Web com Selenium WebDriver e Python**.  

O objetivo é simular cenários de teste em um **e-commerce fictício (SauceDemo)**, cobrindo fluxos críticos como login, adição de produtos ao carrinho e checkout.  

Além de ser um projeto técnico, ele também foi pensado de forma **didática**, servindo como guia para QA’s iniciantes que desejam aprender automação com Selenium + Python.  

---

##  Duas Versões do Projeto  
- `src/` → versão **profissional**, enxuta, sem comentários didáticos. Ideal para mostrar boas práticas em testes automatizados em sites.
- `educacional/` → versão **didática**, com comentários passo a passo explicando a aplicação da **Page Object Model (POM)** e comparações com código “cru”.  

---

## 🎯 Objetivos do Projeto
- **Profissional (src/):** apresentar código limpo, reutilizável e estruturado.  
- **Educacional (educacional/):** servir como guia para iniciantes em QA, mostrando como o POM simplifica testes de automação.
- Demonstrar a aplicação de **boas práticas de automação** com **Page Object Model (POM)**.  
- Validar fluxos essenciais de um e-commerce: login, carrinho e finalização de compra.  
- Fornecer uma base didática, mostrando através de comentários como seria o código “sem POM” e como pode ser otimizado.  

---

## 📂 Estrutura do Projeto  

```
saucedemo-automation/
│
├── src/             # Versão profissional (enxuta e sem comentários)
├── educacional/     # Versão didática (comentada, com exemplos de código cru)
├── requirements.txt # Dependências
├── .gitignore
└── README.md
```
---

## ⚙️ Tecnologias Utilizadas  
- **Linguagem:** Python 3  
- **Framework de Teste:** Pytest  
- **Automação Web:** Selenium WebDriver  
- **IDE:** Visual Studio Code  

---

## 🚀 Como Executar os Testes  

1. Clone este repositório:
   ```bash
   git clone https://github.com/Pattussi/saucedemo-automation-v2-education.git
   cd saucedemo-automation-v2-education
   ```

2. Crie e ative um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate      # Windows
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Execute os testes (versão profissional):
   ```bash
   pytest -v src/tests
   ```

5. Execute os testes (versão didática):
   ```bash
   pytest -v educacional/tests
   ```

---
## 🎓 Versão Educacional

A versão educacional mostra comparações entre:

- **Com POM:** uso de classes/métodos organizados.  
- **Sem POM (código cru):** blocos comentados dentro dos testes mostrando como ficaria com Selenium puro.  

👉 Veja mais detalhes no [`educacional/README.md`](educacional/README.md).  

---
## ✅ Casos de Teste Implementados  
- **CT01 – Fluxo de compra completo**  
   Login → Adição de produtos → Validação no carrinho → Checkout → Confirmação de pedido.  
- **CT02 – Login válido**  
   Verifica login com credenciais corretas.  
- **CT03 – Login inválido**  
   Valida mensagem de erro com credenciais incorretas.  

---

## 🏷️ Marcas de Testes (pytest)

Os testes utilizam **marcas** para organização e execução seletiva:

- `@pytest.mark.login` → testes relacionados ao login.  
- `@pytest.mark.carrinho` → testes relacionados ao carrinho/checkout.  

Exemplos de execução:

```bash
# Rodar todos os testes
pytest

# Rodar apenas os testes de login
pytest -m login

# Rodar apenas os testes de carrinho
pytest -m carrinho
```

---

## 🔮 Possíveis Evoluções  
- Integração de relatórios (Allure, pytest-html).  
- Inclusão de mais cenários (ex.: login bloqueado, remoção de itens do carrinho, checkout vazio).  
- Configuração de CI/CD com GitHub Actions para rodar os testes automaticamente.  

---

## ✨ Sobre Mim
Sou **Leonardo Pattussi**, profissional em transição para a área de **Qualidade de Software (QA)**.  
Após mais de 12 anos atuando como gerente comercial, concluí o **Bootcamp QA da TripleTen**, aplicando agora minha experiência analítica e de processos para garantir a entrega de produtos digitais de qualidade.  

📫 Contato: [pattussi@hotmail.com](mailto:pattussi@hotmail.com) | [LinkedIn](https://linkedin.com/in/leonardo-pattussi)  