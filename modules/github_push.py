from github import Github
import os

# Configura tu token de acceso personal de GitHub
g = Github(os.getenv("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"))

def push_to_github(repo_name, file_path, commit_message):
    """
    Esta función toma el nombre de un repositorio, la ruta de un archivo y un mensaje de commit
    como entrada y hace push del archivo al repositorio en GitHub.
    """
    repo = g.get_user().get_repo(repo_name)
    file = open(file_path, 'r')
    content = file.read()

    # Asegúrate de cerrar el archivo después de leerlo
    file.close()

    # Carga o actualiza el archivo en GitHub
    try:
        repo.create_file(file_path, commit_message, content)
    except:
        contents = repo.get_contents(file_path)
        repo.update_file(contents.path, commit_message, content, contents.sha)

# Primero, debes crear una instancia de la clase Github utilizando tu token de acceso
g = Github(os.getenv("GITHUB_TOKEN"))

def analyze_repo(user_name, repo_name):
    """
    Esta función toma un nombre de usuario y un nombre de repositorio como entrada y luego
    imprime información básica sobre el repositorio.
    """
    # Obtiene el repositorio
    repo = g.get_user(user_name).get_repo(repo_name)

    # Imprime información básica sobre el repositorio
    print(f"Nombre: {repo.name}")
    print(f"Estrellas: {repo.stargazers_count}")
    print(f"Forks: {repo.forks_count}")
    print(f"Fecha de creación: {repo.created_at}")
    print(f"Fecha de última actualización: {repo.updated_at}")

# Luego puedes llamar a esta función con el nombre de usuario y el nombre del repositorio
analyze_repo("your_username", "arena")
