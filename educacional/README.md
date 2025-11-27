# 🎓 Versão Educacional - Saucedemo-automation-v2-education

A versão educacional foi criada para **ensinar automação de testes** usando Selenium + Python + Pytest + POM.

Ela contém:

- Explicações detalhadas  
- Comparações entre **POM** e **Selenium puro**  
- Testes comentados passo a passo  
- Estrutura ideal para iniciantes  

---

## 🔑 Ideia Central

Cada teste contém **duas versões** do código:

- **Com POM:** código simplificado, reaproveitando métodos de classes de páginas.  
- **Sem POM (comentado):** código cru escrito diretamente com Selenium (`driver.find_element...`).

Exemplo:

```python
# Com POM
login_page.fazer_login("standard_user", "secret_sauce")

# Sem POM 
# driver.find_element(By.ID, "user-name").send_keys("standard_user")
# driver.find_element(By.ID, "password").send_keys("secret_sauce")
# driver.find_element(By.ID, "login-button").click()
```

Essa comparação facilita para quem está aprendendo, mostrando o ganho de clareza, manutenção e reutilização de código com POM.

---
## 🧪 Testes Explicados

A versão educacional cobre os mesmos testes da versão profissional, porém com explicações:

- Login válido  
- Login inválido  
- Login bloqueado  
- Fluxo de compra completo  
- Remoção de itens  
- Ordenação  
- Campos obrigatórios  
- Logout  
- Validação de quantidade  
- Ordenação A→Z  

---

## 🏷️ Marcadores Pytest

Os mesmos da versão profissional:

- login  (Testes relacionados ao login)
- carrinho  (Ações no carrinho de compras)
- checkout  (Testes de finalização/erro)
- ordenacao  (Testes de filtros e ordenação)
- negativo  (Cenários negativos)
- smoke  (Testes rápidos para validação básica)
- regressao  (Cenários essenciais da aplicação)
- fluxo_completo  (Testes do início ao fim)


Todos os testes usam **marcas (pytest markers)** para facilitar a execução seletiva, exemplo:

- `@pytest.mark.login` → identifica testes de login.  
- `@pytest.mark.carrinho` → identifica testes de carrinho.  

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

## 👨‍🏫 Para quem é esta versão?

- Iniciantes em QA  
- Pessoas em transição de carreira  
- Mentores  
- Estudantes  
- Curiosos em automação  

---

Comece pelo teste mais completo:

👉 `educacional/tests/test_ct01_adicionar_produtos_carrinho.py`

Bom estudo! 🚀

---
## ✅ Conclusão

Essa versão educacional demonstra **o mesmo fluxo de testes de duas formas diferentes**:
1. Código cru (comentado, para fins didáticos).  
2. Código com POM (limpo e profissional).  

Assim, iniciantes podem compreender melhor os benefícios de utilizar o POM em automação de testes.
