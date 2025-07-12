# 📞 Catálogo de Ramais

Sistema web desenvolvido com Flask e SQLite para gerenciamento de ramais de uma empresa. Este projeto foi criado com fins educacionais e demonstra conhecimento em desenvolvimento web com Python, integração com bancos de dados, estilização responsiva e exportação de dados.

---

## 🚀 Funcionalidades

- ✅ Cadastro de novos ramais  
- ✅ Edição e exclusão de ramais  
- ✅ Busca por nome, sobrenome, e-mail, setor, ramal ou telefone  
- ✅ Exportação da lista completa em Excel  
- ✅ Integração com WhatsApp (link direto via número de telefone)  
- ✅ Links clicáveis de e-mail (abrem o Outlook)  
- ✅ Interface responsiva com HTML + CSS  
- ✅ Importação de planilhas Excel para o banco de dados  

---

## 🛠️ Tecnologias Utilizadas

| Tecnologia | Função |
|------------|--------|
| Python | Lógica principal |
| Flask | Framework web |
| SQLite | Banco de dados local |
| Pandas | Leitura e escrita de Excel |
| XlsxWriter | Exportação de planilha |
| OpenPyXL | Leitura de planilha |
| HTML5 + CSS3 | Interface do usuário |
| Font Awesome | Ícones na interface |

---

## 📁 Estrutura do Projeto

```plaintext
catalogo-ramais/
├── app.py                    # Aplicação principal Flask
├── importar_planilha.py     # Script para importar dados do Excel
├── ramais.db                # Banco de dados SQLite
├── ramais.xlsx              # Planilha de exemplo (opcional)
├── requirements.txt         # Dependências do projeto
├── templates/
│   ├── index.html
│   ├── formulario.html
│   └── editar.html
├── static/
│   ├── style.css
│   ├── favicon.png
│   └── whatsapp-icon.png
```

---

## ⚙️ Como Executar o Projeto

1. **Clone o repositório**
   ```bash
   git clone https://github.com/seu-usuario/catalogo-ramais.git
   cd catalogo-ramais

2. **(Opcional) Crie um ambiente virtual**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Para Windows

3. **Instale manualmente as bibliotecas necessárias**
   ```bash
   pip install flask pandas openpyxl xlsxwriter

4. **Execute o sistema**
   ```bash
   python app.py

5. **(Opcional) Importe dados a partir de planilha**
   > Certifique-se de ter um arquivo chamado `ramais.xlsx` no diretório. Depois:
   ```bash
   python importar_planilha.py

---

## 📎 Exemplo de Planilha Aceita

| Nome         | Setor      | Ramal | Telefone        | Email                   |
|--------------|------------|-------|------------------|--------------------------|
| Ana Silva    | Financeiro | 201   | (11) 99999-0001 | ana.silva@empresa.com   |
| João Pereira | TI         | 202   | (11) 99999-0002 | joao.pereira@empresa.com |

> O campo **Nome** é automaticamente separado em **Nome** e **Sobrenome** durante a importação.
