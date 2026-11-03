# 🐍 Web Test Automation with Selenium WebDriver & Python

Este repositório contém a suíte de testes automatizados Web desenvolvida em **Python** utilizando **Selenium WebDriver**, construída como parte da capacitação em automação de testes pela **Udemy**. 

O projeto aborda desde a manipulação elementar do DOM até a aplicação de padrões de automação para testes regressivos e funcionais.

---

## 📌 Objetivos do Projeto

- Aplicar o **Selenium WebDriver** com **Python** na automação de aplicações web reais.
- Implementar boas práticas de sincronização de elementos utilizando **Explicit Waits** e **Implicit Waits**.
- Manipular diversos elementos de interface (Formulários, Dropdowns, Checkboxes, Alerts, Frames e Modais).
- Estruturar testes funcionais e regressivos automatizados.

---

## 🏗️ Estrutura do Repositório

```text
Automacao-de-Testes-Web-com-Selenium-Webdriver-e-Python-Udemy/
├── tests/                  # Scripts de testes funcionais automatizados
├── pages/                  # Elementos mapeados e interações com telas
├── requirements.txt        # Dependências do projeto (Selenium, PyTest, WebDriver Manager)
└── README.md               # Documentação do projeto
```

---

## 🛠️ Tecnologias & Ferramentas

- **[Python 3.x](https://www.python.org/)**: Linguagem base do projeto.
- **[Selenium WebDriver](https://www.selenium.dev/)**: Framework de automação de testes para navegadores web.
- **[PyTest](https://docs.pytest.org/)**: Test runner para execução e organização dos testes.
- **WebDriver Manager**: Gerenciamento automático de drivers do navegador (ChromeDriver/GeckoDriver).

---

## 🚀 Como Executar o Projeto Localmente

### Pré-requisitos
- **Python 3.8+** instalado na sua máquina
- **Git** instalado

### Passo a Passo

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/vesilva99/Automacao-de-Testes-Web-com-Selenium-Webdriver-e-Python-Udemy.git
   cd Automacao-de-Testes-Web-com-Selenium-Webdriver-e-Python-Udemy
   ```

2. **Crie e ative um ambiente virtual (recomendado):**
   - **Windows:**
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```
   - **Linux/macOS:**
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Execute os testes com PyTest:**
   ```bash
   pytest
   ```
   *Para executar exibindo o navegador em tempo real (não headless):*
   ```bash
   pytest -s -v
   ```

---

## 📋 Habilidades e Conceitos Demonstrados

- [x] **Localização de Elementos:** Estratégias por `ID`, `Name`, `XPath`, `CSS Selector` e `Class`.
- [x] **Tratamento de Sincronismo:** Uso de `WebDriverWait` e `expected_conditions` para evitar testes intermitentes (*flaky tests*).
- [x] **Interação com Componentes:** Preenchimento de campos, cliques, seleção de comboboxes, upload de arquivos e navegação entre janelas/frames.
- [x] **Asserções de Teste:** Validação de textos, visibilidade de elementos e comportamento esperado das telas.

---

## 👤 Autor

**Victor Silva**  
QA Analyst | Testes Manuais & Automatizados  
- **LinkedIn:** [victor-silva-qa](https://www.linkedin.com/in/victor-silva-qa)  
- **GitHub:** [@vesilva99](https://github.com/vesilva99)
