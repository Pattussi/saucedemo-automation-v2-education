# 🎓 Versão Educacional - Projeto SauceDemo

Esta é a versão **didática** do projeto de automação.  
Aqui o objetivo é mostrar de forma prática como o **Page Object Model (POM)** simplifica e organiza o código em comparação com o **Selenium cru**.

---

## 🔑 Ideia Central

Cada teste contém **duas versões** do código:

- **Com POM:** código simplificado, reaproveitando métodos de classes de páginas.  
- **Sem POM (comentado):** código cru escrito diretamente com Selenium (`driver.find_element...`).

Exemplo:

```python
# Com POM
login_page.fazer_login("standard_user", "secret_sauce")

# Sem POM (antes)
# driver.find_element(By.ID, "user-name").send_keys("standard_user")
# driver.find_element(By.ID, "password").send_keys("secret_sauce")
# driver.find_element(By.ID, "login-button").click()
```

Essa comparação facilita para quem está aprendendo, mostrando o ganho de clareza, manutenção e reutilização de código com POM.

---

## 🏷️ Organização por marcas

Todos os testes usam **marcas (pytest markers)** para facilitar a execução seletiva:

- `@pytest.mark.login` → identifica testes de login.  
- `@pytest.mark.carrinho` → identifica testes de carrinho/checkout.  

Exemplos:

```bash
# Executa apenas testes de login
pytest -m login

# Executa apenas testes de carrinho
pytest -m carrinho
```

---

## 📂 Estrutura da versão educacional

```
educacional/
│
├── pages/              # Classes POM das páginas do sistema
├── tests/              # Testes automatizados com comparações (POM vs cru)
└── conftest.py         # Configuração do pytest e inicialização do driver
```

---

## 📘 Arquivos principais

- **`conftest.py`** → configuração de driver, setup/teardown.  
- **`pages/`** → classes com métodos para interagir com cada página (Login, Home, Carrinho, Checkout, Finish).  
- **`tests/`** → cenários de teste:
  - `test_ct01_adicionar_produtos_carrinho.py` → fluxo completo de compra (login → carrinho → checkout → finalizar).  
  - `test_ct02_login_valido.py` → login válido.  
  - `test_ct03_login_invalido.py` → login inválido.  

---

## ✅ Conclusão

Essa versão educacional demonstra **o mesmo fluxo de testes de duas formas diferentes**:
1. Código cru (comentado, para fins didáticos).  
2. Código com POM (limpo e profissional).  

Assim, iniciantes podem compreender melhor os benefícios de utilizar o POM em automação de testes.
