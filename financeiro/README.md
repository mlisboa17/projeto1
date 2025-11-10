# 💰 PiggMeu - Sistema de Controle Financeiro

Um sistema web moderno e intuitivo para controle de receitas e despesas, desenvolvido com Django.

![Python](https://img.shields.io/badge/python-v3.14+-blue.svg)
![Django](https://img.shields.io/badge/django-v5.2.7-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

## 🚀 Funcionalidades

- ✅ **Gerenciamento de Transações**: Adicione, visualize e exclua receitas e despesas
- 📊 **Dashboard Intuitivo**: Visualize seus totais, receitas, despesas e saldo atual
- 🎨 **Design Moderno**: Interface responsiva e moderna com gradientes e animações
- 💫 **Experiência de Usuário**: Confirmações de exclusão e feedback visual
- 📱 **Responsivo**: Funciona perfeitamente em desktop, tablet e mobile
- 👑 **Painel Administrativo**: Gerenciamento completo via Django Admin

## 🛠️ Tecnologias Utilizadas

- **Backend**: Django 5.2.7
- **Frontend**: HTML5, CSS3 (Flexbox/Grid), JavaScript
- **Banco de Dados**: SQLite (desenvolvimento)
- **Python**: 3.14+

## 📋 Pré-requisitos

- Python 3.14 ou superior
- pip (gerenciador de pacotes do Python)

## 🔧 Instalação e Configuração

1. **Clone o repositório:**
```bash
git clone https://github.com/mlisboa17/projeto1.git
cd projeto1
```

2. **Crie um ambiente virtual:**
```bash
python -m venv venv
```

3. **Ative o ambiente virtual:**
- Windows: `venv\Scripts\activate`
- macOS/Linux: `source venv/bin/activate`

4. **Instale as dependências:**
```bash
pip install django
```

5. **Execute as migrações:**
```bash
python manage.py migrate
```

6. **Crie um superusuário (opcional):**
```bash
python manage.py createsuperuser
```

7. **Inicie o servidor de desenvolvimento:**
```bash
python manage.py runserver
```

8. **Acesse a aplicação:**
- Sistema: http://127.0.0.1:8000/
- Admin: http://127.0.0.1:8000/admin/

## 📖 Como Usar

### 💰 Adicionando Transações
1. Preencha a descrição da transação
2. Digite o valor
3. Selecione o tipo (Receita ou Despesa)
4. Clique em "Adicionar Transação"

### 👀 Visualizando Dados
- **Tabela**: Veja todas as transações organizadas
- **Resumo**: Acompanhe totais de receitas, despesas e saldo
- **Cores**: Verde para receitas, vermelho para despesas

### 🗑️ Removendo Transações
- Clique no botão "Excluir" ao lado da transação
- Confirme a exclusão na janela que aparece

## 🎨 Design e Interface

- **Layout Responsivo**: Adapta-se a qualquer tamanho de tela
- **Gradientes Modernos**: Visual atrativo e profissional
- **Animações Suaves**: Transições e efeitos visuais
- **Tipografia Clara**: Fácil leitura em qualquer dispositivo
- **Feedback Visual**: Cores intuitivas para diferentes tipos de dados

## 📁 Estrutura do Projeto

```
financeiro/
├── manage.py
├── financeiro/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── piggmeu/
│   ├── models.py          # Modelo de Transação
│   ├── views.py           # Lógica de negócio
│   ├── admin.py           # Configuração do admin
│   ├── urls.py            # URLs da aplicação
│   ├── templates/
│   │   └── home.html      # Template principal
│   └── static/
│       └── style.css      # Estilos CSS
├── db.sqlite3             # Banco de dados
└── README.md
```

## 🔒 Segurança

- ✅ CSRF Protection habilitado
- ✅ Validação de formulários
- ✅ Sanitização de dados
- ✅ Confirmação de exclusões

## 🤝 Contribuição

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 👨‍💻 Autor

**Marcio Lisboa**
- GitHub: [@mlisboa17](https://github.com/mlisboa17)
- Email: mlisboa17@hotmail.com

## 📞 Suporte

Se você encontrar algum problema ou tiver sugestões, por favor:
1. Abra uma [issue](https://github.com/mlisboa17/projeto1/issues)
2. Entre em contato via email

---

⭐ **Se este projeto foi útil para você, deixe uma estrela!**