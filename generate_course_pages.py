# Script para gerar páginas individuais dos cursos

courses = [
    {
        "id": "webmaster",
        "title": "WebMaster: HTML, CSS e JavaScript",
        "short_title": "WebMaster",
        "description": "Entre no mundo do desenvolvimento web criando páginas modernas e interativas do zero.",
        "level": "Iniciante",
        "level_class": "green-500",
        "image_id": "g2",
        "about": "O curso WebMaster é ideal para quem quer começar no desenvolvimento web. Você aprenderá as três tecnologias fundamentais que formam a base de qualquer página da internet: HTML para estrutura, CSS para estilização e JavaScript para interatividade.",
        "learn": [
            "HTML5 semântico e acessível",
            "CSS3 com Flexbox e Grid",
            "JavaScript ES6+ moderno",
            "Responsividade e Mobile First",
            "Animações e transições CSS",
            "Manipulação do DOM",
            "Projetos práticos reais",
            "Deploy e hospedagem"
        ],
        "target": [
            "Iniciantes em programação web",
            "Designers querendo codificar",
            "Profissionais em transição",
            "Empreendedores digitais"
        ],
        "requirements": [
            "Computador com navegador moderno",
            "Editor de código (recomendamos VS Code)",
            "Vontade de criar sites incríveis"
        ]
    },
    {
        "id": "sql",
        "title": "Banco de Dados com SQL Server",
        "short_title": "SQL Fundamentals",
        "description": "Aprenda a criar e gerenciar bancos de dados relacionais com SQL Server profissionalmente.",
        "level": "Intermediário",
        "level_class": "blue-500",
        "image_id": "g3",
        "about": "Domine SQL Server e banco de dados relacionais. Aprenda a modelar, criar, consultar e otimizar bancos de dados para aplicações profissionais e escaláveis.",
        "learn": [
            "Modelagem de banco de dados",
            "SQL básico ao avançado",
            "Stored Procedures e Functions",
            "Triggers e Views",
            "Índices e otimização",
            "Transações e ACID",
            "Backup e restauração",
            "Segurança de dados"
        ],
        "target": [
            "Desenvolvedores backend",
            "Analistas de dados",
            "DBAs iniciantes",
            "Estudantes de TI"
        ],
        "requirements": [
            "Conhecimentos básicos de lógica",
            "SQL Server instalado",
            "Familiaridade com sistemas"
        ]
    },
    {
        "id": "python",
        "title": "Python do Zero ao Avançado",
        "short_title": "Python Essentials",
        "description": "Domine Python, uma das linguagens mais populares para desenvolvimento, automação e análise de dados.",
        "level": "Iniciante",
        "level_class": "green-500",
        "image_id": "g4",
        "about": "Python é uma das linguagens mais versáteis e procuradas do mercado. Neste curso completo, você aprenderá desde os fundamentos até técnicas avançadas, preparando-se para desenvolvimento web, automação, análise de dados e muito mais.",
        "learn": [
            "Sintaxe e fundamentos Python",
            "Estruturas de dados nativas",
            "Programação orientada a objetos",
            "Módulos e pacotes",
            "Tratamento de exceções",
            "Trabalho com arquivos",
            "APIs e web scraping",
            "Automação de tarefas"
        ],
        "target": [
            "Iniciantes em programação",
            "Profissionais querendo automatizar tarefas",
            "Futuros cientistas de dados",
            "Desenvolvedores de outras linguagens"
        ],
        "requirements": [
            "Nenhum conhecimento prévio necessário",
            "Python 3.x instalado",
            "Curiosidade e dedicação"
        ]
    },
    {
        "id": "react",
        "title": "React JS: Interfaces Modernas",
        "short_title": "React Developer",
        "description": "Desenvolva aplicações web dinâmicas e escaláveis com React e suas melhores práticas.",
        "level": "Intermediário",
        "level_class": "blue-500",
        "image_id": "g6",
        "about": "React é a biblioteca JavaScript mais popular para construção de interfaces. Aprenda a criar aplicações modernas, componentizadas e escaláveis seguindo as melhores práticas da comunidade.",
        "learn": [
            "Components e Props",
            "State e Lifecycle",
            "Hooks (useState, useEffect, etc)",
            "Context API",
            "React Router",
            "Styled Components",
            "Integração com APIs",
            "Performance e otimização"
        ],
        "target": [
            "Desenvolvedores JavaScript",
            "Front-end developers",
            "Full-stack developers",
            "Profissionais atualizando skills"
        ],
        "requirements": [
            "HTML, CSS e JavaScript",
            "Node.js instalado",
            "Conceitos de ES6+"
        ]
    },
    {
        "id": "node",
        "title": "Node.js e APIs RESTful",
        "short_title": "Node.js Backend",
        "description": "Crie servidores e APIs robustas com Node.js, autenticação e deploy na nuvem.",
        "level": "Intermediário",
        "level_class": "blue-500",
        "image_id": "g7",
        "about": "Torne-se um desenvolvedor backend com Node.js. Aprenda a criar APIs RESTful escaláveis, implementar autenticação, trabalhar com bancos de dados e fazer deploy em produção.",
        "learn": [
            "Node.js e Express",
            "APIs RESTful",
            "Autenticação JWT",
            "MongoDB e Mongoose",
            "Validação de dados",
            "Upload de arquivos",
            "WebSockets em tempo real",
            "Deploy e CI/CD"
        ],
        "target": [
            "Desenvolvedores JavaScript",
            "Front-end migrando para full-stack",
            "Backend developers",
            "Arquitetos de software"
        ],
        "requirements": [
            "JavaScript intermediário",
            "Node.js e npm",
            "Conceitos de APIs"
        ]
    },
    {
        "id": "security",
        "title": "Segurança e Ethical Hacking",
        "short_title": "Cyber Security",
        "description": "Entre no mundo da cibersegurança com técnicas de ethical hacking e análise de vulnerabilidades.",
        "level": "Avançado",
        "level_class": "red-500",
        "image_id": "g8",
        "about": "Aprenda a proteger sistemas e aplicações contra ataques cibernéticos. Este curso aborda técnicas de ethical hacking, análise de vulnerabilidades, pentesting e segurança defensiva.",
        "learn": [
            "Fundamentos de segurança",
            "Ethical hacking e pentesting",
            "Análise de vulnerabilidades",
            "OWASP Top 10",
            "Criptografia aplicada",
            "Segurança de redes",
            "Ferramentas profissionais",
            "Relatórios técnicos"
        ],
        "target": [
            "Profissionais de TI",
            "Desenvolvedores preocupados com segurança",
            "Analistas de segurança",
            "Auditores de sistemas"
        ],
        "requirements": [
            "Conhecimento em redes",
            "Lógica de programação",
            "Linux básico"
        ]
    },
    {
        "id": "java",
        "title": "Java e Orientação a Objetos",
        "short_title": "Java Programming",
        "description": "Aprenda Java, uma das linguagens mais usadas no mercado, com foco em POO e boas práticas.",
        "level": "Iniciante",
        "level_class": "green-500",
        "image_id": "g9",
        "about": "Java é uma das linguagens mais utilizadas no mundo corporativo. Aprenda os fundamentos da programação orientada a objetos e desenvolva aplicações robustas e escaláveis.",
        "learn": [
            "Sintaxe e fundamentos Java",
            "Programação Orientada a Objetos",
            "Herança e Polimorfismo",
            "Interfaces e Classes Abstratas",
            "Collections Framework",
            "Exceções e tratamento de erros",
            "JDBC e banco de dados",
            "Projetos práticos"
        ],
        "target": [
            "Iniciantes em programação",
            "Estudantes universitários",
            "Profissionais em transição",
            "Desenvolvedores de outras linguagens"
        ],
        "requirements": [
            "Lógica de programação básica",
            "JDK instalado",
            "IDE (Eclipse ou IntelliJ)"
        ]
    },
    {
        "id": "typescript",
        "title": "TypeScript: Desenvolvimento Moderno",
        "short_title": "TypeScript Pro",
        "description": "Adicione tipagem estática ao JavaScript e desenvolva aplicações mais seguras e escaláveis.",
        "level": "Intermediário",
        "level_class": "blue-500",
        "image_id": "g10",
        "about": "TypeScript adiciona superpoderes ao JavaScript com tipagem estática. Aprenda a escrever código mais seguro, manutenível e escalável para projetos de qualquer tamanho.",
        "learn": [
            "Tipos básicos e avançados",
            "Interfaces e Type Aliases",
            "Generics",
            "Decorators",
            "Módulos e Namespaces",
            "Integração com frameworks",
            "Configuração do compilador",
            "Melhores práticas"
        ],
        "target": [
            "Desenvolvedores JavaScript",
            "Desenvolvedores React/Angular/Vue",
            "Full-stack developers",
            "Arquitetos de software"
        ],
        "requirements": [
            "JavaScript ES6+",
            "Node.js",
            "Conceitos de tipagem"
        ]
    },
    {
        "id": "machinelearning",
        "title": "Machine Learning com Python",
        "short_title": "Machine Learning",
        "description": "Crie modelos de inteligência artificial e machine learning usando Python, TensorFlow e Scikit-learn.",
        "level": "Avançado",
        "level_class": "red-500",
        "image_id": "g12",
        "about": "Entre no mundo da Inteligência Artificial com Machine Learning. Aprenda a criar, treinar e deploy modelos de ML para resolver problemas reais usando Python e bibliotecas profissionais.",
        "learn": [
            "Fundamentos de ML",
            "Regressão e Classificação",
            "Árvores de Decisão e Random Forest",
            "Redes Neurais",
            "Deep Learning básico",
            "Scikit-learn e TensorFlow",
            "Pré-processamento de dados",
            "Avaliação de modelos"
        ],
        "target": [
            "Cientistas de dados",
            "Desenvolvedores Python",
            "Analistas de dados",
            "Pesquisadores e acadêmicos"
        ],
        "requirements": [
            "Python intermediário",
            "Matemática básica (álgebra)",
            "Estatística fundamental"
        ]
    },
    {
        "id": "flutter",
        "title": "Flutter: Desenvolvimento Mobile",
        "short_title": "Flutter Mobile",
        "description": "Crie aplicativos nativos para Android e iOS com um único código usando Flutter e Dart.",
        "level": "Intermediário",
        "level_class": "blue-500",
        "image_id": "g13",
        "about": "Flutter permite criar aplicativos móveis nativos para Android e iOS com um único código. Aprenda a desenvolver apps bonitos, rápidos e com performance nativa.",
        "learn": [
            "Fundamentos do Dart",
            "Widgets e Layouts",
            "Navegação e rotas",
            "State Management",
            "Integração com APIs",
            "Firebase",
            "Animações",
            "Publicação nas lojas"
        ],
        "target": [
            "Desenvolvedores mobile",
            "Desenvolvedores web migrando",
            "Empreendedores tech",
            "Freelancers"
        ],
        "requirements": [
            "Lógica de programação",
            "Flutter SDK instalado",
            "Conceitos de mobile"
        ]
    },
    {
        "id": "uxui",
        "title": "UX/UI Design Completo",
        "short_title": "UX/UI Design",
        "description": "Aprenda a criar interfaces intuitivas e experiências memoráveis com Figma, prototipação e testes.",
        "level": "Iniciante",
        "level_class": "green-500",
        "image_id": "g14",
        "about": "Domine UX/UI Design e crie produtos digitais que as pessoas amam usar. Aprenda pesquisa de usuário, prototipação, design de interface e testes de usabilidade.",
        "learn": [
            "Fundamentos de UX",
            "Pesquisa com usuários",
            "Wireframes e protótipos",
            "Design de interfaces",
            "Figma profissional",
            "Design System",
            "Testes de usabilidade",
            "Portfolio de projetos"
        ],
        "target": [
            "Designers gráficos",
            "Desenvolvedores front-end",
            "Product Managers",
            "Empreendedores"
        ],
        "requirements": [
            "Noções de design",
            "Figma instalado",
            "Criatividade e empatia"
        ]
    },
    {
        "id": "devops",
        "title": "DevOps: CI/CD e Cloud",
        "short_title": "DevOps Engineer",
        "description": "Automatize deploy, monitore aplicações e domine ferramentas DevOps essenciais como Docker e Kubernetes.",
        "level": "Avançado",
        "level_class": "red-500",
        "image_id": "g15",
        "about": "DevOps une desenvolvimento e operações para entregas mais rápidas e confiáveis. Aprenda Docker, Kubernetes, CI/CD, cloud computing e automação de infraestrutura.",
        "learn": [
            "Cultura DevOps",
            "Docker e containers",
            "Kubernetes básico",
            "CI/CD pipelines",
            "Git avançado",
            "AWS/Azure basics",
            "Monitoramento",
            "Infrastructure as Code"
        ],
        "target": [
            "Desenvolvedores",
            "Administradores de sistemas",
            "Engenheiros de infraestrutura",
            "Arquitetos de software"
        ],
        "requirements": [
            "Linux intermediário",
            "Programação básica",
            "Conceitos de redes"
        ]
    }
]

print(f"Total de cursos a serem criados: {len(courses)}")
for course in courses:
    print(f"- {course['title']}")
