# Projeto de Automação de Testes – saucedemo-automation-v2-education

## 📌 Sobre o Projeto  
Este projeto foi desenvolvido como parte do meu portfólio após a conclusão do **Bootcamp de QA da TripleTen** e do curso de **Automação de Testes Web com Selenium WebDriver e Python**.  

Ele simula cenários reais de teste em um **e-commerce fictício (SauceDemo)**, cobrindo fluxos essenciais como:

- Login  
- Ordenação de produtos  
- Carrinho  
- Checkout  
- Finalização de compra  

O projeto possui **duas versões**: uma profissional e uma educacional.

Além de ser um projeto técnico, ele também foi pensado de forma **didática**, servindo como guia para QA’s iniciantes que desejam aprender automação com Selenium + Python.  

---
## 🎯 Objetivos do Projeto
- **Profissional (src/):** apresentar código limpo, reutilizável e estruturado.  
- **Educacional (educacional/):** servir como guia para iniciantes em QA, mostrando como o POM simplifica testes de automação.
- Demonstrar a aplicação de **boas práticas de automação** com **Page Object Model (POM)**.  
- Validar fluxos essenciais de um e-commerce.  
- Fornecer uma base didática, mostrando através de comentários como seria o código “sem POM” e como pode ser otimizado.  

---

## 🧭 Duas Versões do Projeto  

### `src/` – Versão Profissional
- Código limpo  
- Estrutura enxuta  
- Sem comentários didáticos  
- Ideal para entrevistas e portfólio real  

### `educacional/` – Versão Didática
- Comentários passo a passo  
- Comparações entre POM x Selenium puro  
- Explicações sobre cada parte do código  

---

## 📂 Estrutura

```
saucedemo-automation-v2-education/
│
├── src/
│   ├── pages/
│   ├── tests/
├── educacional/
│   ├── pages/
│   ├── tests/
│   └── README.md/
├── requirements.txt
├── conftest.py
└── README.md
```

---

## ⚙️ Tecnologias  
- Python 3  
- Selenium WebDriver  
- Pytest  
- VS Code  

---

## 🚀 Como Executar

### Instalação
```bash
git clone https://github.com/Pattussi/saucedemo-automation-v2-education.git
cd saucedemo-automation-v2-education
python -m venv venv
venv\Scripts\activate   # Windows
pip install -r requirements.txt
```

### Executar testes
**Profissional:**
```bash
pytest -v src/tests
```

**Educacional:**
```bash
pytest -v educacional/tests
```

---

## 🧪 Casos de Teste (10 Testes)

### Login
- CT02 – Login válido  
- CT03 – Login inválido  
- CT10 – Login bloqueado  

### Carrinho
- CT01 – Fluxo completo  
- CT07 – Remover item  
- CT09 – Validar quantidade  

### Checkout
- CT06 – Campos obrigatórios vazios  

### Ordenação
- CT05 – Preço decrescente  
- CT08 – Alfabético A→Z  

### Sessão
- CT04 – Logout  

---

## 🏷️ Marcadores Pytest

| Marcador | Categoria |
|---------|-----------|
| login | Testes de login |
| carrinho | Fluxos do carrinho |
| checkout | Validações do checkout |
| ordenacao | Ordenação de produtos |
| negativo | Cenários negativos |
| smoke | Testes rápidos |
| regressao | Conjunto crítico |
| fluxo_completo | Testes ponta-a-ponta |

**Exemplos:**
```bash
pytest -m login
pytest -m regressao
pytest -m negativo
```

---
## 🎓 Versão Educacional

A versão educacional mostra comparações entre:

- **Com POM:** uso de classes/métodos organizados.  
- **Sem POM (código cru):** blocos comentados dentro dos testes mostrando como ficaria com Selenium puro.  

👉 Veja mais detalhes no [`educacional/README.md`](educacional/README.md).  


---

## 🔮 Possíveis Evoluções  
- Relatórios Allure ou pytest-html

- Integração com GitHub Actions (CI/CD)

- Testes em múltiplos navegadores (Cross-browser)

- Parâmetros de execução (usuários, itens etc.)

- Inclusão de testes de API para complementar o ciclo QA

---

## ✨ Sobre Mim
Sou **Leonardo Pattussi**, profissional em transição para a área de **Qualidade de Software (QA)**.  
Após mais de 12 anos atuando como gerente comercial, concluí o **Bootcamp QA da TripleTen**, aplicando agora minha experiência analítica e de processos para garantir a entrega de produtos digitais de qualidade.  

📫 Contato: [pattussi@hotmail.com](mailto:pattussi@hotmail.com) | [LinkedIn](https://linkedin.com/in/leonardo-pattussi)  