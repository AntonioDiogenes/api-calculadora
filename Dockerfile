# Use a imagem oficial do Python 3.10
FROM python:3.10

# Defina o diretório de trabalho
WORKDIR /app

# Copie o arquivo de requisitos para o contêiner
COPY requirements.txt .

# Instale as dependências
RUN pip install --no-cache-dir -r requirements.txt

RUN pip install Flask-Mail

RUN pip install Flask-CORS

# Copie o restante do aplicativo para o contêiner
COPY . .

# Exponha a porta 5000, que é a porta padrão do Flask
EXPOSE 5000

# Comando para executar o aplicativo Flask
CMD ["python", "calculadoraFlask.py"]
